from PIL import Image,ImageDraw
from ...utils import pill, git, options
import asyncio
import json
import math
_of = git.ImageCache()


class Stat:
    def __init__(self,stats,props,element) -> None:
        self.stats = stats
        self.props = props
        self.element_color = pill.element_color_text.get(element, (149,107,5,255))
        self.line = Image.new("RGBA", (26, 1), (255,255,255,255))
        
    async def creat_prop_icon(self,prop_id):
        background = Image.new("RGBA", (100, 26), (0,0,0,0))

        d = ImageDraw.Draw(background)
        
        icon = await pill.get_icon_add(prop_id, size=(21,20))
        
        main = str(self.new_items[prop_id]["main"])
        sub = str(float('{:.1f}'.format(self.new_items[prop_id]["sub"])))
        if self.new_items[prop_id]["value"] % 1 == 0:
            value = str(self.new_items[prop_id]["value"])
        else:
            value = str('{:.1f}%'.format(self.new_items[prop_id]["value"]))
        x = self.font_13.getlength(main)
        d.text((int(14-x/2),12), main, font= self.font_13, fill=(255,255,255,255))
        
        x = self.font_13.getlength(sub)
        d.text((int(14-x/2),-2), sub, font= self.font_13, fill=(255,255,255,255))
        
        d.text((55,4), value, font= self.font_13, fill=(255,255,255,255))
        
        background.alpha_composite(self.line,(0,13))
        background.alpha_composite(icon,(31,2))
        x = self.font_13.getlength(value)
        background = background.crop((0, 0, 55 + x, 26))
                
        return background
            
            
    async def sort_prop_id(self):
        self.new_items = {}
        for item in self.props:
            for prop_key in item:
                if not prop_key in self.new_items :
                    self.new_items [prop_key] = {"main": item[prop_key]["main"], "sub": item[prop_key]["sub"], "value": item[prop_key]["value"]}
                else:
                    self.new_items [prop_key]['main'] += item[prop_key]['main']
                    self.new_items [prop_key]['sub'] += item[prop_key]['sub']
                    self.new_items [prop_key]['value'] += item[prop_key]['value']
                    
        task = []
        for key in self.new_items:
            task.append(self.creat_prop_icon(key))
        result = await asyncio.gather(*task)
        x = 16
        for prop_icon in result[:9]:
            self.background.alpha_composite(prop_icon, (x,12))
            x += prop_icon.size[0]+10

    async def creat_line_stats(self,stats):
        background = Image.new("RGBA", (411, 50), (0,0,0,0))
        dop_value = 0
        name = options.assets.get_hash_map(stats[0])
        icon,name = await asyncio.gather(pill.get_icon_add(stats[0].replace("_CUR","").replace("_MAX", ""), size=(37,37)), pill.create_image_with_text(name, 21, max_width=215,  color=(255, 255, 255, 255)))
        try:
            value = stats[1].to_percentage_symbol()
        except:
            value = stats[1].to_rounded()
        if stats[0] in self.dop_value:
            dop_value = self.dop_value.get(stats[0], 0)
            up_valur = str(int(value - dop_value["value"]))
            
        
        background.alpha_composite(icon,(0,6))
        background.alpha_composite(name,(49,int(27-name.size[1]/2)))
        
        d = ImageDraw.Draw(background)
        x = self.font_21.getlength(str(value))
        d.text((int(406-x),8), str(value), font= self.font_21, fill=(255,255,255,255))
        if dop_value != 0:
            x = self.font_13.getlength(f"+{dop_value['value']}")
            d.text((int(406-x),32), f"+{dop_value['value']}", font= self.font_13, fill= self.element_color)
            xx = self.font_13.getlength(up_valur)
            d.text((int(406-x-xx-5),32), up_valur, font= self.font_13, fill=(255,255,255,255))

        return {"icon": background,"id": stats[1].id}
            
    async def get_substats(self):
        self.dop_value = {}
        stats_json = json.loads(self.stats.json())
        for key in stats_json:
            if key in options.dopStatAtribute:
                name_dop_value = options.dopStatAtribute.get(key)
                self.dop_value[key] = {"value": math.ceil(stats_json.get(name_dop_value)["value"])}
    
    
    async def add_stats(self):
        x = 22
        y = 68
        for i, key in enumerate(self.sorted_data):
            self.background.alpha_composite(key["icon"],(x,y))
            y += 60
            if i == 4:
                x = 483
                y = 68
                
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
        
        
        
    async def start(self):
        self.font_13, self.font_21, _, self.background = await asyncio.gather(pill.get_font(13),pill.get_font(21),self.get_substats(),_of.stats)
        self.background = self.background.copy()
        
        await self.sort_prop_id()
        await self.creat_stats()
        await self.add_stats()
        
        return self.background
    
        