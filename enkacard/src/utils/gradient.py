# Copyright 2022 DEViantUa <t.me/deviant_ua>
# All rights reserved.
from PIL import Image, ImageDraw
import random
from collections import namedtuple
from math import sqrt
import random
import numpy
from numpy import dtype

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

def userAdaptGrandient(userImg, size = (1502, 787), left = False):
    if left:
        userImg = userImg.crop((0,0,userImg.size[0]+3-userImg.size[0],userImg.size[1]))
    else:
        userImg = userImg.crop((userImg.size[0]-1,0,userImg.size[0],userImg.size[1]))
    rgb = list(userImg.getdata())
    indx = random.choice([1,30])
    color_palette = (rgb[indx],rgb[int(len(rgb)/2)],rgb[len(rgb)-100])
    color_palette = list(color_palette)
    if color_palette[0][0] > 209 and color_palette[0][1] > 209 and color_palette[0][2] >  209:
        color_palette[0] = (209,209,209)
    if color_palette[1][0] > 209 and color_palette[1][1] > 209 and color_palette[1][2] >  209:
        color_palette[1] = (209,209,209)
    if color_palette[2][0] > 209 and color_palette[2][1] > 209 and color_palette[2][2] >  209:
        color_palette[2] = (209,209,209)
    color_palette = tuple(color_palette)
    region = Rect(0, 0, size[0], size[1])
    image = Image.new("RGBA", size, (0,0,0,0))  
    vertGradient(image, region, gradientColor, color_palette) 
    return image

def frameAdapt(color_palette, size = (388, 621)):
    color_palette = list(color_palette)
    if color_palette[0][0] > 209 and color_palette[0][1] > 209 and color_palette[0][2] >  209:
        color_palette[0] = (209,209,209)
    if color_palette[1][0] > 209 and color_palette[1][1] > 209 and color_palette[1][2] >  209:
        color_palette[1] = (209,209,209)
    if color_palette[2][0] > 209 and color_palette[2][1] > 209 and color_palette[2][2] >  209:
        color_palette[2] = (209,209,209)
    color_palette = tuple(color_palette)
    region = Rect(0, 0, size[0], size[1])
    image = Image.new("RGBA", size, (0,0,0,0))  
    vertGradient(image, region, gradientColor, color_palette) 
    return image





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


async def colorBg(img):
    a = colorz(img, n = 2)
    a = list(a)[0].lstrip('#')
    color_palette = list(int(a[i:i+2], 16) for i in (0, 2, 4))
    if color_palette[0]> 209:
        color_palette[0] = 209
    if color_palette[1]> 209:
        color_palette[1] = 209
    if color_palette[1]> 209:
        color_palette[1] = 209
    return tuple(color_palette)
