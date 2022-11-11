# Copyright 2022 DEViantUa <t.me/deviant_ua>
# All rights reserved.
from googletrans import Translator

translator = Translator()

def translate(lang = "ru"):
    if lang == "ru":
        return "Уровень"
    elif lang == "en":
        return "LVL"
    try:
        result = translator.translate("Уровень", src = "ru", dest = lang)
        return result.text
    except Exception as e:
        return "LVL"