from PIL import Image,ImageDraw
from ...utils import pill, git

_of = git.ImageCache()

class Skill:
    def __init__(self, skill,element) -> None:
        self.skill = skill
        self.element_color = pill.element_color_text.get(element, (149,107,5,255))
    
    async def add_icon(self):
        icon = await pill.get_dowload_img(self.skill.icon.url, size= (63,62))
        self.background.alpha_composite(icon,(24,5))
    
    async def add_count(self):
        if self.skill.is_boosted:
            self.count = await pill.recolor_image(self.count,self.element_color[:3])
        
        font_25 = await pill.get_font(25)
        
        d = ImageDraw.Draw(self.count)
        
        x = font_25.getlength(str(self.skill.level))
        d.text((int(22-x/2),6), str(self.skill.level), font= font_25, fill=(255,255,255,255))
    
    async def start(self):
        self.background = await _of.skill_bg
        self.background = self.background.copy()
        self.count = await _of.skill_count
        self.count = self.count.copy()
        
        await self.add_icon()
        await self.add_count()
        
        background = Image.new("RGBA", (82, 81), (0,0,0,0))
        background.alpha_composite(self.background.resize((82,64)))
        background.alpha_composite(self.count,(20,42))

        return background