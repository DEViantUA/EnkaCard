# Copyright 2022 DEViantUa <t.me/deviant_ua>
# All rights reserved.
from PIL import Image, ImageChops
from . import openFile
from .options import *
from .gradient import userAdaptGrandient
import os
path = os.path.dirname(__file__).replace("utils","assets")
def centryImage(userImages, teample = 1):
    if teample == 1:
        x,y = userImages.size
        baseheight = 1200

        if x > y or x == y:
            baseheight = 787
        hpercent = (baseheight / float (y)) 
        wsize = int ((float (x) * float (hpercent)))
        userImages = userImages.resize ((wsize, baseheight), Image.LANCZOS) 

        if x > y or x == y:
            return userImages, -int(userImages.size[0]/2-300)
        else:
            return userImages, -int(userImages.size[0]/2*0.2)
    elif teample == 2:
        x,y = userImages.size
        baseheight = 1500

        if x > y or x == y:
            baseheight = 1048
        hpercent = (baseheight / float (y)) 
        wsize = int ((float (x) * float (hpercent)))
        userImages = userImages.resize ((wsize, baseheight), Image.LANCZOS) 

        if x > y or x == y:
            return userImages, 0
        else:
            return userImages, 555
    else:
        x,y = userImages.size
        baseheight = 1337

        if x > y or x == y:
            baseheight = 802
        hpercent = (baseheight / float (y)) 
        wsize = int ((float (x) * float (hpercent)))
        userImages = userImages.resize ((wsize, baseheight), Image.LANCZOS) 

        if x > y or x == y:
            return userImages, 0
        else:
            return userImages, 0


def openImageElement(element,teample = 1):
    if teample == 1:
        if element == "Fire":
            return Image.open(f'{path}/teapmleOne/background/PYRO.png')
        elif element== "Grass":
            return Image.open(f'{path}/teapmleOne/background/DENDRO.png')
        elif element == "Electric":
            return Image.open(f'{path}/teapmleOne/background/ELECTRO.png')
        elif element == "Water":
            return Image.open(f'{path}/teapmleOne/background/GYDRO.png')
        elif element == "Wind":
            return Image.open(f'{path}/teapmleOne/background/ANEMO.png')
        elif element== "Rock":
            return Image.open(f'{path}/teapmleOne/background/GEO.png')
        elif element == "Ice":
            return Image.open(f'{path}/teapmleOne/background/CRYO.png')
        else:
            return Image.open(f'{path}/teapmleOne/background/ERROR.png')
    elif teample == 2:
        if element == "Fire":
            return Image.open(f'{path}/teapmleTwo/background/PYRO.png')
        elif element== "Grass":
            return Image.open(f'{path}/teapmleTwo/background/DENDRO.png')
        elif element == "Electric":
            return Image.open(f'{path}/teapmleTwo/background/ELECTRO.png')
        elif element == "Water":
            return Image.open(f'{path}/teapmleTwo/background/GYDRO.png')
        elif element == "Wind":
            return Image.open(f'{path}/teapmleTwo/background/ANEMO.png')
        elif element== "Rock":
            return Image.open(f'{path}/teapmleTwo/background/GEO.png')
        elif element == "Ice":
            return Image.open(f'{path}/teapmleTwo/background/CRYO.png')
        else:
            return Image.open(f'{path}/teapmleTwo/background/ERROR.png')
    else:
        if element == "Fire":
            return Image.open(f'{path}/teapmleTree/background/PYRO.png')
        elif element== "Grass":
            return Image.open(f'{path}/teapmleTree/background/DENDRO.png')
        elif element == "Electric":
            return Image.open(f'{path}/teapmleTree/background/ELECTRO.png')
        elif element == "Water":
            return Image.open(f'{path}/teapmleTree/background/GYDRO.png')
        elif element == "Wind":
            return Image.open(f'{path}/teapmleTree/background/ANEMO.png')
        elif element== "Rock":
            return Image.open(f'{path}/teapmleTree/background/GEO.png')
        elif element == "Ice":
            return Image.open(f'{path}/teapmleTree/background/CRYO.png')
        else:
            return Image.open(f'{path}/teapmleTree/background/ERROR.png')

