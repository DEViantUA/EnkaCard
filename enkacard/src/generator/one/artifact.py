from PIL import ImageDraw,Image
from ...utils import pill, git, options
from enkanetwork.enum import EquipmentsType
import asyncio
from collections import defaultdict

_of = git.ImageCache()

class ArtifactSets:
    def __init__(self,artifact) -> None:
        self.artifact = artifact
    
    async def start(self):
        background =  await _of.sets
        background = background.copy()
        count = {}
        for item in filter(lambda x: x.type == EquipmentsType.ARTIFACT, self.artifact):
            if item.detail.artifact_name_set in count:
                count[item.detail.artifact_name_set] += 1
            else:
                count[item.detail.artifact_name_set] = 1

        set_name = {item: occurrences for item, occurrences in count.items() if occurrences > 1}
        position = [(275,31)]
        if len(set_name) == 2:
            position = [(275,14),(275,52)]
            
        font_20 = await pill.get_font(20)
        d = ImageDraw.Draw(background)
        
               
        for i,key in enumerate(set_name):
            name = await pill.create_image_with_text(key, 20, max_width=316, color=(133, 255, 142, 255))
            value = str(set_name[key])
            x = font_20.getlength(value)
            d.text((int(508-x),position[i][1]), value, font= font_20, fill=(255,255,255,255))
            background.alpha_composite(name,(int(275-name.size[0]/2),position[i][1]))
        
        return background


class Artifact:
    def __init__(self, artifact) -> None:
        self.artifact = artifact
        self.CRIT_DMG = 0
        self.CRIT_RATE = 0
        self.props = {}
        self.prop_value = {}
        self.prop_id_counts = defaultdict(int)
        
        self.add_icons = False
    
    async def creat_prop_id_count(self):
        if self.prop_id_counts == {}:
            for p in self.artifact.props:
                self.prop_id_counts[p.prop_id] += 1
        
    async def creat_artifact_up(self, sub):
        countProc = self.prop_id_counts.get(sub.prop_id, 0)
        color = options.color_artifact_up.get(countProc, (235, 142, 255, 255))
        countProc = f"+{countProc}"

        icon, bg_up, font_17 = await asyncio.gather(
            pill.get_icon_add(sub.prop_id, size=(23, 24)),
            _of.artifact_up,
            pill.get_font(17)
        )
        icon = await pill.apply_opacity(icon, opacity=0.5)

        bg = bg_up.copy()
        bg.alpha_composite(icon, (4, 1))

        d = ImageDraw.Draw(bg)
        x = font_17.getlength(countProc)
        d.text((int(14 - x / 2), 4), countProc, font=font_17, fill=(0, 0, 0, 255))
        d.text((int(15 - x / 2), 3), countProc, font=font_17, fill=color)
                           
        return bg
    
    async def add_cv(self):
        cv = f"{float('{:.2f}'.format(self.CRIT_DMG + (self.CRIT_RATE*2)))}CV"
        d = ImageDraw.Draw(self.background)
        x = self.font_20.getlength(cv)
        d.text((int(260-x/2),12), cv, font= self.font_20, fill=(255,255,255,255))
        
    async def add_dmg_and_rate(self,prop_id,value):
        if prop_id == "FIGHT_PROP_CRITICAL_HURT":
            self.CRIT_DMG += value
        if prop_id == "FIGHT_PROP_CRITICAL":
            self.CRIT_RATE += value
    
    async def add_icon(self):
        
        background = Image.new("RGBA", (537, 161), (0,0,0,0))
        background_two = Image.new("RGBA", (537, 161), (0,0,0,0))
        icon, mask= await asyncio.gather(pill.get_dowload_img(self.artifact.detail.icon.url, size=((201,201))), _of.mask_artifact)
        background.alpha_composite(icon,(-38,-20))
        background_two.paste(background.convert("RGBA"),(0,0),mask.convert("L"))
        
        self.background.alpha_composite(background_two)
    
    async def add_main_info(self):
        icon,font_30,stars = await asyncio.gather(pill.get_icon_add(self.artifact.detail.mainstats.prop_id, size=(39,39)),pill.get_font(30),pill.get_stars(self.artifact.detail.rarity))
        self.background.alpha_composite(icon,(133,17))
        
        level = f"+{self.artifact.level}"
        if str(self.artifact.detail.mainstats.type) == "DigitType.PERCENT":
            val = f"{self.artifact.detail.mainstats.value}%"
        else:
            val = str(self.artifact.detail.mainstats.value)

        d = ImageDraw.Draw(self.background)
        x = font_30.getlength(val)
        d.text((int(172-x),66), val, font= font_30, fill=(0,0,0,255))
        d.text((int(173-x),68), val, font= font_30, fill=(255,255,255,255))
        
        x = self.font_20.getlength(level)
        d.text((int(149-x/2),109), level, font= self.font_20, fill=(255,211,91,255))
        self.background.alpha_composite(stars.resize((101,29)),(78,132))

        await self.add_dmg_and_rate(self.artifact.detail.mainstats.prop_id,self.artifact.detail.mainstats.value)
        
    async def add_sub_icon(self,key,x,y,z,d,font_25,i):
        if str(key.type) == "DigitType.PERCENT":
            val = f"{key.value}%"
        else:
            val = str(key.value)
                
        icon, icon_up, _ = await asyncio.gather(pill.get_icon_add(key.prop_id, size=(33,33)), self.creat_artifact_up(key), self.add_dmg_and_rate(key.prop_id,key.value))
        self.background.alpha_composite(icon,(x,y))
        d.text((x+40,y+3), val, font= font_25, fill=(255,255,255,255))
                    
        self.background.alpha_composite(icon_up,(z,10))

    async def add_sub_info(self):
        x,y,z = 203,49,331
        font_25 = await pill.get_font(25)
        d = ImageDraw.Draw(self.background)
        
        i = 0
        task = []
        for key in self.artifact.detail.substats:
            task.append(self.add_sub_icon(key,x,y,z,d,font_25,i))
            x = 369
            if i == 1:
                x,y = 203,103
                
            z += 38
            i += 1
        await asyncio.gather(*task)      
        
    async def start(self):
        if self.artifact is None:
            return {"tcv": 0, "img": await _of.artifact_bg_none} 
        self.font_20,self.background,_ = await asyncio.gather(pill.get_font(20),_of.artifact_bg,self.creat_prop_id_count())
        self.background = self.background.copy()
        await self.add_icon()
        
        task = [self.add_sub_info(),self.add_main_info()]
               
        await asyncio.gather(*task)
        await self.add_cv()
        
        

        return {"tcv": float('{:.2f}'.format(self.CRIT_DMG + (self.CRIT_RATE*2))), "img": self.background}