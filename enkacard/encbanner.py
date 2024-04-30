import asyncio
import aiofiles
import io
from PIL import Image
from enkanetwork import EnkaNetworkAPI
import os
import datetime
from .src.utils.options import get_charter_id, get_info_enka,get_character_art,get_uid,set_assets,check_settings, get_setting_art
from .src.utils.git import change_Font
from .src.utils.pickle_cashe import PickleCache
from .src.utils.translation import translationLang, supportLang
from .src.modal import enkacardCread
from .enc_error import ENCardError
from .src.generator import teample_one, akasha_rank, profile_teample_one, teample_two,profile_teample_two

async def update():
    async with EnkaNetworkAPI(user_agent= "ENC Library: 3.0.0") as ena:
        await ena.update_assets()

async def save_card(uid, image_data, name):
    data = datetime.datetime.now().strftime("%d_%m_%Y %H_%M")
    path = os.getcwd()
    
    try:
        os.makedirs(f'{path}/EnkaCardImg/{uid}', exist_ok=True)
    except FileExistsError:
        pass
    
    file_name = f"{path}/EnkaCardImg/{uid}/{name}_{data}.png"
    
    async with aiofiles.open(file_name, 'wb') as file:
        if isinstance(image_data, Image.Image):
            img_bytes = io.BytesIO()
            image_data.save(img_bytes, format='PNG')
            await file.write(img_bytes.getvalue())


async def set_lang(lang):
    if lang != "kh":
        typelang = 0
        await set_assets(lang)
        lang = lang
        translateLang = translationLang[lang]
        await change_Font(0)
    else:
        typelang = 1
        await set_assets("en")
        lang = "en"
        translateLang = translationLang[lang]
        await change_Font(1)
    
    return typelang,lang,translateLang

class Akasha:
    def __init__(self, uid) -> None:
        self.uid = uid
    
    async def get_stats(self, chart_id = None):
        rank = await akasha_rank.AkashaCreat([],0,0,self.uid).get_rank_akasha()
        if not chart_id is None:
            for key in rank:
                if key['id'] == chart_id:
                    return enkacardCread.AkashaRank(akasha = [key])
            return None
        
        return enkacardCread.AkashaRank(akasha = rank)
    
    async def refresh(self, prints = True):
        result = await akasha_rank.AkashaCreat([],0,0,self.uid).update()
        if prints:
            print(result["data"]["message"])
    
    async def start(self, card, teample):
        rank = await self.get_stats(card["id"])
        if not rank is None:
            card["card"] = await akasha_rank.AkashaCreat(card["card"],teample,rank.akasha[0],self.uid).start()
        
        return card  

