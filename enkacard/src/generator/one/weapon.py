from PIL import Image,ImageDraw
from ...utils import pill, git

_of = git.ImageCache()

class Weapon:
    def __init__(self,weapon,lang) -> None:
        self.weapon = weapon
        self.lang = lang
        self.CRIT_DMG = 0
        self.CRIT_RATE = 0
        
    async def add_substat(self):
        for substat in self.weapon.detail.substats:
            icon = await pill.get_icon_add(substat.prop_id, size=(25,25))
            self.background.alpha_composite(icon,(379,86))
            if str(substat.type) == "DigitType.PERCENT":
                val = f"{substat.value}%"
            else:
                val = str(substat.value)

            if substat.prop_id == "FIGHT_PROP_CRITICAL_HURT":
                self.CRIT_DMG += substat.value
            if substat.prop_id == "FIGHT_PROP_CRITICAL":
                self.CRIT_RATE += substat.value
            
            x = self.font_25.getlength(val)
            self.d.text((int(465-x/2),84), val, font= self.font_25, fill=(255,255,255,255))
            
    async def add_weapon_icon(self):
        icon = await pill.get_dowload_img(self.weapon.detail.icon.url, size=((180,180)))
        self.background.alpha_composite(icon,(43,0))
    
    async def add_stars(self):
        icon = await pill.get_stars(self.weapon.detail.rarity, light= True)
        self.background.alpha_composite(icon.resize((186,22)),(0,168))
    
    async def add_name(self):
        name = await pill.create_image_with_text(self.weapon.detail.name, 25, max_width=294, color=(255, 255, 255, 255))
        self.background.alpha_composite(name,(225,int(34-name.size[1]/2)))
    
    async def add_stats(self):
        lvl = f"{self.lang}: {self.weapon.level}/{self.weapon.max_level}"
        lvl_up = f"R{self.weapon.refinement}"
        base_stats = str(self.weapon.detail.mainstats.value)
        
        self.font_25 = await pill.get_font(25)
        
        self.d = ImageDraw.Draw(self.background)
        
        x = self.font_25.getlength(base_stats)
        self.d.text((int(311-x/2),84), base_stats, font= self.font_25, fill=(255,255,255,255))
        x = self.font_25.getlength(lvl_up)
        self.d.text((int(242-x/2),145), lvl_up, font= self.font_25, fill=(255,208,127,255))
        x = self.font_25.getlength(lvl)
        self.d.text((int(388-x/2),145), lvl, font= self.font_25, fill=(255,255,255,255))
    
    async def start(self):
        if self.weapon.detail.artifact_name_set != "":
            return {"tcv": 0, "img": Image.new("RGBA", (537, 161), (0,0,0,0))}
        
        self.background = await _of.weapon
        self.background = self.background.copy()
        
        await self.add_weapon_icon()
        await self.add_stats()
        await self.add_name()
        await self.add_stars()
        await self.add_substat()

        return {"tcv": float('{:.2f}'.format(self.CRIT_DMG + (self.CRIT_RATE*2))), "img": self.background}
        
        