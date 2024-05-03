from PIL import ImageFont,Image,ImageDraw,ImageStat,ImageFilter
from io import BytesIO
from . import git
import aiohttp,re, json,random
import numpy as np
import colorsys


from PIL import Image
from more_itertools import chunked

from cachetools import TTLCache
from collections import namedtuple
from math import sqrt


__all__ = (
    'get_average_color', 'get_dominant_colors',
    'get_distance_alpha',
    'get_background_alpha', 'get_foreground_alpha',
    'get_background_colors', 'get_foreground_colors',
)

element_color_text = {
   "Wind":(55,199,184,255),
   "Water":(55,167,199,255),
   "Rock":(199,157,55,255),
   "Ice":(55,199,197,255),
   "Electric":(170,55,199,255),
   "Fire":(202,69,69,255),
   "Grass":(60,159,76,255)
}

element_color = {
    "Wind": (5,149,134,255),
    "Water": (5,117,149,255),
    "Rock": (149,107,5,255),
    "Ice": (5,149,147,255),
    "Electric": (120,5,149,255),
    "Fire": (152,19,19,255),
    "Grass": (10,109,26,255)
}

async def apply_opacity(image, opacity=0.2):
    result_image = image.copy()
    alpha = result_image.split()[3]
    alpha = alpha.point(lambda p: int(p * opacity))
    result_image.putalpha(alpha)

    return result_image

async def recolor_image(image, target_color):
    result = Image.new('RGBA', image.size, target_color)
    
    if image.mode == 'RGBA':
        result.putalpha(image.split()[-1])
    
    return result

async def get_stars(level, light = False):
    if light:
        if level == 5:
            return await git.ImageCache().l_star5
        elif level == 4:
            return await git.ImageCache().l_star4
        elif level == 3:
            return await git.ImageCache().l_star3
        elif level == 2:
            return await git.ImageCache().l_star2
        else:
            return await git.ImageCache().l_star1
    
    if level == 5:
        return await git.ImageCache().star5
    elif level == 4:
        return await git.ImageCache().star4
    elif level == 3:
        return await git.ImageCache().star3
    elif level == 2:
        return await git.ImageCache().star2
    else:
        return await git.ImageCache().star1


async def get_icon_add(prop_id, recolor = (255,255,255), size = None):
    if f"{prop_id}_{recolor}_{size}" in cache:
        return cache[f"{prop_id}_{recolor}_{size}"]
    
    icon = await git.ImageCache().download_icon_stats(prop_id = prop_id)
    if "ADD_HURT" not in prop_id and prop_id != "FIGHT_PROP_PHYSICAL_ADD_HURT":
        icon = await recolor_image(icon,recolor)
    if size:
        icon.thumbnail(size)
        cache[f"{prop_id}_{recolor}_{size}"] = icon.convert("RGBA").copy()
        return cache[f"{prop_id}_{recolor}_{size}"]
    else:
        cache[f"{prop_id}_{recolor}_{size}"] = icon.convert("RGBA").copy()
        return cache[f"{prop_id}_{recolor}_{size}"]

async def get_font(size):
    return ImageFont.truetype(git.font, size)

cache = TTLCache(maxsize=1000, ttl=300)  

async def get_dowload_img(link,size = None, thumbnail_size = None):
    cache_key = json.dumps((link, size, thumbnail_size), sort_keys=True)  # Преобразовываем в строку
        
    if cache_key in cache:
        return cache[cache_key]
    headers_p = {}
    try:
        if "pximg" in link:
            headers_p = {
                "referer": "https://www.pixiv.net/",
            }
        async with aiohttp.ClientSession(headers=headers_p) as session, session.get(link) as r:
            try:
                image = await r.read()
            finally:
                await session.close()
    except:
        raise
    
    image = Image.open(BytesIO(image)).convert("RGBA")
    if size:
        image = image.resize(size)
        cache[cache_key] = image
        return image
    elif thumbnail_size:
        image.thumbnail(thumbnail_size)
        cache[cache_key] = image
        return image
    else:
        cache[cache_key] = image
        return image


