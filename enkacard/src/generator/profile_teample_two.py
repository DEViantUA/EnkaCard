import asyncio
import random
from PIL import ImageDraw,Image,ImageChops
from ..utils import pill, git, options

_of = git.ImageCache()

class ProfileCard:
    def __init__(self,profile,lang,img,hide,uid,background) -> None:
        self.profile = profile
        self.lang = lang
        self.img = img
        self.hide = hide
        self.uid = uid
        self.background = background
    
    
    async def creat_background(self):
        self.background_profile = Image.new("RGBA", (828, 1078), (0,0,0,0))
        
        maska,frame = await asyncio.gather(_of.maska_prof_bg,_of.frame_profile)
        if self.background is None:
            background_image = random.choice([await _of.bg_1, await  _of.bg_2, await  _of.bg_3])
            background_shadow = Image.new("RGBA", (828, 1078), (0,0,0,50))
        else:
            background_image = await pill.get_dowload_img(self.background)
            background_image = await pill.get_centr_honkai_art((828,1078),background_image)
            background_shadow = Image.new("RGBA", (828, 1078), (0,0,0,150))
        background_image = background_image.convert("RGBA")
        background_image.alpha_composite(background_shadow)
        self.background_profile.paste(background_image,(0,0),maska.convert("L"))
        self.background_profile.alpha_composite(frame)

    async def creat_charter(self,key):
        
        charter_profile = Image.new("RGBA", (147, 211), (0,0,0,50))
        if not self.img is None:
            if str(key.id) in self.img:
                url_id = self.img[str(key.id)]
        else:
            url_id = key.icon.url
            
        splash,mask = await asyncio.gather(pill.get_dowload_img(url_id),_of.maska_character)
        splash = await pill.get_centr_honkai_art((147,211),splash)
        charter_profile.paste(splash,(0,0),mask.convert("L"))
        
        stars = options.assets.character(key.id)
        stars = await pill.get_stars(stars.rarity)
        name = await pill.create_image_with_text(key.name, 15, max_width=135, color=(255, 255, 255, 255)) 
        
        charter_profile.alpha_composite(stars.resize((85,25)),(31,0))
        charter_profile.alpha_composite(name,(int(74-name.size[0]/2),int(189-name.size[1]/2)))       

        return charter_profile
    
    async def get_charter(self):
        task = []
        for key in self.profile.characters_preview:
            task.append(self.creat_charter(key))
        
        self.charter = await asyncio.gather(*task)
    
    async def creat_avatar(self):
        self.background_profile_avatar = Image.new("RGBA", (625, 319), (0,0,0,0))
        background_avatar = Image.new("RGBA", (168, 168), (0,0,0,0))
        if self.profile.avatar.icon is None:
            avatar = "https://api.ambr.top/assets/UI/UI_AvatarIcon_Paimon.png"
        else:
            avatar = self.profile.avatar.icon.url
            
        avatar,font_20,maska,ab_ac,desc_frame = await asyncio.gather(pill.get_dowload_img(avatar, size= (168,168)),pill.get_font(20),_of.avatar_maska,_of.icons,_of.desc_frame)
        background_avatar.paste(avatar,(0,0),maska.convert("L"))
    
        self.background_profile_avatar.alpha_composite(background_avatar,(19,44))
        self.background_profile_avatar.alpha_composite(ab_ac,(170,183))
        
        d = ImageDraw.Draw(self.background_profile_avatar)
        
        level = f"{self.lang['lvl']}: {self.profile.level}"
        Wlevel = f"{self.lang['WL']}: {self.profile.world_level}"
        if self.hide:
            uid  = 'UID: Hide'
        else:
            uid = f"UID: {self.uid}"
        
        d.text((179,67), self.profile.nickname, font= font_20, fill=(255,255,255,255))
        d.text((179,139), level, font= font_20, fill=(255,255,255,255))
        d.text((179,103), Wlevel, font= font_20, fill=(255,255,255,255))
        d.text((13,0), uid, font= font_20, fill=(255,255,255,255))
        
        d.text((332,193), f"{self.profile.abyss_floor}-{self.profile.abyss_room}", font= font_20, fill=(255,255,255,255))
        d.text((220,193), str(self.profile.achievement), font= font_20, fill=(255,255,255,255))
        
        signature = await pill.create_image_with_text(self.profile.signature, 20, max_width=600, color=(255, 255, 255, 255))
        self.background_profile_avatar.alpha_composite(desc_frame,(0,228))
        self.background_profile_avatar.alpha_composite(signature,(int(320-signature.size[0]/2),250))
        
    
        
    
    async def build(self):
        self.background_profile.alpha_composite(self.background_profile_avatar,(23,19))
        x,y = 15,450  
        for i, key in enumerate(self.charter):
            self.background_profile.alpha_composite(key,(x,y))
            x += 168
            if i == 3:
                x = 15
                y += 237
        logo = await _of.logo
        self.background_profile.alpha_composite(logo,(18,978))
                
    async def start(self):
        
        await asyncio.gather(self.creat_background(), self.get_charter(), self.creat_avatar())
        await self.build()        
        return self.background_profile