# Copyright 2022 DEViantUa <t.me/deviant_ua>
# All rights reserved.
from googletrans import Translator

translator = Translator()
supportLang = {"en":"en", 
        "ru":"ru",
        "vi": "vi", 
        "th":"th",
        "pt":"pt",
        "kr":"ko",
        "jp":"ja",
        "zh":"zh-cn",
        "id":"id",
        "fr":"fr",
        "es":"es",
        "de":"de",
        "chs":"zh-tw",
        "cht":"zh-tw"
    }

def translate(lang = "ru"):
    if lang == "ru":
        return {"lvl": "Уровень", "AR":"РП", "WL":"УМ", "AC": "Достижения", "AB": "Бездна"}
    elif lang == "en":
        return  {"lvl": "LVL", "AR":"AR", "WL":"WL", "AC": "Achievements", "AB": "Abyss"}
    try:
        result = translator.translate("Уровень -- Достижения -- Бездна", src = "ru", dest = supportLang[lang])
        return {"lvl": result.text.split("--")[0], "AR":"AR", "WL":"WL", "AC": result.text.split("--")[1], "AB": result.text.split("--")[2]}
    except Exception as e:
        return {"lvl": "LVL", "AR":"AR", "WL":"WL", "AC": "Achievements", "AB": "Abyss"}