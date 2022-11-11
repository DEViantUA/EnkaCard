# Copyright 2022 DEViantUa <t.me/deviant_ua>
# All rights reserved.
from PIL import Image, ImageFilter, ImageChops
from .openFile import *
from .options import *
from .gradient import userAdaptGrandient


def centryImage(userImages):
    x,y = userImages.size
    if x > y or x == y:
        baseheight = 787
        hpercent = (baseheight / float (userImages.size[1])) 
        wsize = int ((float (userImages.size[0]) * float (hpercent)))
        userImages = userImages.resize ((wsize, baseheight), Image.ANTIALIAS) 
        positionX = -int(userImages.size[0]/2-300)
    else:
        baseheight = 1000
        hpercent = (baseheight / float (userImages.size[1])) 
        wsize = int ((float (userImages.size[0]) * float (hpercent)))
        userImages = userImages.resize ((wsize, baseheight), Image.ANTIALIAS) 
        positionX = -int(userImages.size[0]/2*0.2)
    return userImages, positionX
    

def openImageElement(element):
    if element == "Fire":
        return PyroBg.copy()
    elif element== "Grass":
        return DendroBg.copy()
    elif element == "Electric":
        return ElectroBg.copy()
    elif element == "Water":
        return GydroBg.copy()
    elif element == "Wind":
        return AnemoBg.copy()
    elif element== "Rock":
        return GeoBg.copy()
    elif element == "Ice":
        return CryoBg.copy()
    else:
        return ErrorBg.copy()
    
def openImageElementConstant(element):
    if element == "Fire":
        return PyroConstant.copy()
    elif element== "Grass":
        return DendroConstant.copy()
    elif element == "Electric":
        return ElectroConstant.copy()
    elif element == "Water":
        return GydroConstant.copy()
    elif element == "Wind":
        return AnemoConstant.copy()
    elif element== "Rock":
        return GeoConstant.copy()
    elif element == "Ice":
        return CryoConstant.copy()
    else:
        return ErrorConstant.copy()

def maskaAdd(element,charter):
    bg = openImageElement(element)
    bgUP = bg.copy()
    bg.paste(charter,(-734,-134),charter)
    im = Image.composite(bg, bgUP, MaskaBg) #ЗАДНИК / НАКЛАДЫВАЕМЫЙ / МАСКА
    bg.paste(im,(0,0))
    return bg


def userImage(img,element = None, adaptation = False):
    userImagess,pozitionX = centryImage(img)
    if adaptation:
        grandient = userAdaptGrandient(userImagess.convert("RGB").copy())
        Effect = UserEffect.copy()
        grandient = ImageChops.screen(grandient,Effect)
        Effect.paste(userImagess,(pozitionX,0),userImagess)
        im = Image.composite(Effect, grandient, MaskaUserBg2) #ЗАДНИК / НАКЛАДЫВАЕМЫЙ / МАСКА
        return im
    else:
        bg = openImageElement(element)
        effect = bg.copy()
        bg.paste(userImagess,(pozitionX,0),userImagess)
        im = Image.composite(bg, effect, MaskaUserBg) #ЗАДНИК / НАКЛАДЫВАЕМЫЙ / МАСКА
        bg.paste(im,(0,0))
        return bg

def userImageBlur(img,element = None, adaptation = False):
    userImagess,pozitionX = centryImage(img)
    if adaptation:
        Effect = UserEffect.copy()
        bgBlur = userImagess.filter(ImageFilter.GaussianBlur(radius=80)).resize(Effect.size).convert("RGBA")
        bgBlur = ImageChops.screen(bgBlur,Effect)
        Effect.paste(userImagess,(pozitionX,0),userImagess)
        bg = Image.composite(Effect, bgBlur, MaskaUserBg2) #ЗАДНИК / НАКЛАДЫВАЕМЫЙ / МАСКА
        return bg
    else:
        img = openImageElement(element)
        effect = img.copy()
        img.paste(userImagess,(pozitionX,0))
        img.show()
        im = Image.composite(img, effect, MaskaUserBg) #ЗАДНИК / НАКЛАДЫВАЕМЫЙ / МАСКА
        img.paste(im,(0,0))
        return img
    
def star(x):
    if x == 1:
        imgs = Star1
    elif x == 2:
        imgs = Star2
    elif x == 3:
        imgs = Star3
    elif x == 4:
        imgs = Star4
    elif x == 5:
        imgs = Star5

    return imgs


def getIconAdd(x, icon = False, size = None):
    if not icon:
        if not x in IconAddTrue:
            return False
    if x == "FIGHT_PROP_MAX_HP" or x == "FIGHT_PROP_HP":
        icons = FIGHT_PROP_MAX_HP 
    elif x == "FIGHT_PROP_CUR_ATTACK" or x =="FIGHT_PROP_ATTACK":
        icons = FIGHT_PROP_CUR_ATTACK
    elif x == "FIGHT_PROP_CUR_DEFENSE" or x == "FIGHT_PROP_DEFENSE":
        icons = FIGHT_PROP_CUR_DEFENSE
    elif x == "FIGHT_PROP_ELEMENT_MASTERY":
        icons = FIGHT_PROP_ELEMENT_MASTERY
    elif x == "FIGHT_PROP_CRITICAL":
        icons = FIGHT_PROP_CRITICAL
    elif x == "FIGHT_PROP_CRITICAL_HURT":
        icons = FIGHT_PROP_CRITICAL_HURT
    elif x == "FIGHT_PROP_CHARGE_EFFICIENCY":
        icons = FIGHT_PROP_CHARGE_EFFICIENCY
    elif x == "FIGHT_PROP_ELEC_ADD_HURT":
        icons = FIGHT_PROP_ELEC_ADD_HURT
    elif x == "FIGHT_PROP_DEFENSE_PERCENT":
        icons = FIGHT_PROP_DEFENSE_PERCENT
    elif x == "FIGHT_PROP_ATTACK_PERCENT":
        icons = FIGHT_PROP_ATTACK_PERCENT
    elif x == "FIGHT_PROP_HP_PERCENT":
        icons = FIGHT_PROP_HP_PERCENT
    elif x == "FIGHT_PROP_WATER_ADD_HURT":
        icons = FIGHT_PROP_WATER_ADD_HURT
    elif x == "FIGHT_PROP_WIND_ADD_HURT":
        icons = FIGHT_PROP_WIND_ADD_HURT
    elif x == "FIGHT_PROP_ICE_ADD_HURT":
        icons = FIGHT_PROP_ICE_ADD_HURT
    elif x == "FIGHT_PROP_ROCK_ADD_HURT":
        icons = FIGHT_PROP_ROCK_ADD_HURT
    elif x == "FIGHT_PROP_FIRE_ADD_HURT":
        icons = FIGHT_PROP_FIRE_ADD_HURT
    elif x == "FIGHT_PROP_GRASS_ADD_HURT":
        icons = FIGHT_PROP_GRASS_ADD_HURT
    elif x == "FIGHT_PROP_HEAL_ADD":
        icons = FIGHT_PROP_HEAL_ADD
    elif x == "FIGHT_PROP_HEAL":
        icons = FIGHT_PROP_HEAL
    else:
        return False
    
    if size:
        icons.thumbnail(size)
        return icons.convert("RGBA")
    else:
        return icons.convert("RGBA")
