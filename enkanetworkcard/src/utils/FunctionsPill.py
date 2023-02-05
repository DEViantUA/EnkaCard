# Copyright 2022 DEViantUa <t.me/deviant_ua>
# All rights reserved.
from PIL import Image, ImageFont
from . import openFile
from io import BytesIO
import aiohttp
from asyncache import cached
from cachetools import TTLCache

@cached(TTLCache(200, ttl=20))  
async def dowloadImg(link = ""):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as response:
                return await response.read()
    except:
        raise

async def imagSize(link = "", image = None, fixed_width = 0, size = None):
    if not image:
        imgs = await dowloadImg(link = link)
        imgs = Image.open(BytesIO(imgs))
    else:
        imgs = image
    if size:
        new_image = imgs.resize(size)
    else:
        if imgs.size[0] != imgs.size[1]:
            ratio = (fixed_width / float(imgs.size[0]))
            height = int((float(imgs.size[1]) * float(ratio)))
            new_image = imgs.resize((fixed_width, height), Image.LANCZOS)
        else:
            new_image = imgs.resize((fixed_width,fixed_width))
    return new_image

async def imgD(link = ""):
    imgs = await dowloadImg(link = link)
    imgs = Image.open(BytesIO(imgs))
    return imgs.convert("RGBA")

@cached(TTLCache(80, ttl=30))  
async def centrText(text, witshRam = 100, razmer = 24, start = 0, Yram = 20, y = None, aling = "centry"):
    Text = ImageFont.truetype(openFile.font, razmer)
    maxDlina = witshRam
    while True:
        Text = ImageFont.truetype(openFile.font, razmer)
        withText = int(Text.getlength(str(text)))
        r = witshRam/2 
        t = withText/2 
        itog = r-t 

        if withText > maxDlina:
            razmer -= 1
            if razmer <= 2:
                break
            continue
        break
    if y:
        while True:
            Text = ImageFont.truetype(openFile.font, razmer)
            HegText = Text.getbbox(str(text))[3]
            maxHeg = Yram
            r = Yram/2 
            t = HegText/2 
            itogs = r-t 

            if HegText > maxHeg:
                razmer -= 1
                if razmer <= 2:
                    break
                continue
            break
        
        if aling == "centry":
            return (int(start + itog),int(y + itogs)),Text
        else:
            return (int(start),int(y)),Text

    if aling == "centry":
        return int(start + itog),Text
    else:
        return int(start),Text