async def get_centr_honkai_art(size, file_name):
    background_image = Image.new('RGBA', size, color=(0, 0, 0, 0))
    foreground_image = file_name.convert("RGBA")

    scale = max(size[0] / foreground_image.size[0], size[1] / foreground_image.size[1])
    foreground_image = foreground_image.resize((int(foreground_image.size[0] * scale), int(foreground_image.size[1] * scale)), resample=Image.BICUBIC)

    background_size = background_image.size
    foreground_size = foreground_image.size

    x = background_size[0] // 2 - foreground_size[0] // 2

    if foreground_size[1] > background_size[1]:
        y_offset = max(int(0.3 * (foreground_size[1] - background_size[1])), int(0.5 * (-foreground_size[1])))
        y = -y_offset
    else:
        y = background_size[1] // 2 - foreground_size[1] // 2

    background_image.alpha_composite(foreground_image, (x, y))

    return background_image

Point = namedtuple('Point', ('coords', 'n', 'ct'))
Cluster = namedtuple('Cluster', ('points', 'center', 'n'))

def get_points(img):
    points = []
    w, h = img.size
    for count, color in img.getcolors(w * h):
        points.append(Point(color, 3, count))
    return points

rtoh = lambda rgb: '#%s' % ''.join(('%02x' % p for p in rgb))

def colorz(img, n=3):
    img = img.copy()
    img.thumbnail((200, 200))
    w, h = img.size

    points = get_points(img)
    clusters = kmeans(points, n, 1)
    rgbs = [map(int, c.center.coords) for c in clusters]
    
    return map(rtoh, rgbs)

def euclidean(p1, p2):
    return sqrt(sum([
        (p1.coords[i] - p2.coords[i]) ** 2 for i in range(p1.n)
    ]))

def calculate_center(points, n):
    vals = [0.0 for i in range(n)]
    plen = 0
    for p in points:
        plen += p.ct
        for i in range(n):
            vals[i] += (p.coords[i] * p.ct)
    return Point([(v / plen) for v in vals], n, 1)

def kmeans(points, k, min_diff):
    clusters = [Cluster([p], p, p.n) for p in random.sample(points, k)]

    while 1:
        plists = [[] for i in range(k)]

        for p in points:
            smallest_distance = float('Inf')
            for i in range(k):
                distance = euclidean(p, clusters[i].center)
                if distance < smallest_distance:
                    smallest_distance = distance
                    idx = i
            plists[idx].append(p)

        diff = 0
        for i in range(k):
            old = clusters[i]
            center = calculate_center(plists[i], old.n)
            new = Cluster(plists[i], center, old.n)
            clusters[i] = new
            diff = max(diff, euclidean(old.center, new.center))

        if diff < min_diff:
            break
    
    return clusters

async def light_level(pixel_color):
    h, l, s = colorsys.rgb_to_hls(*(x / 255 for x in pixel_color[:3]))    
    return l

async def _get_light_pixel_color(pixel_color):
    h, l, s = colorsys.rgb_to_hls(*(x / 255 for x in pixel_color[:3]))
    l = min(max(0.2, l), 0.8)

    return tuple(round(x * 255) for x in colorsys.hls_to_rgb(h, l, s))
  
async def _get_dark_pixel_color(pixel_color):
    h, l, s = colorsys.rgb_to_hls(*(x / 255 for x in pixel_color[:3]))
    l = min(max(0.8, l), 0.2)
    a = tuple(round(x * 255) for x in colorsys.hls_to_rgb(h, l, s))
    
    return  a


async def get_color_art(img):
    a = colorz(img, n = 2)
    a = list(a)[0].lstrip('#')
    color_palette = tuple(int(a[i:i+2], 16) for i in (0, 2, 4))
    
    ll = await light_level(color_palette)
    
    if ll < 45:
        color_palette = await _get_light_pixel_color(color_palette)
    elif ll > 200:
        color_palette = await _get_dark_pixel_color(color_palette)
    return color_palette


