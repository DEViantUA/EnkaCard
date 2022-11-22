# Copyright 2022 DEViantUa <t.me/deviant_ua>
# All rights reserved.
from PIL import Image, ImageFont
from .openFile import *
from io import BytesIO
import requests

class PillImg:
    def __init__(self, link = "", image = None):
        self.link = link
        self.image = image
        self.dowloadImg()

    def dowloadImg(self):
        if self.link != "":
            self.imgs = Image.open(BytesIO(requests.get(self.link).content))
        else:
            self.imgs = self.image
        
    def imagSize(self, fixed_width = 0, size = None):
        if size:
            new_image = self.imgs.resize(size)
        else:
            if self.imgs.size[0] != self.imgs.size[1]:
                ratio = (fixed_width / float(self.imgs.size[0]))
                height = int((float(self.imgs.size[1]) * float(ratio)))
                new_image = self.imgs.resize((fixed_width, height), Image.ANTIALIAS)
            else:
                new_image = self.imgs.resize((fixed_width,fixed_width))
        return new_image

    def imgD(self):
        return self.imgs.convert("RGBA")

    def centrText(self, text, witshRam = 100, razmer = 24, start = 0, Yram = 20, y = None, aling = "centry"):
        Text = ImageFont.truetype(font, razmer)
        maxDlina = witshRam
        while True:
            Text = ImageFont.truetype(font, razmer)
            withText = int(Text.getlength(str(text)))
            r = witshRam/2 
            t = withText/2 
            itog = r-t 
            if withText > maxDlina:
                razmer -= 1
                if razmer == 2:
                    break
                continue
            break
        if y:
            while True:
                Text = ImageFont.truetype(font, razmer)
                HegText = Text.getbbox(str(text))[3]
                maxHeg = Yram
                r = Yram/2 
                t = HegText/2 
                itogs = r-t 
                if HegText > maxHeg:
                    razmer -= 1
                    if razmer == 2:
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