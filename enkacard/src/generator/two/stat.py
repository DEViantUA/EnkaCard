from PIL import Image,ImageDraw
from ...utils import pill, git, options
import asyncio
import json
import math
_of = git.ImageCache()


class Stat:
    def __init__(self,stats,element) -> None:
        self.stats = stats
        self.element_color = pill.element_color_text.get(element, (149,107,5,255))
        self.line = Image.new("RGBA", (26, 1), (255,255,255,255))
    
    
    async def get_substats(self):
        self.dop_value = {}
        stats_json = json.loads(self.stats.json())
        for key in stats_json:
            if key in options.dopStatAtribute:
                name_dop_value = options.dopStatAtribute.get(key)
                self.dop_value[key] = {"value": math.ceil(stats_json.get(name_dop_value)["value"])}
    
    async def creat_stats(self):
        task = []
        elementUp = True        
        for key in self.stats:
            if key[1].id in [40,41,42,43,44,45,46]:
                if elementUp:
                    key = max((x for x in self.stats if 40 <= x[1].id <= 46), key=lambda x: x[1].value)
                    elementUp = False
                else:
                    continue
            if key[1].value != 0 and key[0] in options.IconAddTrue:
                task.append(self.creat_line_stats(key))
            
        result = await asyncio.gather(*task)
        self.sorted_data = sorted(result, key=lambda x: x['id'] not in [2000, 2001, 2002])
    
    async def creat_line_stats(self,stats):
        background = Image.new("RGBA", (519, 47), (0,0,0,0))
        dop_value = 0
        name = options.assets.get_hash_map(stats[0])
        icon,name = await asyncio.gather(pill.get_icon_add(stats[0].replace("_CUR","").replace("_MAX", ""), size=(45,45)), pill.create_image_with_text(name, 18, max_width=155,  color=(255, 255, 255, 255)))
        try:
            value = stats[1].to_percentage_symbol()
        except:
            value = stats[1].to_rounded()
        if stats[0] in self.dop_value:
            dop_value = self.dop_value.get(stats[0], 0)
            up_valur = str(int(value - dop_value["value"]))
            
        
        background.alpha_composite(icon,(0,1))
        background.alpha_composite(name,(63,int(25-name.size[1]/2)))
        
        d = ImageDraw.Draw(background)
        xs = self.font_29.getlength(str(value))
        d.text((int(519-xs),0), str(value), font= self.font_29, fill=(255,255,255,255))
        if dop_value != 0:
            x = self.font_12.getlength(f"+{dop_value['value']}")
            d.text((int(519-x),30), f"+{dop_value['value']}", font= self.font_12, fill= self.element_color)
            xx = self.font_12.getlength(up_valur)
            d.text((int(519-x-xx-5),30), up_valur, font= self.font_12, fill=(255,255,255,255))
        
        size_x_line = int(519-name.size[0]-xs - 60-40)
        line = Image.new("RGBA", (size_x_line, 1), (255,255,255,50))
        background.alpha_composite(line, (63+name.size[0] + 20,22))
                
        return {"icon": background,"id": stats[1].id}
                            
    async def start(self):
        self.font_29,self.font_12 = await asyncio.gather(pill.get_font(29),pill.get_font(12))
        await self.get_substats()
        await self.creat_stats()
        
        return self.sorted_data