async def create_image_with_text(text, font_size, max_width=336, color=(255, 255, 255, 255), alg="Left"):
    
    key = (text, font_size, max_width, color, alg)
    if key in cache:
        return cache[key]
    
    font = await get_font(font_size)

    lines = []
    line = []
    for word in text.split():
        if line:
            temp_line = line + [word]
            temp_text = ' '.join(temp_line)
            temp_width = font.getmask(temp_text).getbbox()[2]
            if temp_width <= max_width:
                line = temp_line
            else:
                lines.append(line)
                line = [word]
        else:
            line = [word]
    if line:
        lines.append(line)

    width,height = 0, 0
    
    for line in lines:
        line_width = font.getmask(' '.join(line)).getbbox()[2]
        width = max(width, line_width)
        height += font.getmask(' '.join(line)).getbbox()[3]

    img = Image.new('RGBA', (min(width, max_width), height + (font_size)), color=(255, 255, 255, 0))

    draw = ImageDraw.Draw(img)
    
    y_text = 0
    for line_num, line in enumerate(lines):
        text_width, text_height = font.getmask(' '.join(line)).getbbox()[2:]
        if alg == "center" and line_num > 0:
            x_text = (max_width - text_width) // 2
        else:
            x_text = 0
        draw.text((x_text, y_text), ' '.join(line), font=font, fill=color)
        y_text += text_height + 5
        
    cache[key] = img
    
    return img


async def get_average_color(image):
    if image.mode != 'RGBA':
        image = image.convert('RGBA')
    
    channels = image.split()
    
    return (
        round(np.average(channels[0], weights=channels[-1])),
        round(np.average(channels[1], weights=channels[-1])),
        round(np.average(channels[2], weights=channels[-1])),
    )


async def get_dominant_colors(
    image,
    number,
    *,
    dither=Image.Quantize.FASTOCTREE,
    common=True,
):
    if image.mode != 'RGB':
        if image.mode != 'RGBA':
            image = image.convert('RGBA')
        
        if not common:
            width = image.width
            height = image.height
            
            image = Image.fromarray(np.array([np.repeat(
                np.reshape(image.convert('RGB'), (width * height, 3)),
                np.reshape(image.split()[-1], width * height),
                0,
            )]), 'RGB')
    
    if image.mode == 'RGBA':
        if dither == Image.Quantize.FASTOCTREE:
            simple_image = image.copy()
            simple_image.putalpha(255)
        else:
            simple_image = image.convert('RGB')
    else:
        simple_image = image
    
    reduced = simple_image.quantize(dither=dither, colors=number)
    
    palette = [*chunked(reduced.getpalette(), 3)]
    
    if common and image.mode == 'RGBA':
        alpha = np.array(image.split()[-1])
        
        colors = sorted((
            (
                np.sum(alpha * reduced.point([0] * i + [1] + [0] * (255 - i))),
                tuple(palette[i]),
            )
            for _, i in reduced.getcolors()
        ), reverse=True)
    else:
        colors = [
            (n, tuple(palette[i]))
            for n, i in sorted(reduced.getcolors(), reverse=True)
        ]
    
    return tuple(colors)


async def get_distance_alpha(image, converter=(lambda x: x)):
    width = image.width
    height = image.height
    
    radius = np.hypot(1, 1)
    
    return Image.fromarray(np.fromfunction(
        lambda y, x: np.uint8(255 * converter(np.hypot(
            2 * x / (width - 1) - 1,
            2 * y / (height - 1) - 1,
        ) / radius)),
        (height, width),
    ), 'L')


async def get_background_alpha(image):
    return await get_distance_alpha(
        image,
        lambda x: x * np.sin(x * np.pi / 2),
    )


async def get_foreground_alpha(image):
    return await get_distance_alpha(
        image,
        lambda x: 1 - x * np.sin(x * np.pi / 2),
    )

async def get_background_colors(image,number,*,common=False,radius=1,quality=None):
    if quality is not None:
        image = image.copy()
        image.thumbnail((quality, quality), 0)
    
    if radius > 1:
        image = image.filter(ImageFilter.BoxBlur(radius))
    
    filtered_image = image.convert('RGB')
    
    if image.mode != 'RGBA':
        filtered_image.putalpha(await get_background_alpha(image))
    else:
        filtered_image.putalpha(Image.fromarray(np.uint8(
            np.uint16(await get_background_alpha(image))
            * image.split()[-1]
            / 255
        ), 'L'))
    
    color_palette = await get_dominant_colors(filtered_image, number, common=common)
    color_palette = color_palette[0][1]
    ll = await light_level(color_palette)
    if ll < 0.15:
        color_palette = await _get_light_pixel_color(color_palette)
    elif ll > 0.80:
        color_palette = await _get_dark_pixel_color(color_palette)
        
        
    return color_palette
     


