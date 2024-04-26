import aiohttp
import asyncio
import json


DATA_URL = "https://gitlab.com/Dimbreath/AnimeGameData/-/raw/master/{FOLDER}/{value}"
LANG_URL = "https://gitlab.com/Dimbreath/AnimeGameData/-/raw/master/{LANG_FOLDER}/TextMap{key}.json"
_PATH = None

from .pathfinding import search

from .config import (
    FOLDER,
    LANG_FOLDER,
    AVATAR,
    COSTUME,
    SKILLDEPOT,
    SKILLS,
    TALENTS,
    ARTIFACTS,
    WEAPONS,
    ARTIFACTS_SETS,
    FIGHT_PROPS,
    PROPS_MAP,
    NAMECARDS,
    ARTIFACT_PROPS_MAIN,
    ARTIFACT_PROPS_SUB,
    ENVKEY,
    LANGKEY
)

_DATA = {}
_DATA_LANG = {
    "artifact_sets": [],
    "artifacts": [],
    "characters": [],
    "constellations": [],
    "fight_props": [],
    "namecards": [],
    "skills": [],
    "weapons": [],
}

def save_json(NAME_JSON, data, path = "data"):
    global _PATH
    
    with open(f"{_PATH}/{path}/{NAME_JSON}", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

async def fetch_data(url, key, lang = False):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.text()
                _DATA[key] = json.loads(data)
    if lang:
        print(f"| Dowload lang: {key}")

async def creat_artifact_sets():
    data = {}
    for key in _DATA["ARTIFACTS_SETS"]:
        data[key["id"]] = {"affixId": key["affixId"], "nameTextMapHash": key["nameTextMapHash"]}
        _DATA_LANG["artifact_sets"].append(str(key["nameTextMapHash"]))
        
async def creat_weapon():   
    data = {}
    
    for key in _DATA["WEAPONS"]:
        data[key["id"]] = {"nameTextMapHash": key["nameTextMapHash"], "icon": key["icon"], "awakenIcon": key["awakenIcon"], "rankLevel": key["rankLevel"]}
        _DATA_LANG["weapons"].append(str(key["nameTextMapHash"]))
    save_json("weapons.json", data)

async def creat_namecards():   
    data = {}
       
    for key in _DATA["NAMECARDS"]:
        if key.get("materialType", "_") == "MATERIAL_NAMECARD":
            data[key["id"]] = {"nameTextMapHash": key["nameTextMapHash"], "icon": key["icon"], "picPath": key["picPath"], "rankLevel": key["rankLevel"], "materialType": key["materialType"]}
            _DATA_LANG["namecards"].append(str(key["nameTextMapHash"]))
    save_json("namecards.json", data)

async def creat_artifact():
    data = {}
    
    for key in _DATA["ARTIFACTS"]:
        data[key["id"]] = {"nameTextMapHash": key["nameTextMapHash"], "itemType": key["itemType"], "equipType": key["equipType"], "icon": key["icon"], "rankLevel": key["rankLevel"], "mainPropDepotId": key["mainPropDepotId"], "appendPropDepotId": key["appendPropDepotId"]}
        
        _DATA_LANG["artifacts"].append(str(key["nameTextMapHash"]))
        
    save_json("artifacts.json", data)
    
async def creat_costume():   
    data = {}

    for key in _DATA["COSTUME"]:
        data[key["skinId"]] = {"iconName": key["frontIconName"], "sideIconName": key["sideIconName"], "nameTextMapHash": key["nameTextMapHash"]}
    
    save_json("costumes.json", data)
        
async def creat_fight_props():
    data = {}
    
    for key in _DATA["FIGHT_PROPS"]:
        data[key["textMapId"]] = {"nameTextMapHash": key["textMapContentTextMapHash"]}
    save_json("fight_props.json", data)
        
async def creat_skill():
    data = {}
    
    for key in _DATA["SKILLS"]:
        if key["skillIcon"]:
            data[key["id"]] = {"nameTextMapHash": key["nameTextMapHash"], "skillIcon": key["skillIcon"], "proudSkillGroupId": key.get("proudSkillGroupId","")}
            _DATA_LANG["skills"].append(str(key["nameTextMapHash"]))
    save_json("skills.json", data)

async def creat_const():
    data = {}
    
    for key in _DATA["TALENTS"]:
        data[key["talentId"]] = {"nameTextMapHash": key["nameTextMapHash"], "icon": key["icon"]}
        _DATA_LANG["constellations"].append(str(key["nameTextMapHash"]))
    save_json("constellations.json", data)
    
async def creat_skill_depo():
    
    data = {}
    
    for key in _DATA["SKILLDEPOT"]:
        if key["id"] == 101 or key.get("energySkill",0) != 0:
            data[key["id"]] = {"id":key["id"],"energySkill": key["energySkill"], "skills": key["skills"], "subSkills": key["subSkills"], "talents": key["talents"]}
            
    return data

async def creat_characrer():
 
    data = {}
    sub_data = await creat_skill_depo()
   
    skill_data = {}
    for key in _DATA["SKILLS"]:
        skill_data[key["id"]] = {"nameTextMapHash": key["nameTextMapHash"], "skillIcon": key["skillIcon"], "proudSkillGroupId": key.get("proudSkillGroupId",""), "costElemType": key.get("costElemType", None), "forceCanDoSkill": key.get("forceCanDoSkill", None)}
   
    for key in _DATA["AVATAR"]:
        if key["skillDepotId"] == 101 or \
            key["iconName"].endswith("_Kate") or \
            str(key['id'])[:2] == "11":
                continue    
        
        _DATA_LANG["characters"].append(str(key["nameTextMapHash"]))
           
        if key["iconName"].endswith("_PlayerBoy") or key["iconName"].endswith("_PlayerGirl"):
            new_data =  {"nameTextMapHash": key["nameTextMapHash"], "iconName": key["iconName"], "sideIconName": key["sideIconName"], "qualityType": key["qualityType"], 
                           "costElemType": "", "skills": [], "talents": [] }
            
            for skill_id in key["candSkillDepotIds"]:
                new_data.update({"skills": [],"talents": []})
                
                depot = sub_data.get(skill_id)
                if depot and depot["id"] != 101:
                    for skill in depot["skills"]:
                        if skill <= 0:
                            continue
                        new_data["skills"].append(skill)
                        
                    element_id = skill_data.get(depot.get("energySkill"))
                    
                    new_data.update({
                            "costElemType": element_id.get("costElemType")
                        })
                    
                    new_data["skills"].append(int(depot.get('energySkill')))   

                    new_data.update({
                        "talents": [x for x in depot["talents"] if x > 0],
                    })
                    
                    data[str(key["id"]) + "-" + str(depot["id"])] = new_data.copy()
  
            data[str(key["id"])] = new_data.copy()
        else:
            data[key["id"]] = {"nameTextMapHash": key["nameTextMapHash"], "iconName": key["iconName"], "sideIconName": key["sideIconName"], "qualityType": key["qualityType"], 
                           "costElemType": "", "skills": [], "talents": [] }
            depot = sub_data.get(key["skillDepotId"])
            if depot and depot["id"] != 101:
                for skill in depot["skills"]:
                    if skill <= 0:
                        continue
                    skill_info = skill_data.get(int(skill))
                    if not skill_info["forceCanDoSkill"] is None:
                        continue
                    data[key["id"]]["skills"].append(skill)
                element_id = skill_data.get(depot.get("energySkill"))
                data[key["id"]]["costElemType"] = element_id.get("costElemType")
                
                data[key["id"]]["skills"].append(int(depot.get('energySkill')))  
                data[key["id"]]["talents"] =  [x for x in depot["talents"] if x > 0]
                
    save_json("characters.json", data)

async def creat_artifact_prop():
    data = {}
    ARTIFACT_PROPS = []
    ARTIFACT_PROPS.extend(_DATA["ARTIFACT_PROPS_MAIN"])
    ARTIFACT_PROPS.extend(_DATA["ARTIFACT_PROPS_SUB"])
    
    PERCENT = ['HURT','CRITICAL','EFFICIENCY','PERCENT','ADD']
    
        
    for key in ARTIFACT_PROPS:
        ISPERCENT = key['propType'].split("_")[-1] in PERCENT
        RAW = key.get("propValue", 0)

        data[key["id"]] = {
            'propType': key['propType'],
            'propDigit': 'PERCENT' if ISPERCENT else 'DIGIT',
            'propValue': round(RAW * 100, 1) if ISPERCENT else round(RAW)
        }
    
    save_json("artifact_props.json", data)

async def creat_lang():
    task = []
    for key in LANGKEY:
        url = LANG_URL.format(LANG_FOLDER = LANG_FOLDER, key = key)
        task.append(fetch_data(url, key, lang= True))
    print(">> Start dowload lang")
    await asyncio.gather(*task)
    
    print("| End dowload lang")
    
    print(">> Start update lang")
    
    data = {
        "artifact_sets": {},
        "artifacts": {},
        "characters": {},
        "constellations": {},
        "namecards": {},
        "skills": {},
        "weapons": {}
    }
    
    set_lang = {"CHS": "",
        "CHT": "",
        "DE": "",
        "EN": "",
        "ES": "",
        "FR": "",
        "ID": "",
        "IT": "",
        "JP": "",
        "KR": "",
        "PT": "",
        "RU": "",
        "TH": "",
        "TR": "",
        "VI": ""
    }
    
    count = 1
    
    for name in data:
        for key in _DATA_LANG[name]:
            data[name][key] = {
                "CHS": _DATA["CHS"].get(key,""),
                "DE": _DATA["DE"].get(key,""),
                "EN": _DATA["EN"].get(key,""),
                "ES": _DATA["ES"].get(key,""),
                "FR": _DATA["FR"].get(key,""),
                "ID": _DATA["ID"].get(key,""),
                "IT": _DATA["IT"].get(key,""),
                "JP": _DATA["JP"].get(key,""),
                "KR": _DATA["KR"].get(key,""),
                "PT": _DATA["PT"].get(key,""),
                "RU": _DATA["RU"].get(key,""),
                "TH": _DATA["TH"].get(key,""),
                "TR": _DATA["TR"].get(key,""),
                "VI": _DATA["VI"].get(key,""),
            }
        print(f"| ({count}/7) Finish Convert {name}") 
        count += 1

    for key in data:
        save_json(f"{key}.json", data[key], path= "langs")
        
    print("| End update lang")
    
async def dowload(path = None):
    global _PATH
    
    if path is None:
        _PATH = await search()
    else:
        _PATH = path
        
    if "data" in _PATH:
        _PATH = _PATH.replace("/data", "")
    
    print(f"Path to enkanetwork.py: {_PATH}")
    print("="*25)
    print(">> Start dowload data")
    variables = {key: globals()[key] for key in ENVKEY}
    task = []
    for key, value in variables.items():
        url = DATA_URL.format(FOLDER = FOLDER, value = value)
        task.append(fetch_data(url, key))
        
    await asyncio.gather(*task)
    print("| End dowload data")
    
    print(">> Start update data")
    
    await asyncio.gather(creat_artifact_sets(),
                        creat_weapon(),
                        creat_namecards(),
                        creat_artifact(),
                        creat_costume(),
                        creat_fight_props(),
                        creat_skill(),
                        creat_const(),
                        creat_characrer(),
                        creat_artifact_prop(),
    )
    
    print("| End update data")
    
    print("="*25)
    
    await creat_lang()
    
    print("="*25)
