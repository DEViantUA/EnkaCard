import asyncio
from PIL import ImageDraw,Image,ImageChops
from ..utils import pill, git,diagram,options
from enkanetwork.enum import EquipmentsType
from .two import background, artifact, stat, skill
from .one import weapon,constant
from .akasha_rank import AkashaCreat
import random
_of = git.ImageCache()







class Creat:
    def __init__(self,characters,lang,img,hide,uid,name) -> None:
        self.character = characters
        self.lang = lang["lvl"]
        self.img = img
        self.hide = hide
        self.uid = uid
        self.name = name
        self.tcv = 0
        
    async def collect_background(self):
        if self.img:
            self.background =  await background.Background(self.img, None).start()
        else:
            self.background = await background.Background(self.character.image.banner.url,self.character.element.value).start()
        
    async def collect_weapon(self):
        self.weapon = await weapon.Weapon(self.character.equipments[-1], self.lang).start()
        self.weapon = self.weapon["img"].resize((351,129))

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
        self.background_constant = self.background_constant.resize((54,342))
        
    async def collect_artifact(self):
        task_art = []
        y = 0
        
        ids_next = {"4": None,"2": None,"5": None,"1": None,"3": None}
        self.artifact_background = Image.new("RGBA", (457, 655), (0,0,0,0))
        
        for key in filter(lambda x: x.type == EquipmentsType.ARTIFACT, self.character.equipments):
            ids = key.detail.icon.filename[-1:]
            ids_next[ids] = key
        
        for key in ids_next:
            task_art.append(artifact.Artifact(ids_next[key],self.character.element.value).start())
        
        results = await asyncio.gather(*task_art)
        
        for key in results:
            self.artifact_background.alpha_composite(key["img"],(0,y))
            y += 133
            self.tcv += key["tcv"]
        
    async def collect_sets(self):
        self.artifact_sets = await artifact.ArtifactSets(self.character.equipments,self.character.element.value).start()
    
    async def creat_name(self):
        self.background_name = Image.new("RGBA", (350, 75), (0,0,0,0))
        name = self.character.name
        level = f"{self.lang}: {self.character.level}/{self.character.max_level}"
        stars = await pill.get_stars(self.character.rarity)
        friends = str(self.character.friendship_level)
        font_23 = await pill.get_font(23)
        font_15 = await pill.get_font(15)
        d = ImageDraw.Draw(self.background_name)
        x = font_23.getlength(name)
        d.text((int(349-x),0), name, font= font_23, fill=(255,255,255,255))
        
        x = font_15.getlength(level)
        d.text((int(349-x),31), level, font= font_15, fill=(255,255,255,255))
        
        friends_icon = await pill.get_icon_add("FRIENDS", size=(21,21))
        self.background_name.alpha_composite(stars.resize((101,29)),(202,46))
        self.background_name.alpha_composite(friends_icon,(328,50))
        x = font_15.getlength(friends)
        d.text((int(324-x),51), friends, font= font_15, fill=(255,255,255,255))
       
    async def add_logo(self):
        logo = await _of.logo
        self.background.alpha_composite(logo, (1108,710))
    
    async def creat_diagram(self):
        elementUp = True
        akashaElement = False
        data_user = []
        
        dataAkasha = await AkashaCreat(uid = self.uid).get_info_character(self.character.id)
        if dataAkasha == []:
            dataAkasha = {}
        if dataAkasha != {}:
            dataAkasha  = dataAkasha[random.choice(list(dataAkasha.keys()))]['stats']
        dataAkasha_new = []
        
        for key in self.character.stats:
            if key[1].id in [40,41,42,43,44,45,46]:
                if elementUp:
                    key = max((x for x in self.character.stats if 40 <= x[1].id <= 46), key=lambda x: x[1].value)
                    elementUp = False
                    akashaElement = True
                else:
                    continue
            if key[1].value != 0 and key[0] in options.IconAddTrue:
                akasha_name = options.AkashaStats.get(key[0], None)
                if not akasha_name is None or akashaElement:
                    if akashaElement:
                        for keys in dataAkasha:
                            if "DMG" in keys and not "_CRITICAL" in keys:
                                akasha_name = keys
                                akashaElement = False
                                    
                    name = options.assets.get_hash_map(key[0])
                    
                    if "." in name:
                        name = name.replace(".",".\n")
                    else:
                        name = name.replace(" ","\n")
                    
                    try:
                        value = key[1].to_percentage()
                        procent = True
                    except:
                        value = key[1].to_rounded()
                        procent = False
                        
                    if dataAkasha != {}:
                        if procent:
                            dataAkasha_new.append({"name": name, "value": float('{:.2f}'.format(dataAkasha[akasha_name]))})
                        else:
                            dataAkasha_new.append({"name": name, "value": round(dataAkasha[akasha_name])})

                    data_user.append({"name": name, "value": value})
        
        if dataAkasha == {}:
            dataAkasha_new = [{'name': entry['name'], 'value': entry['value']} for entry in data_user]  
        
        self.diagram = await diagram.create_normalized_radial_chart(data_user,dataAkasha_new,self.character.element.value)

    async def creat_stat(self):
        self.stat_background = Image.new("RGBA", (519, 601), (0,0,0,0))
        result = await stat.Stat(self.character.stats, self.character.element.value).start()
        if len(result) <= 1:
            x = 0 
        x = int(519 / (len(result) - 1))
        position_line = 0
        for key in result:
            self.stat_background.alpha_composite(key["icon"], (0, position_line))
            position_line += x
    
    async def creat_skill(self): 
        task = []
        self.background_skill = Image.new("RGBA", (288, 81), (0,0,0,0))
        for key in self.character.skills:
            task.append(skill.Skill(key,self.character.element.value).start())
        
        result = await asyncio.gather(*task)
        
        x = 0
        for key in result:
            self.background_skill.alpha_composite(key,(x,0))
            x += 103
    
    async def add_tcr(self):
        background_tcv = await _of.tcv
        background_tcv = background_tcv.copy()
        font_23 = await pill.get_font(23)
        d = ImageDraw.Draw(background_tcv)
        self.tcv = float('{:.2f}'.format(self.tcv))
        x = font_23.getlength(f"{self.tcv}TCV")
        d.text((int(76-x/2),4), f"{self.tcv}TCV", font= font_23, fill=(255,255,255,255))
        
        self.background.alpha_composite(background_tcv.resize((99,23)),(1324,106))
    
    async def creat_name_user(self):
        self.background_name_user = Image.new("RGBA", (128, 32), (0,0,0,0))
        font_13 = await pill.get_font(13)
        d = ImageDraw.Draw(self.background_name_user)
        d.text((0,0), self.name, font= font_13, fill=(255,255,255,150))
        if self.hide:
            d.text((0,18), "UID: Hide", font= font_13, fill=(255,255,255,150))
        else:
            d.text((0,18), f"UID: {self.uid}", font= font_13, fill=(255,255,255,150))
    
    async def build(self):
        self.background.alpha_composite(self.weapon,(518,7))
        self.background.alpha_composite(self.background_constant,(1449,30))
        self.background.alpha_composite(self.artifact_background,(37,22))
        self.background.alpha_composite(self.artifact_sets,(32,696))
        self.background.alpha_composite(self.background_name,(1073,22))
        self.background.alpha_composite(self.diagram.resize((556,413)),(962 ,262))
        self.background.alpha_composite(self.stat_background,(519,155))
        self.background.alpha_composite(self.background_skill,(1096,155))
        self.background.alpha_composite(self.background_name_user,(1793,769))
        
        await self.add_tcr()
        await self.add_logo()
    
    async def start(self,snow):
        await asyncio.gather(self.collect_background(),self.collect_weapon(),self.collect_constant(),self.collect_artifact(),self.collect_sets(),self.creat_name(),
                             self.creat_name_user(),self.creat_diagram(),self.creat_stat(),self.creat_skill())
        
        await self.build()
        
        if snow:
            snow = await _of.snow
            snow_texture = await _of.snow_texture
            self.background = ImageChops.soft_light(self.background , snow_texture.convert("RGBA"))
        
        return {
            "id": self.character.id,
            "name": self.character.name,
            "element": self.character.element.value,
            "rarity": self.character.rarity,
            "card": self.background
        }