class ENC:
    def __init__(self,lang = "en", uid = None, character_art = None,
            character_id = None, hide_uid = False, save = False, pickle = None, agent = "Library: 3.3.7",
            setting_art = None):
        
        self.character_ids = []
        self.character_name = []
        self.USER_AGENT = f"ENC {agent}"
        self.lang  = lang
        self.save = save
        self.img = None

        self.print_size = None
        
        self.pickle = pickle
        self.hide_uid = hide_uid
        self.character_id = character_id
        self.uid = uid
        self.character_art = character_art
        self.setting_art = setting_art
        
        self.pickle_class = PickleCache(self.uid)
        
    async def __aenter__(self):
        self.uid = await get_uid(self.uid)
        
        if self.uid is None:
            raise ENCardError(5,"The UIDS parameter must be a number or a string. To pass multiple UIDs, separate them with commas.\nExample: uids = 55363")
        if self.lang in supportLang:
            self.typelang,self.lang,self.translateLang = await set_lang(self.lang)
        else:
            self.lang = "en"
        
        self.enc = await get_info_enka(self.uid,self.USER_AGENT,self.lang)

        if self.enc is None:
            raise ENCardError(1001, "Enable display of the showcase in the game or add characters there")
        
        if self.character_id:
            self.character_id = await get_charter_id(self.character_id)
        
        if self.setting_art:
            if not isinstance(self.setting_art, dict):
                raise ENCardError(4,"The setting_art parameter must be a dictionary, where the key is the name of the character, and the parameter is an percentage from 0.1 to 1.\nExample: setting_art = {'1235': 1.0, '1235': 0.3}")
            else:
                self.setting_art = await get_setting_art(self.setting_art)
        
        if self.character_art:
            if not isinstance(self.character_art, dict):
                raise ENCardError(4,"The character_art parameter must be a dictionary, where the key is the name of the character, and the parameter is an image.\nExample: character_art = {'1235': 'img.png', '1235': ['img.png','http.../img2.png']} or {'123596': 'img.png', '123854': 'http.../img2.png', ...}")
            else:
                self.character_art = await get_character_art(self.character_art)
        
        if not self.pickle is None:
            if type(self.pickle) != dict:
                 raise ENCardError(80, "Pickle argument must be in dict format")

            self.pickle = await check_settings(self.pickle)
            
            self.enc.characters = await self.pickle_class.setting_charters(self.pickle,self.enc.characters)
            
            if self.pickle["size"]:
                self.print_size = await self.pickle_class.size_pickle()
        else:
            self.pickle = await check_settings({})
                
        return self

    async def __aexit__(self, *args):
        pass
       
    def sorting(self,result):
        enc_card = {"info": {
            "uid": self.uid,
            "lang": self.lang,
            "save": self.save
            },
            "card": result, 
            "character_id": self.character_ids,
            "character_name": self.character_name,
            "pickle_size": self.print_size
        }
                
        return enkacardCread.EnkaCard(**enc_card)
    
    async def creat(self, template = 1, akasha = False, snow = False):
        template = int(template)
        task = []
        task_save = []
        
        generator = []
        gen_tools = []
        
        if self.pickle["get_generate"]:
            generator = await self.pickle_class.get_generator(template)
                        
        if not template in [1,2]:
            template = 1
                
        for key in self.enc.characters:
            self.character_ids.append(key.id)
            self.character_name.append(key.name)

            if self.character_id:
                if not str(key.id) in self.character_id:
                    continue  
                                     
            if key.id in generator:
                if not generator.get(key.id,None) is None:
                    gen_tools.append(generator.get(key.id))
                continue
            if str(key.id) == "10000092":
                key.image.banner.url = "https://api.ambr.top/assets/UI/UI_Gacha_AvatarImg_Gaming.png"
            elif str(key.id) == "10000093":
                key.image.banner.url = "https://api.ambr.top/assets/UI/UI_Gacha_AvatarImg_Liuyun.png"
                
            art = None
            setting = 0
            
            if self.character_art:
                if str(key.id) in self.character_art:
                    art = self.character_art[str(key.id)]
            
            if self.setting_art:
                if str(key.id) in self.setting_art:
                    setting = self.setting_art[str(key.id)]
            
            if not self.character_id is None:
                if not str(key.id) in self.character_id:
                    continue
            
            if template == 1:
                task.append(teample_one.Creat(key,self.translateLang,art,self.hide_uid,self.uid,self.enc.player.nickname).start())
            else:
                task.append(teample_two.Creat(key,self.translateLang,art,self.hide_uid,self.uid,self.enc.player.nickname, setting).start(snow))
                
        
        
        result = await asyncio.gather(*task)
        
        if not self.pickle is None:
            if self.pickle["add_generate"] and  result != []:
                await self.pickle_class.add_generator(template,result)
        
        if gen_tools != []:
            result = result + gen_tools

        if akasha:
            akasha_result = []
            for key in result:
                akasha_result.append(Akasha(self.uid).start(key, template))
            result = await asyncio.gather(*akasha_result)
        
        if self.save:
            for key in result:
                task_save.append(save_card(self.uid,key["card"],key["id"]))
        
            await asyncio.gather(*task_save)
        
        return self.sorting(result)

    async def profile(self,teamplate = 1, card = False,background = None):
        
        for key in self.enc.characters:
            self.character_ids.append(key.id)
            self.character_name.append(key.name)
            
        data = {
            "player":{
                "name":self.enc.player.nickname,
                "uid": self.uid,
                "lang": self.lang,
                "achievement": self.enc.player.achievement,
                "level": self.enc.player.level,
                "world_level": self.enc.player.world_level,
                "abyss": f"{self.enc.player.abyss_floor}-{self.enc.player.abyss_room}",
                "avatar": None,
            },
            "characters":{
                "count": len(self.enc.characters),
                "character_name": self.character_name,
                "character_id": self.character_ids,
            },
            "card": None
        }
        
        if self.enc.player.avatar.icon is None:
            data["player"]["avatar"] = "https://api.ambr.top/assets/UI/UI_AvatarIcon_Paimon.png"
        else:
            data["player"]["avatar"] = self.enc.player.avatar.icon.url

        if card:
            if int(teamplate) == 1:
                data["card"] = await profile_teample_one.ProfileCard(self.enc.player,self.translateLang,self.character_art,self.hide_uid,self.uid,background).start()
            elif int(teamplate) == 2:
                data["card"] = await profile_teample_two.ProfileCard(self.enc.player,self.translateLang,self.character_art,self.hide_uid,self.uid,background).start()
            if self.save:
                await save_card(self.uid, data["card"], "profile")
        
        return enkacardCread.Profile(**data)

