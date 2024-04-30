from PIL import Image,ImageChops,ImageFilter
from ...utils import pill, git
import asyncio


_of = git.ImageCache()

class Background:
    def __init__(self,img,element, setting) -> None:
        self.img = img
        self.element = element
        self.element_color = None
        self.setting = setting
        
    async def get_element_color(self):
        self.element_color = pill.element_color.get(self.element, (149,107,5,255))
        self.background_grandient = Image.new("RGBA", (1950, 813), self.element_color)
        

    async def add_overlay(self):
        overlay = await _of.overlay_bg
        self.grandient = ImageChops.soft_light(self.grandient, overlay.convert("RGBA"))
        self.background_grandient = ImageChops.soft_light(self.grandient, overlay.convert("RGBA"))

    async def creat_grandient(self):
        if self.element is None:
            self.grandient = await pill.GradientGenerator(self.img).generate(1, 813)
            self.grandient = self.grandient.resize((1950, 813)).convert("RGBA")
        else:
            self.grandient = Image.new("RGBA", (1950, 813), self.element_color)
            
        userImages_opacity = await pill.apply_opacity(self.img, opacity=0.6)
        if self.element is None:
            self.grandient.alpha_composite(userImages_opacity,(1242+ self.setting,0))
            self.grandient = self.grandient.filter(ImageFilter.GaussianBlur(30))
        else:
            self.grandient.alpha_composite(userImages_opacity,(698,-75))
            self.grandient = self.grandient.filter(ImageFilter.GaussianBlur(20))
        await self.add_overlay()
        shadow = Image.new("RGBA", (1950, 813), (0,0,0,50))
        
        self.grandient.alpha_composite(shadow,(0,0))
        line = await _of.line_bg
        self.grandient.alpha_composite(line,(-17,0))
        
    
    async def add_mask(self):
        maska_bg = await _of.maska_bg
        maska_bg = maska_bg.convert("L")
        
        mask =  await _of.total_mask_bg
        mask = mask.convert("L")
        
        self.background = Image.new("RGBA", (1950, 813), (0,0,0,0))
        
        if self.element is None:
            self.background_grandient.alpha_composite(self.img,(1242+ self.setting,0))
        else:
            self.background_grandient.alpha_composite(self.img,(698,-75))
        self.background_grandient.paste(self.grandient,(0,0),maska_bg)
        self.background.paste(self.background_grandient,(0,0),mask)       
    
    async def creat_art(self):
        if self.element is None:
            self.img = await pill.get_centr_honkai_art((798,821),self.img)
    
    async def start(self):
        self.img = await pill.get_dowload_img(self.img)   
        if not self.element is None:
            await self.get_element_color()
        else:
            self.background_grandient = Image.new("RGBA", (1950, 813), (0,0,0,255))
        await self.creat_art()
        await self.creat_grandient()
        await self.add_mask()
                
        return self.background 