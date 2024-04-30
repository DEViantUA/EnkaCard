# Copyright 2023 DEViantUa <t.me/deviant_ua>
# All rights reserved.
from enkanetwork import EnkaNetworkAPI, Assets
import random, aiohttp, json
from . import affixes
import math

assets = Assets(lang="en")

async def fetch_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                text_data = await response.text()
                json_data = json.loads(text_data)
                return json_data
            else:
                print(f"Error: {response.status}")
                return None

data_prop_json = affixes.data_prop_json
    
async def data_prop():
    global data_prop_json
    if data_prop_json is None:
        url = "https://raw.githubusercontent.com/EnkaNetwork/API-docs/master/store/affixes.json"
        data_prop_json = await fetch_json(url)
        
        return data_prop_json
    else:
        data_prop_json = None
        return None


AkashaStats = {
    "FIGHT_PROP_CRITICAL": "critRate",
    "FIGHT_PROP_CRITICAL_HURT": "critDMG",
    "FIGHT_PROP_CHARGE_EFFICIENCY": "energyRecharge",
    "FIGHT_PROP_ELEMENT_MASTERY":"elementalMastery",
    "FIGHT_PROP_MAX_HP": "maxHP",
    "FIGHT_PROP_CUR_ATTACK":"maxDEF",
    "FIGHT_PROP_CUR_DEFENSE":"maxATK"
}


_mapProcent = {
    "maxHp": False,
    "atk": False,
    "def": False,
    "energyRecharge": True,
    "healingBonus": True,
    "critRate": True,
    "critDamage": True,
    "elementalMastery": False,
    "pyroDamageBonus": True,
    "hydroDamageBonus": True,
    "cryoDamageBonus": True,
    "dendroDamageBonus": True,
    "electroDamageBonus": True,
    "anemoDamageBonus": True,
    "geoDamageBonus": True,
    "physicalDamageBonus": True,
}

_mapHash = {
    "maxHp": "FIGHT_PROP_HP",
    "atk": "FIGHT_PROP_ATTACK",
    "def": "FIGHT_PROP_DEFENSE",
    "energyRecharge": "FIGHT_PROP_CHARGE_EFFICIENCY",
    "healingBonus": "FIGHT_PROP_HEAL_ADD",
    "critRate": "FIGHT_PROP_CRITICAL",
    "critDamage": "FIGHT_PROP_CRITICAL_HURT",
    "elementalMastery":"FIGHT_PROP_ELEMENT_MASTERY",
    "pyroDamageBonus": "FIGHT_PROP_FIRE_ADD_HURT",
    "hydroDamageBonus": "FIGHT_PROP_WATER_ADD_HURT",
    "cryoDamageBonus": "FIGHT_PROP_ICE_ADD_HURT",
    "dendroDamageBonus": "FIGHT_PROP_GRASS_ADD_HURT",
    "electroDamageBonus": "FIGHT_PROP_ELEC_ADD_HURT",
    "anemoDamageBonus": "FIGHT_PROP_WIND_ADD_HURT",
    "geoDamageBonus": "FIGHT_PROP_ROCK_ADD_HURT",
    "physicalDamageBonus": "FIGHT_PROP_PHYSICAL_ADD_HURT",
}

_map_default = {
    'maxHp': 0,
    'atk': 0,
    'def': 0,
    'elementalMastery': 0,
    'energyRecharge': 0,
    'healingBonus': 0,
    'critRate': 0,
    'critDamage': 0,
    }

def map_enka(key, data):
    if key == "maxHp":
        return data.FIGHT_PROP_MAX_HP
    elif key == "atk":
        return data.FIGHT_PROP_CUR_ATTACK
    elif key == "def":
        return data.FIGHT_PROP_CUR_DEFENSE
    elif key == "energyRecharge":
        return data.FIGHT_PROP_CHARGE_EFFICIENCY
    elif key == "healingBonus":
        return data.FIGHT_PROP_HEAL_ADD
    elif key == "critRate":
        return data.FIGHT_PROP_CRITICAL
    elif key == "critDamage":
        return data.FIGHT_PROP_CRITICAL_HURT
    elif key == "elementalMastery":
        return data.FIGHT_PROP_ELEMENT_MASTERY
    elif key == "electroDamageBonus":
        return data.FIGHT_PROP_ELEC_ADD_HURT
    elif key == "pyroDamageBonus":
        return data.FIGHT_PROP_FIRE_ADD_HURT
    elif key == "hydroDamageBonus":
        return data.FIGHT_PROP_WATER_ADD_HURT
    elif key == "cryoDamageBonus":
        return data.FIGHT_PROP_ICE_ADD_HURT
    elif key == "dendroDamageBonus":
        return data.FIGHT_PROP_GRASS_ADD_HURT
    elif key == "anemoDamageBonus":
        return data.FIGHT_PROP_WIND_ADD_HURT
    elif key == "geoDamageBonus":
        return data.FIGHT_PROP_ROCK_ADD_HURT
    elif key == "physicalDamageBonus":
        return data.FIGHT_PROP_PHYSICAL_ADD_HURT
    

