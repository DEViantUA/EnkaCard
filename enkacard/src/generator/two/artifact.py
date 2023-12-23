from PIL import ImageDraw,Image
from ...utils import pill, git, options
from enkanetwork.enum import EquipmentsType
import asyncio
from collections import defaultdict

_of = git.ImageCache()

class ArtifactSets:
    def __init__(self,artifact, element) -> None:
        self.artifact = artifact
        self.element = pill.element_color_text.get(element, (149,107,5,255))
        
    async def start(self):
        background = Image.new("RGBA", (457, 59), (0,0,0,0))
        bg_count = await _of.artifact_set_count
        count = {}
        for item in filter(lambda x: x.type == EquipmentsType.ARTIFACT, self.artifact):
            if item.detail.artifact_name_set in count:
                count[item.detail.artifact_name_set] += 1
            else:
                count[item.detail.artifact_name_set] = 1

        set_name = {item: occurrences for item, occurrences in count.items() if occurrences > 1}
        position = [(0,21)]
        if len(set_name) == 2:
            position = [(0,0),(431,35)]
            
        font_16 = await pill.get_font(16)
        
        for i,key in enumerate(set_name):
            bg_coun = bg_count.copy()
            name = await pill.create_image_with_text(key, 17, max_width=398, color=self.element)

            dd = ImageDraw.Draw(bg_coun)
            if set_name[key] > 5:
                value = 4
            elif set_name[key] == 3:
                value = 2
            else:
                value = set_name[key]
            dd.text((6,2), str(value), font= font_16, fill=self.element)
            background.alpha_composite(bg_coun,position[i])
            
            if i == 0:
                background.alpha_composite(name,(position[i][0]+ 33,position[i][1]+2))
            else:
                background.alpha_composite(name,(int(position[i][0] - name.size[0] - 5) ,position[i][1]+2))
                           
        return background
 
class Artifact:
    
    def __init__(self, artifact,element) -> None:
        self.artifact = artifact
        self.CRIT_DMG = 0
        self.CRIT_RATE = 0 
        self.element = element
            
    async def add_icon_artifact(self):
        background = Image.new("RGBA", (457, 123), (0,0,0,0))
        self.background_icon = Image.new("RGBA", (457, 123), (0,0,0,0))
        icon, mask= await asyncio.gather(pill.get_dowload_img(self.artifact.detail.icon.url, size=((203,199))), _of.artifact_mask)
        background.alpha_composite(icon,(-49,-45))
        self.background_icon.paste(background.convert("RGBA"),(0,0),mask.convert("L"))
            
            
    async def build(self):
        self.background.alpha_composite(self.background_icon)
        self.background.alpha_composite(self.background_m_stat)
        self.background.alpha_composite(self.background_s_stat)
        await self.add_cv()
        
    async def add_dmg_and_rate(self,prop_id,value):
        if prop_id == "FIGHT_PROP_CRITICAL_HURT":
            self.CRIT_DMG += value
        if prop_id == "FIGHT_PROP_CRITICAL":
            self.CRIT_RATE += value
    
    async def creat_main_stat(self):
        stat_frame = await _of.artifact_eff
        self.background_m_stat = Image.new("RGBA", (457, 123), (0,0,0,0))
        self.background_m_stat.alpha_composite(stat_frame)
        element = pill.element_color_text.get(self.element, (149,107,5,255))
        icon,font_30,stars = await asyncio.gather(pill.get_icon_add(self.artifact.detail.mainstats.prop_id, size=(25,25)),pill.get_font(30),pill.get_stars(self.artifact.detail.rarity))
        
        self.background_m_stat.alpha_composite(icon,(154,6))
        self.background_m_stat.alpha_composite(stars.resize((83,24)),(98,98))
        
        level = f"+{self.artifact.level}"
        if str(self.artifact.detail.mainstats.type) == "DigitType.PERCENT":
            val = f"{self.artifact.detail.mainstats.value}%"
        else:
            val = str(self.artifact.detail.mainstats.value)

        d = ImageDraw.Draw(self.background_m_stat)
        x = font_30.getlength(val)
        d.text((int(179-x),39), val, font= font_30, fill=(0,0,0,255))
        d.text((int(180-x),40), val, font= font_30, fill=(255,255,255,255))
        
        x = self.font_17.getlength(level)
        d.text((int(130-x/2),10), level, font= self.font_17, fill= element)
        self.background_m_stat.alpha_composite(stars.resize((101,29)),(78,132))

        await self.add_dmg_and_rate(self.artifact.detail.mainstats.prop_id,self.artifact.detail.mainstats.value)
    
    async def add_sub_icon(self,key,x,y,d):
        if str(key.type) == "DigitType.PERCENT":
            val = f"{key.value}%"
        else:
            val = str(key.value)
                
        icon, _ = await asyncio.gather(pill.get_icon_add(key.prop_id, size=(23,23)), self.add_dmg_and_rate(key.prop_id,key.value))
        self.background_s_stat.alpha_composite(icon,(x,y))
        d.text((x+40,y+2), val, font= self.font_17 , fill=(255,255,255,255))
    
    async def add_sub_info(self):
        self.background_s_stat = Image.new("RGBA", (457, 123), (0,0,0,0))
        
        x,y = 206,22
        d = ImageDraw.Draw(self.background_s_stat)
        i = 0
        task = []
        for key in self.artifact.detail.substats:
            task.append(self.add_sub_icon(key,x,y,d))
            x = 332
            if i == 1:
                x,y = 206,75
            i += 1
            
        await asyncio.gather(*task)  
    
    async def add_cv(self):
        cv = f"{float('{:.2f}'.format(self.CRIT_DMG + (self.CRIT_RATE*2)))}CV"
        d = ImageDraw.Draw(self.background)
        x = self.font_17.getlength(cv)
        d.text((int(140-x/2),77), cv, font= self.font_17, fill=(255,255,255,255))
    
    
    async def start(self):
        self.background = Image.new("RGBA", (457, 123), (0,0,0,50))
        
        if self.artifact is None:
            return {"tcv": 0, "img": self.background} 
        
        self.font_17 = await pill.get_font(17)
        
        await self.add_icon_artifact()
        await self.creat_main_stat()
        await self.add_sub_info()
        await self.build()
     
        return {"tcv": float('{:.2f}'.format(self.CRIT_DMG + (self.CRIT_RATE*2))), "img": self.background}