async def get_foreground_colors(image,number,*,common=False,radius=1,quality=None):
    if quality is not None:
        image = image.copy()
        image.thumbnail((quality, quality), 0)
    
    if radius > 1:
        image = image.filter(ImageFilter.BoxBlur(radius))
    
    filtered_image = image.convert('RGB')
    
    if image.mode != 'RGBA':
        filtered_image.putalpha(await get_foreground_alpha(image))
    else:
        filtered_image.putalpha(Image.fromarray(np.uint8(
            np.uint16(await  get_foreground_alpha(image))
            * image.split()[-1]
            / 255
        ), 'L'))
    
    return await  get_dominant_colors(filtered_image, number, common=common)


async def apply_opacity(image, opacity=0.2):
    result_image = image.copy()
    alpha = result_image.split()[3]
    alpha = alpha.point(lambda p: int(p * opacity))
    result_image.putalpha(alpha)

    return result_image
    
class GradientGenerator:
    def __init__(self, source_img_path):
        self.source_img = source_img_path
        self.frame = ()
        self.source_width, self.source_height = self.source_img.size

    async def generate(self, width, height, left = False):
        gradient_img = Image.new("RGB", (width, height))

        # Вычисляем ширину и высоту каждой полосы градиента
        top_height = height // 3
        bottom_height = height // 3
        center_height = height - top_height - bottom_height
        # Определяем координаты точек, с которых будем брать цвета
        if left:
            left = 3
            right = 4
        else:
            left = self.source_width - 142
            right = self.source_width - 141
        top_1 = 1
        bottom_1 = top_height - 1
        top_2 = top_height + 1
        bottom_2 = top_height + center_height - 1
        top_3 = top_height + center_height + 1
        bottom_3 = height - 2

        top_color = await self._get_pixel_color(left, top_1, right, bottom_1)
        ll = await light_level(top_color)
        if ll < 45:
            top_color = await _get_light_pixel_color(top_color)
        elif ll > 200:
            top_color = await _get_dark_pixel_color(top_color)

        center_color = await self._get_pixel_color(left, top_2, right, bottom_2)
        
        ll = await light_level(center_color)
        if ll < 45:
            center_color = await _get_light_pixel_color(center_color)
        elif ll > 200:
            center_color = await _get_dark_pixel_color(center_color)

        bottom_color = await self._get_pixel_color(left, top_3, right, bottom_3)
        ll = await light_level(bottom_color)
        if ll < 45:
            bottom_color = await _get_light_pixel_color(bottom_color)
        elif ll > 200:
            bottom_color = await _get_dark_pixel_color(bottom_color)

        for y in range(top_height):
            for x in range(width):
                ratio = y / (top_height - 1)
                gradient_color = self._get_interpolated_color(top_color, center_color, ratio)
                gradient_img.putpixel((x, y), gradient_color)

        for y in range(center_height):
            for x in range(width):
                ratio = y / (center_height - 1)
                gradient_color = self._get_interpolated_color(center_color, bottom_color, ratio)
                gradient_img.putpixel((x, y + top_height), gradient_color)

        for y in range(bottom_height):
            for x in range(width):
                gradient_color = bottom_color
                gradient_img.putpixel((x, y + top_height + center_height), gradient_color)

        return gradient_img

    async def _get_pixel_color(self, left, top, right, bottom):
        cropped_img = self.source_img.crop((left, top, right, bottom))
        resized_img = cropped_img.convert("RGB").resize((1, 1))
        pixel_color = resized_img.getpixel((0, 0))
        
        return pixel_color
    
    def _get_interpolated_color(self, start_color, end_color, ratio):
        return tuple(int(start_color[i] + (end_color[i] - start_color[i]) * ratio) for i in range(3))