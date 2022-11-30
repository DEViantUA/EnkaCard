# Copyright 2022 DEViantUa <t.me/deviant_ua>
# All rights reserved.
from PIL import Image, ImageChops
from .openFile import *
from .options import *
from .gradient import userAdaptGrandient
import time


def centryImage(userImages, teample = 1):
    if teample == 1:
        x,y = userImages.size
        baseheight = 1200

        if x > y or x == y:
            baseheight = 787
        hpercent = (baseheight / float (y)) 
        wsize = int ((float (x) * float (hpercent)))
        userImages = userImages.resize ((wsize, baseheight), Image.ANTIALIAS) 

        if x > y or x == y:
            return userImages, -int(userImages.size[0]/2-300)
        else:
            return userImages, -int(userImages.size[0]/2*0.2)
    else:
        x,y = userImages.size
        baseheight = 1500

        if x > y or x == y:
            baseheight = 1048
        hpercent = (baseheight / float (y)) 
        wsize = int ((float (x) * float (hpercent)))
        userImages = userImages.resize ((wsize, baseheight), Image.ANTIALIAS) 

        if x > y or x == y:
            return userImages, 0
        else:
            return userImages, 555
def openImageElement(element,teample = 1):
    if teample == 1:
        if element == "Fire":
            return PyroBgTeampleOne.copy()
        elif element== "Grass":
            return DendroBgTeampleOne.copy()
        elif element == "Electric":
            return ElectroBgTeampleOne.copy()
        elif element == "Water":
            return GydroBgTeampleOne.copy()
        elif element == "Wind":
            return AnemoBgTeampleOne.copy()
        elif element== "Rock":
            return GeoBgTeampleOne.copy()
        elif element == "Ice":
            return CryoBgTeampleOne.copy()
        else:
            return ErrorBgTeampleOne.copy()
    else:
        if element == "Fire":
            return PyroBgTeampleTwo.copy()
        elif element== "Grass":
            return DendroBgTeampleTwo.copy()
        elif element == "Electric":
            return ElectroBgTeampleTwo.copy()
        elif element == "Water":
            return GydroBgTeampleTwo.copy()
        elif element == "Wind":
            return AnemoBgTeampleTwo.copy()
        elif element== "Rock":
            return GeoBgTeampleTwo.copy()
        elif element == "Ice":
            return CryoBgTeampleTwo.copy()
        else:
            return ErrorBgTeampleTwo.copy()
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

def maskaAdd(element,charter, teample = 1):
    if teample == 1:
        bg = openImageElement(element)
        bgUP = bg.copy()
        bg.paste(charter,(-734,-134),charter)
        im = Image.composite(bg, bgUP, MaskaBgTeampleOne)
        bg.paste(im,(0,0))
    else:
        bg = openImageElement(element, teample = 2)
        bgUP = bg.copy()
        bg.paste(charter,(0,0),charter)
        im = Image.composite(bg, bgUP, MaskaSplas)
        bg.paste(im,(0,0))
        bg.paste(MasskaEffectDown,(0,0),MasskaEffectDown)
    return bg

def userImage(img,element = None, adaptation = False):
    userImagess,pozitionX = centryImage(img)
    if adaptation:
        grandient = userAdaptGrandient(userImagess.convert("RGB").copy())
        Effect = UserEffectTeampleOne.copy()
        grandient = ImageChops.screen(grandient,Effect)
        Effect.paste(userImagess,(pozitionX,0),userImagess)
        im = Image.composite(Effect, grandient, MaskaUserBg2TeampleOne)
        return im
    else:
        try:
            bg = openImageElement(element)
            #bg.load()
            effect = bg.copy()
        except Exception as e:
            print(e)

        bg.paste(userImagess,(pozitionX,0))
        im = Image.composite(bg, effect, MaskaUserBg2TeampleOne)
        bg.paste(im,(0,0))
        return bg

def userImageTwo(img,element = None, adaptation = False):
    userImagess,pozitionX = centryImage(img, teample = 2)
    if adaptation:
        bg = openImageElement("error", teample = 2)
        grandientLeft = userAdaptGrandient(userImagess.convert("RGB").copy(), size = (1038, 1048),left = True)
        grandientRight = userAdaptGrandient(userImagess.convert("RGB").copy(), size = (937, 1048))
        bg.paste(grandientLeft,(0,0),grandientLeft)
        bg.paste(grandientRight,(grandientLeft.size[0],0),grandientRight)
        Effect = UserEffectTeampleTwo.copy()
        grandient = ImageChops.screen(bg,Effect)
        Effect.paste(userImagess,(pozitionX,0),userImagess)
        im = Image.composite(Effect, grandient, UserBgTeampleTwo)
        return im
    else:
        bg = openImageElement(element, teample = 2)
        effect = bg.copy()
        bg.paste(userImagess,(pozitionX,0),userImagess)
        im = Image.composite(bg, effect, UserBgTeampleTwo)
        bg.paste(im,(0,0))
        return bg

'''
def userImageBlur(img,element = None, adaptation = False):
    userImagess,pozitionX = centryImage(img)
    if adaptation:
        Effect = UserEffectTeampleOne.copy()
        bgBlur = userImagess.filter(ImageFilter.GaussianBlur(radius=80)).resize(Effect.size).convert("RGBA")
        bgBlur = ImageChops.screen(bgBlur,Effect)
        Effect.paste(userImagess,(pozitionX,0),userImagess)
        bg = Image.composite(Effect, bgBlur, MaskaUserBg2TeampleOne) 
        return bg
    else:
        img = openImageElement(element)
        effect = img.copy()
        img.paste(userImagess,(pozitionX,0))
        img.show()
        im = Image.composite(img, effect, MaskaUserBgTeampleOne)
        img.paste(im,(0,0))
        return img
'''

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


def elementIconPanel(element):
    if element == "Fire":
        return PyroCharterElementTeampleTwo.copy()
    elif element== "Grass":
        return DendroCharterElementTeampleTwo.copy()
    elif element == "Electric":
        return ElectoCharterElementTeampleTwo.copy()
    elif element == "Water":
        return GydroCharterElementTeampleTwo.copy()
    elif element == "Wind":
        return AnemoCharterElementTeampleTwo.copy()
    elif element== "Rock":
        return GeoCharterElementTeampleTwo.copy()
    elif element == "Ice":
        return CryoCharterElementTeampleTwo.copy()
    else:
        return PyroCharterElementTeampleTwo.copy()

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
