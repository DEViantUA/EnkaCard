import aiohttp
from ..utils import pill, git
from PIL import ImageDraw,Image

_of = git.ImageCache()

api_url = "https://akasha.cv/api/getCalculationsForUser/{uid}"
api_update = "https://akasha.cv/api/user/refresh/{uid}"

#https://akasha.cv/api/leaderboards/{uid}/{hash}?variant=profilePage - ПОЛУЧИТЬ ХАШ ОБЩИЙ И ДЛЯ ПЕРСОНАЖЕЙ
#https://akasha.cv/api/substatPriority/{uid}/{hash} - ПОЛУЧИТЬ ИНФОРМАЦИЮ О СТАТАХ ПЕРСОНАЖА


data_akasha = {}

class AkashaCreat:
    def __init__(self,card = None,teample= None,rank= None,uid= None) -> None:
        self.card = card
        self.teample = teample
        self.rank = rank
        self.uid = uid
    
    async def get_hash(self, charter_id):
        async with aiohttp.ClientSession() as session:
            async with session.get(api_url.format(uid = self.uid)) as response:
                data = await response.json()
                for key in data["data"]:
                    if str(charter_id) == str(key["characterId"]):
                        return key["md5"]
    
    async def update(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(api_update.format(uid = self.uid)) as response:
                return await response.json()
    
    async def get_info_character(self, id):
        hash = await self.get_hash(id)
        url = f'https://akasha.cv/api/leaderboards/{self.uid}/{hash}?variant=profilePage'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    return data["data"]
                else:
                    return {}
            
    async def get_rank_akasha(self):
        akaska_info = []
        if not self.uid in data_akasha:
            async with aiohttp.ClientSession() as session:
                async with session.get(api_url.format(uid = self.uid)) as response:
                    data = await response.json()
                    for key in data.get("data", []):
                        calculator = key.get("calculations", {}).get("fit", {})
                        if calculator:
                            rank = int(str(calculator.get("ranking", "0")).replace("~", ""))
                            out = int(calculator.get("outOf", "1"))
                            percentage = round((rank / out) * 100)
                            if percentage == 0:
                                percentage = 1
                            akaska_info.append({"id": key["characterId"], "rank": rank, "out": out, "precent": percentage})
                            
                    data_akasha[self.uid] = akaska_info
        return data_akasha[self.uid]
         
    async def creat_logo(self):
        logo = await _of.akasha
        logo = logo.copy()
        
        background = Image.new("RGBA",(264,79) ,(0,0,0,0))
        
        background.alpha_composite(logo)
        
        font = await pill.get_font(12)
        d = ImageDraw.Draw(background)
        d.text((61,55), f'Rank: ~{self.rank.rank}/{self.rank.out}', font = font, fill= (255,255,255,255)) 
        d.text((61,39), f'Top: {self.rank.precent}%', font = font, fill= (255,255,255,255)) 
        
        return background
        
        
    async def start(self):
        if self.rank is None:
            return self.card
        
        logo = await self.creat_logo()

        if self.teample == 1:
            self.card.alpha_composite(logo,(11,409))
        elif self.teample == 2:
            self.card.alpha_composite(logo,(952,13))
        return self.card