def format_value(stat_name, value, reversed = False,types=0):
    if types == 0:
        if stat_name in ['atk', 'def', 'maxHp']:
            return int(value)
        elif stat_name == "elementalMastery":
            return round(value, 1)
        else:
            return math.ceil(value)
    elif types == 1:
        if reversed:
            return float('{:.2f}'.format(round(value*100,1)))
        else:
            return int(value)

color_artifact_up = {
    0: (255,255,255,255),
    1: (255,142,142,255),
    2: (255,214,142,255),
    3: (145,255,142,255),
    4: (142,255,240,255) #(235,142,255,255)
}

async def set_assets(lang):
    global assets
    assets = Assets(lang=lang)

async def get_charter_id(data):
    data = [value.strip() for value in data.split(',') if value.strip()]

    data = [value for value in data if value.isdigit()]
    
    if data == []:
        return None
    return data

async def get_info_enka(uid,USER_AGENT,lang):
    async with EnkaNetworkAPI(user_agent = USER_AGENT, lang=lang) as client:
        result = await client.fetch_user_by_uid(uid)
        if result.characters:
            return result
        else:
            return None

async def get_uid(uids):
    if type(uids) == int or type(uids) == str:
        return str(uids).replace(' ', '').split(",")[0]
    else:
        return None
    
async def get_setting_art(setting):
    processed_dict = {}
    for key, value in setting.items():
        if value > 0 and value < 1.0:
            right = 224 * value
            processed_dict[key] = int(right)

    return processed_dict

async def get_character_art(character_art):
    processed_dict = {}
    for key, value in character_art.items():
        if isinstance(value, list):
            processed_dict[key] = random.choice(value)
        else:
            processed_dict[key] = value

    return processed_dict

stat_perc = {3, 6, 9, 11, 12, 20, 21, 22, 23, 24, 25, 26, 27, 29, 30, 40, 41, 42, 43, 44, 45, 46, 47, 50, 51, 52, 53, 54, 55, 56, 3002, 3004, 3005, 3007, 3008, 3009, 3010, 3011, 3012, 3013, 3014, 3015, 3016, 3017, 3018, 3019, 3020, 3021, 3024}
IconAddTrue = ["FIGHT_PROP_PHYSICAL_ADD_HURT","FIGHT_PROP_HEAL_ADD","FIGHT_PROP_GRASS_ADD_HURT","FIGHT_PROP_FIRE_ADD_HURT","FIGHT_PROP_MAX_HP","FIGHT_PROP_CUR_ATTACK","FIGHT_PROP_CUR_DEFENSE","FIGHT_PROP_ELEMENT_MASTERY","FIGHT_PROP_CRITICAL","FIGHT_PROP_CRITICAL_HURT","FIGHT_PROP_CHARGE_EFFICIENCY","FIGHT_PROP_ELEC_ADD_HURT","FIGHT_PROP_ROCK_ADD_HURT","FIGHT_PROP_ICE_ADD_HURT","FIGHT_PROP_WIND_ADD_HURT","FIGHT_PROP_WATER_ADD_HURT"]
dopStatAtribute = {"FIGHT_PROP_MAX_HP": "BASE_HP", "FIGHT_PROP_CUR_ATTACK":"FIGHT_PROP_BASE_ATTACK","FIGHT_PROP_CUR_DEFENSE":"FIGHT_PROP_BASE_DEFENSE"}


async def check_settings(settings):
    allowed_keys = {
        "get_characters": True,
        "get_generate": True, 
        "add_characters": True,
        "add_generate": True,
        "delete_all_pickle": True, 
        "delete_characters_pickle": True,
        "delete_generate_pickle": True,
        "delete_user_characters": True,
        "delete_user_generate": True,
        "size": True,
        "auto_clear": True 
    }

    for key in allowed_keys:
        if key not in settings:
            settings[key] = False

    return settings