def openImageElementConstant(element, teampt = 1):
    if teampt in [1,2]:
        if element == "Fire":
            return Image.open(f'{path}/constant/PYRO.png')
        elif element== "Grass":
            return Image.open(f'{path}/constant/DENDRO.png')
        elif element == "Electric":
            return Image.open(f'{path}/constant/ELECTRO.png')
        elif element == "Water":
            return Image.open(f'{path}/constant/GYDRO.png')
        elif element == "Wind":
            return Image.open(f'{path}/constant/ANEMO.png')
        elif element== "Rock":
            return Image.open(f'{path}/constant/GEO.png')
        elif element == "Ice":
            return Image.open(f'{path}/constant/CRYO.png')
        else:
            return Image.open(f'{path}/constant/ERROR.png')
    else:
        if element == "Fire":
            return Image.open(f'{path}/teapmleTree/constant/open/OPEN_CONST_PYRO.png'),Image.open(f'{path}/teapmleTree/constant/closed/CLOSE_CONST_PYRO.png')
        elif element== "Grass":
            return Image.open(f'{path}/teapmleTree/constant/open/OPEN_CONST_DENDRO.png'),Image.open(f'{path}/teapmleTree/constant/closed/CLOSE_CONST_DENDRO.png')
        elif element == "Electric":
            return Image.open(f'{path}/teapmleTree/constant/open/OPEN_CONST_ELECTRO.png'), Image.open(f'{path}/teapmleTree/constant/closed/CLOSE_CONST_ELECTRO.png')
        elif element == "Water":
            return Image.open(f'{path}/teapmleTree/constant/open/OPEN_CONST_GYDRO.png'),Image.open(f'{path}/teapmleTree/constant/closed/CLOSE_CONST_GYDRO.png')
        elif element == "Wind":
            return Image.open(f'{path}/teapmleTree/constant/open/OPEN_CONST_ANEMO.png'), Image.open(f'{path}/teapmleTree/constant/closed/CLOSE_CONST_ANEMO.png')
        elif element== "Rock":
            return Image.open(f'{path}/teapmleTree/constant/open/OPEN_CONST_GEO.png'), Image.open(f'{path}/teapmleTree/constant/closed/CLOSE_CONST_GEO.png')
        elif element == "Ice":
            return Image.open(f'{path}/teapmleTree/constant/open/OPEN_CONST_CRYO.png'), Image.open(f'{path}/teapmleTree/constant/closed/CLOSE_CONST_CRYO.png')
        else:
            return Image.open(f'{path}/teapmleTree/constant/open/OPEN_CONST_ERROR.png'), Image.open(f'{path}/teapmleTree/constant/closed/CLOSE_CONST_ERROR.png')


def maskaAdd(element,charter, teample = 1):
    if teample == 1:
        bg = openImageElement(element)
        bgUP = bg.copy()
        bg.paste(charter,(-734,-134),charter)
        im = Image.composite(bg, bgUP, openFile.MaskaBgTeampleOne.convert('L'))
        bg.paste(im,(0,0))
    elif teample == 2:
        bg = openImageElement(element, teample = 2)
        bgUP = bg.copy()
        bg.paste(charter,(0,0),charter)
        im = Image.composite(bg, bgUP, openFile.MaskaSplas.convert('L').resize(bg.size))
        bg.paste(im,(0,0))
        bg.paste(openFile.MasskaEffectDown,(0,0),openFile.MasskaEffectDown)
    else:
        bg = openImageElement(element, teample = 3)
        bgUP = bg.copy()
        bg.paste(charter,(-810,-115),charter)
        im = Image.composite(bg, bgUP, openFile.UserBgTeampleTree.convert('L'))
        bg.paste(im,(0,0))
        bg.paste(openFile.EffectBgTeampleTree,(0,0),openFile.EffectBgTeampleTree)
    return bg


def userImage(img,element = None, adaptation = False):
    userImagess,pozitionX = centryImage(img)
    if adaptation:
        grandient = userAdaptGrandient(userImagess.convert("RGB").copy())
        Effect = openFile.UserEffectTeampleOne.copy()
        grandient = ImageChops.screen(grandient,Effect)
        Effect.paste(userImagess,(pozitionX,0),userImagess)
        im = Image.composite(Effect, grandient, openFile.MaskaUserBg2TeampleOne)
        return im
    else:
        try:
            bg = openImageElement(element)
            effect = bg.copy()
        except Exception as e:
            print(e)

        bg.paste(userImagess,(pozitionX,0))
        im = Image.composite(bg, effect, openFile.MaskaUserBg2TeampleOne)
        bg.paste(im,(0,0))
        return bg

def userImageTree(img,element = None, adaptation = False):
    userImagess,pozitionX = centryImage(img, teample = 3)
    if adaptation:
        grandient = userAdaptGrandient(userImagess.convert("RGB").copy(), size =(1924,802))
        Effect = openFile.EffectBgTree.copy()
        grandient = ImageChops.screen(grandient,Effect)
        Effect.paste(userImagess,(pozitionX,0),userImagess)
        im = Image.composite(Effect, grandient, openFile.UserBgTeampleImgTree)
        im.paste(openFile.EffectBgTeampleTree,(0,0),openFile.EffectBgTeampleTree)
        return im
    else:
        bg = openImageElement(element, teample = 3)
        effect = bg.copy()
        bg.paste(userImagess,(pozitionX,0),userImagess)
        im = Image.composite(bg, effect, openFile.UserBgTeampleImgTree)
        bg.paste(im,(0,0))
        bg.paste(openFile.EffectBgTeampleTree,(0,0),openFile.EffectBgTeampleTree)
        return bg


