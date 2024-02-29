# Copyright 2023 DEViantUa <t.me/deviant_ua>
# All rights reserved.
from PIL import Image
import threading
from pathlib import Path
import aiohttp
from io import BytesIO
from cachetools import TTLCache
lock = threading.Lock()

_cache = TTLCache(maxsize=1000, ttl=300)

_BASE_URL = 'https://raw.githubusercontent.com/DEViantUA/EnkaCardData/main/assets/'

assets = Path(__file__).parent.parent / 'assets'

font = str(assets / 'font' / 'Genshin_Impact.ttf')
fontKH = str(assets / 'font' / 'GSEnochian.ttf')

async def change_Font(x):
    global font
    if x == 0:
        font = str(assets / 'font' / 'Genshin_Impact.ttf')
    else:
        font = str(assets / 'font' / 'GSEnochian.ttf')
mapping = {
    "artifact_bg": "one/artifact_bg.png",
    "artifact_bg_none": "one/artifact_bg_none.png",
    "shadow_one": "one/shadow.png",
    "mask_artifact": "one/mask_artifact.png",
    "artifact_up": "one/artifact_up.png",
    "maska_art": "one/maska_art.png",
    "overlay": "one/overlay.png",
    "overlay_dark": "one/overlay_dark.png",
    "sets": "one/sets.png",
    "stats": "one/stats.png",
    "tcv": "one/tcv.png",
    "weapon": "one/weapon.png",
    "closed_const": "total/constant/closed/CLOSED.png",
    "icon_stats": "stats_icon/{prop_id}.png",
    "icon_const_unlock": "total/constant/open/{element}.png",
    "icon_const_lock": "total/constant/closed/{element}.png",
    
    "star1": "total/stars/Star1.png",
    "star2": "total/stars/Star2.png",
    "star3": "total/stars/Star3.png",
    "star4": "total/stars/Star4.png",
    "star5": "total/stars/Star5.png",
    
    "l_star5": "total/stars/5_stars_light.png",
    "l_star4": "total/stars/4_stars_light.png",
    "l_star3": "total/stars/3_stars_light.png",
    "l_star2": "total/stars/2_stars_light.png",
    "l_star1": "total/stars/1_stars_light.png",
    "logo": "total/logo.png",
    "akasha": "total/akasha_logo.png",
    
    "skill_bg": "total/talants/bg.png",
    "skill_count": "total/talants/CoontLow.png",
    
    
    "ab_ac": "profile/ab_ac.png",
    "art_profile_mask": "profile/art_profile_mask.png",
    "avatar_mask": "profile/avatar_mask.png",
    "overlay_profile": "profile/overlay.png",
    "profile_bg_mask": "profile/profile_bg_mask.png",
    "shadow_art_profile": "profile/shadow_art_profile.png",
    
    
    "artifact_set_count": "two/artifact_set_count.png",
    "maska_bg": "two/maska_bg.png",
    "overlay_bg": "two/overlay_l_bg.png",
    "total_mask_bg": "two/total_mask_bg.png",
    "artifact_mask": "two/artifact_mask.png",
    "line_bg": "two/line_bg.png",
    "artifact_eff": "two/artifact_eff.png",
    
    "snow_texture": "two/snow_texture.png",
    "snow": "two/snow.png",
    
    
    "avatar_maska": "profile_two/avatar_maska.png",
    "bg_1": "profile_two/bg_1.png",
    "bg_2": "profile_two/bg_2.png",
    "bg_3": "profile_two/bg_3.png",
    "desc_frame": "profile_two/desc_frame.png",
    "frame_profile": "profile_two/frame_profile.png",
    "icons": "profile_two/icons.png",
    "maska_character": "profile_two/maska_character.png",
    "maska_prof_bg": "profile_two/maska_prof_bg.png"
}

class ImageCache:
    @classmethod
    async def download_image(cls, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                try:
                    image = await response.read()
                finally:
                    await session.close()
                    
        return BytesIO(image)

    @classmethod
    async def _load_image(cls, name):
        url = _BASE_URL + name
        if url in _cache:
            return _cache[url]
        else:
            image_data = await cls.download_image(url)
            image = Image.open(image_data)
            _cache[url] = image
        return image

    async def __getattr__(self, name):
        if name in mapping:
            return await self._load_image(mapping[name])
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
        
    async def download_icon_stats(self, prop_id):
        if 'icon_stats' in mapping:
            url = mapping['icon_stats'].format(prop_id=prop_id)
            full_url = _BASE_URL + url
            if full_url in _cache:
                return _cache[full_url].copy()
            else:
                image_data = await self.download_image(full_url)
                image = Image.open(image_data)
                _cache[full_url] = image
                return image.copy()
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute 'icon_stats'")

    async def download_icon_constant(self, element, unlock, resizes = None):
        if 'icon_const_unlock' in mapping and "icon_const_lock" in mapping:
            if unlock:
                url = mapping['icon_const_unlock'].format(element=element.upper())
            else:
                url = mapping['icon_const_lock'].format(element=element.upper())
            full_url = _BASE_URL + url
            key = (full_url, resizes, unlock)
            if key in _cache:
                return _cache[key].copy()
            else:
                image_data = await self.download_image(full_url)
                image = Image.open(image_data)
                if not resizes is None:
                    image = image.resize(resizes)
                    
                _cache[full_url] = image
                return image.copy()
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute 'icon_stats'")