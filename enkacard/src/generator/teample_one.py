# Copyright 2023 DEViantUa <t.me/deviant_ua>
# All rights reserved.
import asyncio
from PIL import ImageDraw,Image
from ..utils import pill, git
from enkanetwork.enum import EquipmentsType
from .one import background, artifact, weapon, constant, skill, stat, prop
_of = git.ImageCache()
 
class Creat:
    def __init__(self,characters,lang,img,hide,uid,name) -> None:
        self.character = characters
        self.lang = lang["lvl"]
        self.img = img
        self.hide = hide
        self.uid = uid
        self.name = name
        
        
    
    async def creat_name_user(self):
        self.background_name_user = Image.new("RGBA", (249, 49), (0,0,0,0))
        font_20 = await pill.get_font(20)
        d = ImageDraw.Draw(self.background_name_user)
        d.text((0,0), self.name, font= font_20, fill=(255,255,255,150))
        if self.hide:
            d.text((0,25), "UID: Hide", font= font_20, fill=(255,255,255,150))
        else:
            d.text((0,25), f"UID: {self.uid}", font= font_20, fill=(255,255,255,150))
            
    
    async def collect_background(self):
        if self.img:
            self.background =  await background.Background(self.img, None).start()
        else:
            self.background = await background.Background(self.character.image.banner.url,self.character.element.value).start()
        
    async def collect_artifact(self):
        task_art = []
        task_prop = []
        ids_next = {"4": None,"2": None,"5": None,"1": None,"3": None}
        for key in filter(lambda x: x.type == EquipmentsType.ARTIFACT, self.character.equipments):
            ids = key.detail.icon.filename[-1:]
            ids_next[ids] = key
        
        for key in ids_next:
            task_art.append(artifact.Artifact(ids_next[key]).start())
            if not ids_next[key] is None:
                task_prop.append(prop.Prop(ids_next[key]).start())
        
        results = await asyncio.gather(*task_art, *task_prop)
        self.artifact = results[:len(task_art)]
        self.prop = results[len(task_art):]

    async def collect_sets(self):
        self.artifact_sets = await artifact.ArtifactSets(self.character.equipments).start()
    
    async def creat_name(self):
        self.background_name = Image.new("RGBA", (479, 149), (0,0,0,0))
        name = self.character.name
        level = f"{self.lang}: {self.character.level}/{self.character.max_level}"
        stars = await pill.get_stars(self.character.rarity)
        friends = str(self.character.friendship_level)
        font_25 = await pill.get_font(25)
        d = ImageDraw.Draw(self.background_name)
        x = font_25.getlength(name)
        d.text((int(468-x),0), name, font= font_25, fill=(255,255,255,255))
        x = font_25.getlength(level)
        d.text((int(468-x),40), level, font= font_25, fill=(255,255,255,255))
        friends_icon = await pill.get_icon_add("FRIENDS", size=(44,44))
        self.background_name.alpha_composite(stars.resize((101,29)),(378,120))
        self.background_name.alpha_composite(friends_icon,(428,76))
        x = font_25.getlength(friends)
        d.text((int(424-x),87), friends, font= font_25, fill=(255,255,255,255))
        
    async def creat_skill(self): 
        task = []
        self.background_skill = Image.new("RGBA", (97, 387), (0,0,0,0))
        for key in self.character.skills:
            task.append(skill.Skill(key,self.character.element.value).start())
        
        result = await asyncio.gather(*task)
        
        y = 0
        for key in result:
            self.background_skill.alpha_composite(key,(0,y))
            y += 146
            
        
    async def build(self):
        y = 239
        self.tcv = 0
        for key in self.artifact:
            self.background.alpha_composite(key["img"],(941,y))
            y += 168
            self.tcv += key["tcv"]
        
        self.background.alpha_composite(self.artifact_sets,(941,1100))
        self.background.alpha_composite(self.weapon["img"],(941,16))
        self.background.alpha_composite(self.background_name,(451,426))
        self.background.alpha_composite(self.background_constant, (10,494))
        self.background.alpha_composite(self.background_skill,(809,656))
        self.background.alpha_composite(self.background_stat, (11,16))
        self.background.alpha_composite(self.background_name_user,(11,1216))
        self.tcv += self.weapon["tcv"]
        await self.add_tcr()
    
    async def add_tcr(self):
        background_tcv = await _of.tcv
        background_tcv = background_tcv.copy()
        font_23 = await pill.get_font(23)
        d = ImageDraw.Draw(background_tcv)
        self.tcv = float('{:.2f}'.format(self.tcv))
        x = font_23.getlength(f"{self.tcv}TCV")
        d.text((int(76-x/2),4), f"{self.tcv}TCV", font= font_23, fill=(255,255,255,255))
        
        self.background.alpha_composite(background_tcv,(660,506))
    
    async def add_logo(self):
        logo = await _of.logo
        self.background.alpha_composite(logo, (1163,1216))
    
    async def collect_weapon(self):
        self.weapon = await weapon.Weapon(self.character.equipments[-1], self.lang).start()
    
    async def collect_constant(self):
        self.background_constant = Image.new("RGBA", (108, 672), (0,0,0,0))
        task = []
        y = 0
        for key in self.character.constellations:
            task.append(constant.Constant(key,self.character.element.value).start())
        
        result = await asyncio.gather(*task)
        
        for key in result:
            self.background_constant.alpha_composite(key,(0,y))
            y += 112
        
        
    async def collect_stat(self):
        self.background_stat = await stat.Stat(self.character.stats, self.prop, self.character.element.value).start()
        
    async def start(self):       
        tasks = [self.collect_artifact(), self.creat_name_user(),self.collect_background()]
        await asyncio.gather(*tasks)
        tasks = [
            self.collect_weapon(),
            self.creat_skill(),
            self.collect_sets(),
            self.collect_constant(),
            self.creat_name(),
            self.add_logo(),
            self.collect_stat()
        ]

        await asyncio.gather(*tasks)

        await self.build()

        return {
            "id": self.character.id,
            "name": self.character.name,
            "element": self.character.element.value,
            "rarity": self.character.rarity,
            "card": self.background
        }