def userImageTwo(img,element = None, adaptation = False):
    userImagess,pozitionX = centryImage(img, teample = 2)
    if adaptation:
        bg = openImageElement("error", teample = 2)
        grandientLeft = userAdaptGrandient(userImagess.convert("RGB").copy(), size = (1038, 1048),left = True)
        grandientRight = userAdaptGrandient(userImagess.convert("RGB").copy(), size = (937, 1048))
        bg.paste(grandientLeft,(0,0),grandientLeft)
        bg.paste(grandientRight,(grandientLeft.size[0],0),grandientRight)
        Effect = openFile.UserEffectTeampleTwo.copy()
        grandient = ImageChops.screen(bg,Effect)
        Effect.paste(userImagess,(pozitionX,0),userImagess)
        im = Image.composite(Effect, grandient, openFile.UserBgTeampleTwo)
        return im
    else:
        bg = openImageElement(element, teample = 2)
        effect = bg.copy()
        bg.paste(userImagess,(pozitionX,0),userImagess)
        im = Image.composite(bg, effect, openFile.UserBgTeampleTwo)
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
        imgs = Image.open(f'{path}/stars/Star1.png')
    elif x == 2:
        imgs = Image.open(f'{path}/stars/Star2.png')
    elif x == 3:
        imgs = Image.open(f'{path}/stars/Star3.png')
    elif x == 4:
        imgs = Image.open(f'{path}/stars/Star4.png')
    elif x == 5:
        imgs = Image.open(f'{path}/stars/Star5.png')

    return imgs.copy()


def elementIconPanel(element):
    if element == "Fire":
        return Image.open(f'{path}/teapmleTwo/charter_element/PYRO.png')
    elif element== "Grass":
        return Image.open(f'{path}/teapmleTwo/charter_element/DENDRO.png')
    elif element == "Electric":
        return Image.open(f'{path}/teapmleTwo/charter_element/ELECTRO.png')
    elif element == "Water":
        return Image.open(f'{path}/teapmleTwo/charter_element/GYDRO.png')
    elif element == "Wind":
        return Image.open(f'{path}/teapmleTwo/charter_element/ANEMO.png')
    elif element== "Rock":
        return Image.open(f'{path}/teapmleTwo/charter_element/GEO.png')
    elif element == "Ice":
        return Image.open(f'{path}/teapmleTwo/charter_element/CRYO.png')
    else:
        return Image.open(f'{path}/teapmleTwo/charter_element/PYRO.png')

def getIconAdd(x, icon = False, size = None):
    if not icon:
        if not x in IconAddTrue:
            return False
    if x == "FIGHT_PROP_MAX_HP" or x == "FIGHT_PROP_HP":
        icons = Image.open(f'{path}/icon/HP.png')  
    elif x == "FIGHT_PROP_CUR_ATTACK" or x =="FIGHT_PROP_ATTACK":
        icons = Image.open(f'{path}/icon/ATTACK.png')
    elif x == "FIGHT_PROP_CUR_DEFENSE" or x == "FIGHT_PROP_DEFENSE":
        icons = Image.open(f'{path}/icon/DEFENSE.png')
    elif x == "FIGHT_PROP_ELEMENT_MASTERY":
        icons = Image.open(f'{path}/icon/MASTERY.png')
    elif x == "FIGHT_PROP_CRITICAL":
        icons = Image.open(f'{path}/icon/CRITICAL_HURT.png')
    elif x == "FIGHT_PROP_CRITICAL_HURT":
        icons = Image.open(f'{path}/icon/CRITICAL.png')
    elif x == "FIGHT_PROP_CHARGE_EFFICIENCY":
        icons = Image.open(f'{path}/icon/CHARGE_EFFICIENCY.png')
    elif x == "FIGHT_PROP_ELEC_ADD_HURT":
        icons = Image.open(f'{path}/icon/ELECTRO.png')
    elif x == "FIGHT_PROP_DEFENSE_PERCENT":
        icons = Image.open(f'{path}/icon/DEFENSE_PERCENT.png')
    elif x == "FIGHT_PROP_ATTACK_PERCENT":
        icons = Image.open(f'{path}/icon/ATTACK_PERCENT.png')
    elif x == "FIGHT_PROP_HP_PERCENT":
        icons = Image.open(f'{path}/icon/HP_PERCENT.png')
    elif x == "FIGHT_PROP_WATER_ADD_HURT":
        icons = Image.open(f'{path}/icon/HYDRO.png')
    elif x == "FIGHT_PROP_WIND_ADD_HURT":
        icons = Image.open(f'{path}/icon/ANEMO.png')
    elif x == "FIGHT_PROP_ICE_ADD_HURT":
        icons = Image.open(f'{path}/icon/CRYO.png')
    elif x == "FIGHT_PROP_ROCK_ADD_HURT":
        icons = Image.open(f'{path}/icon/GEO.png')
    elif x == "FIGHT_PROP_FIRE_ADD_HURT":
        icons = Image.open(f'{path}/icon/PYRO.png')
    elif x == "FIGHT_PROP_GRASS_ADD_HURT":
        icons = Image.open(f'{path}/icon/DENDRO.png')
    elif x == "FIGHT_PROP_HEAL_ADD":
        icons = Image.open(f'{path}/icon/HEALED_ADD.png')
    elif x == "FIGHT_PROP_HEAL":
        icons = Image.open(f'{path}/icon/HEAL.png')
    else:
        return False
    if size:
        icons.thumbnail(size)
        return icons.convert("RGBA").copy()
    else:
        return icons.convert("RGBA").copy()
