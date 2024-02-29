import asyncio
from PIL import ImageDraw,Image,ImageChops
from ..utils import pill, git, options
_of = git.ImageCache()

url_banner = "https://api.ambr.top/assets/UI/namecard/{id}.png"
url_splash = "https://enka.network/ui/{id}.png"

class ProfileCard:
    def __init__(self,profile,lang,img,hide,uid,background) -> None:
        self.profile = profile
        self.lang = lang
        self.img = img
        self.hide = hide
        self.uid = uid
        self.background = background
    
    async def get_background(self):
        position = (0,-63)
        if not self.background is None:
            banner = await pill.get_dowload_img(self.background)
            banner = await pill.get_centr_honkai_art((757,298),banner)
            position = (0,0)
        else:
            banner = url_banner.format(id = self.profile.namecard.banner.filename)
            banner = await pill.get_dowload_img(banner, size= (757,361))
        
        color = await pill.get_background_colors(banner, 15, common=True, radius=5, quality=800)
        
        background = Image.new("RGBA", (757, 717), color)
        background_banner = Image.new("RGBA", (757, 717), (0,0,0,0))
        background_banner.alpha_composite(banner,position)
        profile_bg_mask,overlay = await asyncio.gather(_of.profile_bg_mask,_of.overlay_profile)
        background.paste(background_banner,(0,0), profile_bg_mask.convert("L"))
        
        background = ImageChops.screen(background, overlay.convert("RGBA"))
        background_shadow = Image.new("RGBA", (757, 717), (0,0,0,150))
        background.alpha_composite(background_shadow)
        
        return background
        
    
    async def creat_avatar_info(self):
        background = Image.new("RGBA", (757, 156), (0,0,0,0))
        background_avatar = Image.new("RGBA", (120, 120), (0,0,0,0))
        if self.profile.avatar.icon is None:
            avatar = "https://api.ambr.top/assets/UI/UI_AvatarIcon_Paimon.png"
        else:
            avatar = self.profile.avatar.icon.url
        maska,ab_ac = await asyncio.gather(_of.avatar_mask, _of.ab_ac)
        avatar = await pill.get_dowload_img(avatar, size= (120,120))
        background_avatar.paste(avatar,(0,0),maska.convert("L"))
        background.alpha_composite(background_avatar,(320,7))
        background.alpha_composite(ab_ac,(274,23))
        
        font_15 = await pill.get_font(15)
        
        d = ImageDraw.Draw(background)
        
        level = f"{self.lang['lvl']}: {self.profile.level}"
        Wlevel = f"{self.lang['WL']}: {self.profile.world_level}"
        if self.hide:
            uid  = 'UID: Hide'
        else:
            uid = f"UID: {self.uid}"
        
        d.text((447,20), self.profile.nickname, font= font_15, fill=(255,255,255,255))
        d.text((447,44), level, font= font_15, fill=(255,255,255,255))
        d.text((447,68), Wlevel, font= font_15, fill=(255,255,255,255))
        d.text((447,92), uid, font= font_15, fill=(255,255,255,255))
        
        x = font_15.getlength(f"{self.profile.abyss_floor}-{self.profile.abyss_room}")
        d.text((int(268-x),88), f"{self.profile.abyss_floor}-{self.profile.abyss_room}", font= font_15, fill=(255,255,255,255))
        x = font_15.getlength(str(self.profile.achievement))
        d.text((int(268-x),35), str(self.profile.achievement), font= font_15, fill=(255,255,255,255))
        
        signature = await pill.create_image_with_text(self.profile.signature, 15, max_width=744, color=(255, 255, 255, 255))
        background.alpha_composite(signature,(int(380-signature.size[0]/2),135))
        
        return background
    
    async def creat_charter(self,key):
        background = Image.new("RGBA", (180, 263), (0,0,0,0))
        if self.img is None:
            self.img = {}
        if str(key.id) in self.img:
            url = self.img[str(key.id)]
        else:
            if "Costume" in key.icon.filename:
                url_id = key.icon.filename.replace("UI_AvatarIcon","UI_Costume")
            else:
                url_id = key.icon.filename.replace("UI_AvatarIcon","UI_Gacha_AvatarImg")
            url = url_splash.format(id = url_id)
        splash,mask,shadow = await asyncio.gather(pill.get_dowload_img(url),_of.art_profile_mask,_of.shadow_art_profile)
        splash = await pill.get_centr_honkai_art((180,263),splash)
        background.paste(splash,(0,0),mask.convert("L"))
        background.alpha_composite(shadow)
        stars = options.assets.character(key.id)
        stars = await pill.get_stars(stars.rarity)
        background.alpha_composite(stars.resize((58,17)),(25,235))
        
        name = await pill.create_image_with_text(key.name, 15, max_width=112, color=(0, 0, 0, 255))
        background.alpha_composite(name,(29,int(219-name.size[1])))
        name = await pill.recolor_image(name,(255,255,255))
        background.alpha_composite(name,(30,int(219-name.size[1])))
        
        
        font_15 = await pill.get_font(15)
        
        d = ImageDraw.Draw(background)
        
        level = f"{self.lang['lvl']}: {key.level}"
        d.text((29,219), level, font= font_15, fill=(0,0,0,255))
        d.text((30,219), level, font= font_15, fill=(255,255,255,255))
        
        return background
     
    async def build(self):
        self.background.alpha_composite(self.avatar,(0,10))
        x,y = 9,170
        i = 0
        for key in self.charter:
            self.background.alpha_composite(key,(x,y))
            x += 185
            i += 1
            if i == 4:
                x = 9
                y += 277
    
    async def start(self):
        
        self.background,self.avatar = await asyncio.gather(self.get_background(),self.creat_avatar_info())
               
        task = []
        for key in self.profile.characters_preview:
            task.append(self.creat_charter(key))
        
        self.charter = await asyncio.gather(*task)
        await self.build()
        
        return self.background