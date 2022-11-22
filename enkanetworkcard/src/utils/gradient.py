# Copyright 2022 DEViantUa <t.me/deviant_ua>
# All rights reserved.
from PIL import Image, ImageDraw

class Mark(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

class Rect(object):
    def __init__(self, x1, y1, x2, y2):
        minx, maxx = (x1,x2) if x1 < x2 else (x2,x1)
        miny, maxy = (y1,y2) if y1 < y2 else (y2,y1)
        self.min = Mark(minx, miny)
        self.max = Mark(maxx, maxy)

    width  = property(lambda self: self.max.x - self.min.x)
    height = property(lambda self: self.max.y - self.min.y)

def gradientColor(minval, maxval, val, color_palette):
    max_index = len(color_palette)-1
    delta = maxval - minval
    if delta == 0:
        delta = 1
    v = float(val-minval) / delta * max_index
    i1, i2 = int(v), min(int(v)+1, max_index)
    (r1, g1, b1), (r2, g2, b2) = color_palette[i1], color_palette[i2]
    f = v - i1
    return int(r1 + f*(r2-r1)), int(g1 + f*(g2-g1)), int(b1 + f*(b2-b1))

def vertGradient(image, rect, color_func, color_palette):
    draw = ImageDraw.Draw(image)
    minval, maxval = 1, len(color_palette)
    delta = maxval - minval
    height = float(rect.height) 
    for y in range(rect.min.y, rect.max.y+1):
        f = (y - rect.min.y) / height
        val = minval + f * delta
        color = color_func(minval, maxval, val, color_palette)
        draw.line([(rect.min.x, y), (rect.max.x, y)], fill=color)


def userAdaptGrandient(userImg, size = (1503, 788), left = False):
    if left:
        userImg = userImg.crop((0,0,userImg.size[0]+3-userImg.size[0],userImg.size[1]))
    else:
        userImg = userImg.crop((userImg.size[0]-1,0,userImg.size[0],userImg.size[1]))
    rgb = list(userImg.getdata())
    color_palette = (rgb[30],rgb[int(len(rgb)/2-73)],rgb[len(rgb)-200])
    region = Rect(0, 0, size[0], size[1])
    image = Image.new("RGBA", size, (0,0,0,0))  
    vertGradient(image, region, gradientColor, color_palette) 
    return image

