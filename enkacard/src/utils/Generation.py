# Copyright 2022 DEViantUa <t.me/deviant_ua>
# All rights reserved.
from PIL import Image, ImageChops,ImageFilter
from . import openFile
from .options import *
from .gradient import userAdaptGrandient, colorBg
import os
path = os.path.dirname(__file__).replace("utils","assets")

'''
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
            x,y = userImages.size
            if x < 738:
                return userImages, -int(userImages.size[0]/2*0.2)
            else:
                return userImages, -int(userImages.size[0]-738)
        

        x,y = userImages.size
        if x > y:
            baseheight = 787
            hpercent = (baseheight / float (y)) 
            wsize = int ((float (x) * float (hpercent)))
            userImages = userImages.resize ((wsize, baseheight), Image.LANCZOS)
            return userImages, -int(userImages.size[0]/2-300)
        elif x == y or x-y < 10:
            basewidth = 838
            wpercent = (basewidth / float(userImages.size[0]))
            hsize = int((float(userImages.size[1]) * float(wpercent)))
            userImages = userImages.resize((basewidth, hsize), Image.LANCZOS)
            return userImages, -81
        else:
            basewidth = 838
            wpercent = (basewidth / float(userImages.size[0]))
            hsize = int((float(userImages.size[1]) * float(wpercent)))
            userImages = userImages.resize((basewidth, hsize), Image.LANCZOS)
            return userImages, 0


            basewidth = 575
            wpercent = (basewidth / float(userImages.size[0]))
            hsize = int((float(userImages.size[1]) * float(wpercent)))
            userImages = userImages.resize((basewidth, hsize), Image.LANCZOS)
            return userImages, 0
            # вертикальное

x,y = userImages.size
sizeImg = x/y
if sizeImg > 1.1:
    baseheight = 1048
    hpercent = (baseheight / float (y)) 
    wsize = int ((float (x) * float (hpercent)))
    userImages = userImages.resize((wsize, baseheight), Image.LANCZOS)
    if sizeImg > 1.1 and sizeImg < 1.19 or sizeImg > 2.1 :
        return userImages, 0
    else:
        return userImages, 487
else:
    basewidth = 1085
    wpercent = (basewidth / float(userImages.size[0]))
    hsize = int((float(userImages.size[1]) * float(wpercent)))
    userImages = userImages.resize((basewidth, hsize), Image.LANCZOS)
    return userImages, 487

x,y = userImages.size
baseheight = 1500

if x > y or x == y:
    baseheight = 1048
hpercent = (baseheight / float (y)) 
wsize = int ((float (x) * float (hpercent)))
userImages = userImages.resize((wsize, baseheight), Image.LANCZOS) 

if x > y or x == y:
    return userImages, 0
else:
    return userImages, 555

x,y = userImages.size
        baseheight = 965

        if x > y or x == y:
            baseheight = 621
        hpercent = (baseheight / float (y)) 
        wsize = int ((float (x) * float (hpercent)))
        userImages = userImages.resize((wsize, baseheight), Image.LANCZOS) 

        if x > y or x == y:
            return userImages, -359
        else:
            x,y = userImages.size
            if x < 552:
                return userImages, -int(userImages.size[0]/2*0.2)
            else:
                return userImages, -int(userImages.size[0]-552)
            #return userImages, -116

x,y = userImages.size
        baseheight = 1311

        if x > y or x == y:
            baseheight = 802
        hpercent = (baseheight / float (y)) 
        wsize = int ((float (x) * float (hpercent)))
        userImages = userImages.resize ((wsize, baseheight), Image.LANCZOS) 

        if x > y or x == y:
            return userImages, -int(userImages.size[0]/2-300)
        else:
            x,y = userImages.size
            if x < 806:
                return userImages, 0
            else:
                return userImages, -int(x-806) 
x,y = userImages.size
        sizeImg = x/y
        if sizeImg > 1.1:
            baseheight = 621 
            hpercent = (baseheight / float (y)) 
            wsize = int ((float (x) * float (hpercent)))
            userImages = userImages.resize ((wsize, baseheight), Image.LANCZOS)
            return userImages, -int(userImages.size[0]/2-250)
        else:
            basewidth = 667
            wpercent = (basewidth / float(userImages.size[0]))
            hsize = int((float(userImages.size[1]) * float(wpercent)))
            userImages = userImages.resize((basewidth, hsize), Image.LANCZOS)
            return userImages, -119           
'''
def centryImage(userImages, teample = 1):
    if teample == 6:
        x,y = userImages.size
        if max(x, y) / min(x, y) < 1.1:
            baseheight = 1615
            hpercent = (baseheight / float (y)) 
            wsize = int ((float (x) * float (hpercent)))
            userImages = userImages.resize ((wsize, baseheight), Image.LANCZOS)
            return userImages, -235
            # квадратное 
        elif x > y:
            baseheight = 1615
            hpercent = (baseheight / float (y)) 
            wsize = int ((float (x) * float (hpercent)))
            userImages = userImages.resize ((wsize, baseheight), Image.LANCZOS)
            return userImages, int(515 -userImages.size[0]/2)
        else:
            basewidth = 1066
            wpercent = (basewidth / float(userImages.size[0]))
            hsize = int((float(userImages.size[1]) * float(wpercent)))
            if hsize < 1615:
                baseheight = 1615
                hpercent = (baseheight / float (y)) 
                wsize = int ((float (x) * float (hpercent)))
                userImages = userImages.resize ((wsize, baseheight), Image.LANCZOS)
                return userImages, int(515 -userImages.size[0]/2)
            userImages = userImages.resize((basewidth, hsize), Image.LANCZOS)

            return userImages, 0
        
    elif teample == 1:
        x,y = userImages.size
        if max(x, y) / min(x, y) < 1.1:
            baseheight = 787
            hpercent = (baseheight / float (y)) 
            wsize = int ((float (x) * float (hpercent)))
            userImages = userImages.resize ((wsize, baseheight), Image.LANCZOS)
            return userImages, -58
            # квадратное 
            pass
        elif x > y:
            baseheight = 787
            hpercent = (baseheight / float (y)) 
            wsize = int ((float (x) * float (hpercent)))
            userImages = userImages.resize ((wsize, baseheight), Image.LANCZOS)
            return userImages, int(271 -userImages.size[0]/2)
        else:
            basewidth = 575
            wpercent = (basewidth / float(userImages.size[0]))
            hsize = int((float(userImages.size[1]) * float(wpercent)))
            if hsize < 787:
                baseheight = 787
                hpercent = (baseheight / float (y)) 
                wsize = int ((float (x) * float (hpercent)))
                userImages = userImages.resize ((wsize, baseheight), Image.LANCZOS)
                return userImages, int(271 -userImages.size[0]/2)
            userImages = userImages.resize((basewidth, hsize), Image.LANCZOS)
            return userImages, 0
            # вертикальное
        
    elif teample == 2:
        x,y = userImages.size
        if max(x, y) / min(x, y) < 1.1:
            baseheight = 1047
            hpercent = (baseheight / float (y)) 
            wsize = int ((float (x) * float (hpercent)))
            userImages = userImages.resize ((wsize, baseheight), Image.LANCZOS)
            return userImages, 537, 0
            # квадратное 
            pass
        elif x > y:

            baseheight = 1047
            hpercent = (baseheight / float (y)) 
            wsize = int ((float (x) * float (hpercent)))
            userImages = userImages.resize ((wsize, baseheight), Image.LANCZOS)
            return userImages, int(972 -userImages.size[0]/2), 1
        else:
            basewidth = 1029
            wpercent = (basewidth / float(userImages.size[0]))
            hsize = int((float(userImages.size[1]) * float(wpercent)))
            userImages = userImages.resize((basewidth, hsize), Image.LANCZOS)
            return userImages, 509,2
            # вертикальное
    elif teample == 4:
        x,y = userImages.size
        if max(x, y) / min(x, y) < 1.1:
            basewidth = 647
            wpercent = (basewidth / float(userImages.size[0]))
            hsize = int((float(userImages.size[1]) * float(wpercent)))
            userImages = userImages.resize((basewidth, hsize), Image.LANCZOS)
            return userImages, int(194-userImages.size[0]/2)
            # квадратное 
            pass
        elif x > y:
            baseheight = 621
            hpercent = (baseheight / float (y)) 
            wsize = int ((float (x) * float (hpercent)))
            userImages = userImages.resize ((wsize, baseheight), Image.LANCZOS)
            return userImages, int(194 -userImages.size[0]/2)
        else:
            basewidth = 388
            wpercent = (basewidth / float(userImages.size[0]))
            hsize = int((float(userImages.size[1]) * float(wpercent)))
            if hsize < 618:
                baseheight = 621
                hpercent = (baseheight / float (y)) 
                wsize = int ((float (x) * float (hpercent)))
                userImages = userImages.resize ((wsize, baseheight), Image.LANCZOS)
                return userImages, int(194 -userImages.size[0]/2)
            userImages = userImages.resize((basewidth, hsize), Image.LANCZOS)
            return userImages, 0
            # вертикальное
    else:
        x,y = userImages.size
        if max(x, y) / min(x, y) < 1.1:
            baseheight = 802
            hpercent = (baseheight / float (y)) 
            wsize = int ((float (x) * float (hpercent)))
            userImages = userImages.resize ((wsize, baseheight), Image.LANCZOS)
            return userImages, (0,0), 1
            # квадратное '''
        elif x > y:
            baseheight = 802
            hpercent = (baseheight / float (y)) 
            wsize = int ((float (x) * float (hpercent)))
            userImages = userImages.resize ((wsize, baseheight), Image.LANCZOS)
            return userImages, (int(300  -userImages.size[0]/2),0), 1
        else:
            basewidth = 645
            wpercent = (basewidth / float(userImages.size[0]))
            hsize = int((float(userImages.size[1]) * float(wpercent)))
            userImages = userImages.resize((basewidth, hsize), Image.LANCZOS)
            if hsize < 802:
                baseheight = 802
                hpercent = (baseheight / float (y)) 
                wsize = int ((float (x) * float (hpercent)))
                userImages = userImages.resize ((wsize, baseheight), Image.LANCZOS)
                return userImages, (int(300  -userImages.size[0]/2),0), 2
            return userImages, (0,0), 2


def openImageElement(element,teample = 1):
    if teample == 1:
        if element == "Fire":
            return Image.open(f'{path}/teapmleOne/background/PYRO.png').convert("RGBA")
        elif element== "Grass":
            return Image.open(f'{path}/teapmleOne/background/DENDRO.png').convert("RGBA")
        elif element == "Electric":
            return Image.open(f'{path}/teapmleOne/background/ELECTRO.png').convert("RGBA")
        elif element == "Water":
            return Image.open(f'{path}/teapmleOne/background/GYDRO.png').convert("RGBA")
        elif element == "Wind":
            return Image.open(f'{path}/teapmleOne/background/ANEMO.png').convert("RGBA")
        elif element== "Rock":
            return Image.open(f'{path}/teapmleOne/background/GEO.png').convert("RGBA")
        elif element == "Ice":
            return Image.open(f'{path}/teapmleOne/background/CRYO.png').convert("RGBA")
        else:
            return Image.open(f'{path}/teapmleOne/background/ERROR.png').convert("RGBA")
    elif teample == 2:
        if element == "Fire":
            return Image.open(f'{path}/teapmleTwo/background/PYRO.png').convert("RGBA")
        elif element== "Grass":
            return Image.open(f'{path}/teapmleTwo/background/DENDRO.png').convert("RGBA")
        elif element == "Electric":
            return Image.open(f'{path}/teapmleTwo/background/ELECTRO.png').convert("RGBA")
        elif element == "Water":
            return Image.open(f'{path}/teapmleTwo/background/GYDRO.png').convert("RGBA")
        elif element == "Wind":
            return Image.open(f'{path}/teapmleTwo/background/ANEMO.png').convert("RGBA")
        elif element== "Rock":
            return Image.open(f'{path}/teapmleTwo/background/GEO.png').convert("RGBA")
        elif element == "Ice":
            return Image.open(f'{path}/teapmleTwo/background/CRYO.png').convert("RGBA")
        else:
            return Image.open(f'{path}/teapmleTwo/background/ERROR.png').convert("RGBA")
    else:
        if element == "Fire":
            return Image.open(f'{path}/teapmleTree/background/PYRO.png').convert("RGBA")
        elif element== "Grass":
            return Image.open(f'{path}/teapmleTree/background/DENDRO.png').convert("RGBA")
        elif element == "Electric":
            return Image.open(f'{path}/teapmleTree/background/ELECTRO.png').convert("RGBA")
        elif element == "Water":
            return Image.open(f'{path}/teapmleTree/background/GYDRO.png').convert("RGBA")
        elif element == "Wind":
            return Image.open(f'{path}/teapmleTree/background/ANEMO.png').convert("RGBA")
        elif element== "Rock":
            return Image.open(f'{path}/teapmleTree/background/GEO.png').convert("RGBA")
        elif element == "Ice":
            return Image.open(f'{path}/teapmleTree/background/CRYO.png').convert("RGBA")
        else:
            return Image.open(f'{path}/teapmleTree/background/ERROR.png').convert("RGBA")

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
    charter = charter.convert("RGBA")
    if teample == 1:
        bg = openImageElement(element)
        bgUP = bg.copy()
        bg.alpha_composite(charter,(-734,-134))
        im = Image.composite(bg, bgUP, openFile.MaskaBgTeampleOne.convert('L'))
        bg.alpha_composite(im,(0,0))
    elif teample == 2:
        bg = openImageElement(element, teample = 2)
        bgUP = bg.copy()
        bg.alpha_composite(charter,(0,0))
        im = Image.composite(bg, bgUP, openFile.MaskaSplas.convert('L').resize(bg.size))
        bg.alpha_composite(im,(0,0))
        bg.alpha_composite(openFile.MasskaEffectDown,(0,0))
    else:
        bg = openImageElement(element, teample = 3)
        bgUP = bg.copy()
        bg.alpha_composite(charter,(-810,-115))
        im = Image.composite(bg, bgUP, openFile.UserBgTeampleTree.convert('L'))
        bg.alpha_composite(im,(0,0))
        bg.alpha_composite(openFile.EffectBgTeampleTree,(0,0))
    return bg


def userImage(img,element = None, adaptation = False):
    userImagess,pozitionX = centryImage(img)
    if adaptation:
        grandient = userAdaptGrandient(userImagess.convert("RGB").copy())
        Effect = openFile.UserEffectTeampleOne.copy().convert('RGBA')
        grandient = ImageChops.soft_light(grandient,Effect)
        
        Effect.alpha_composite(userImagess,(pozitionX,0))
        im = Image.composite(Effect, grandient, openFile.MaskaUserBg2TeampleOne.convert("L"))
        return im
    else:
        try:
            bg = openImageElement(element)
            effect = bg.copy()
        except Exception as e:
            print(e)

        bg.alpha_composite(userImagess,(pozitionX,0))
        im = Image.composite(bg, effect, openFile.MaskaUserBg2TeampleOne.convert("L"))
        bg.alpha_composite(im,(0,0))
        return bg

def userImageTree(img,element = None, adaptation = False):
    userImagess,pozitionX,types = centryImage(img, teample = 3)
    if adaptation:
        grandient = userAdaptGrandient(userImagess.convert("RGB").copy(), size =(1924,802))
        Effect = openFile.EffectBgTree.copy().convert("RGBA")
        grandient = ImageChops.soft_light(grandient,Effect)
        Effect.alpha_composite(userImagess,pozitionX)
        if types == 2:
            im = Image.composite(Effect, grandient, openFile.USER_BG_IMG_VERT.convert("L"))
        else:
            im = Image.composite(Effect, grandient, openFile.UserBgTeampleImgTree.convert("L"))
        
        im.alpha_composite(openFile.EffectBgTeampleTree,(0,0))
        return im
    else:
        bg = openImageElement(element, teample = 3)
        effect = bg.copy()
        bg.alpha_composite(userImagess,(pozitionX,0))
        im = Image.composite(bg, effect, openFile.UserBgTeampleImgTree.convert("L"))
        bg.alpha_composite(im,(0,0))
        bg.alpha_composite(openFile.EffectBgTeampleTree.convert("RGBA"),(0,0))
        return bg


def userImageTwo(img,element = None, adaptation = False):
    userImagess,pozitionX,types = centryImage(img, teample = 2)
    if adaptation:
        bg = openImageElement("error", teample = 2)
        grandientLeft = userAdaptGrandient(userImagess.convert("RGB").copy(), size = (1038, 1048),left = True)
        grandientRight = userAdaptGrandient(userImagess.convert("RGB").copy(), size = (937, 1048))
        bg.alpha_composite(grandientLeft,(0,0))
        bg.alpha_composite(grandientRight,(grandientLeft.size[0],0))
        Effect = openFile.UserEffectTeampleTwo.copy().convert("RGBA")
        grandient = ImageChops.soft_light(bg,Effect)
        Effect.alpha_composite(userImagess,(pozitionX,0))
        if types == 0:
            im = Image.composite(Effect, grandient, openFile.UserBgTeampleTwo.convert("L"))
        elif types == 1:
            im = Image.composite(Effect, grandient, openFile.MaskaArt_TWO_TREE.convert("L"))
        else:
            im = Image.composite(Effect, grandient, openFile.MaskaArt_TWO.convert("L"))
        return im
    else:
        bg = openImageElement(element, teample = 2)
        effect = bg.copy()
        bg.alpha_composite(userImagess,(pozitionX,0))
        im = Image.composite(bg, effect, openFile.UserBgTeampleTwo.convert("L"))
        bg.alpha_composite(im,(0,0))
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

def getIconAdd(x, icon = False, size = None, element = False):
    elements = False
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
        if not element:
            icons = Image.open(f'{path}/icon/ELECTRO.png')
        else:
            icons = Image.open(f'{path}/icon/ELECTRO_UP.png').resize(())
    elif x == "FIGHT_PROP_DEFENSE_PERCENT":
        icons = Image.open(f'{path}/icon/DEFENSE_PERCENT.png')
    elif x == "FIGHT_PROP_ATTACK_PERCENT":
        icons = Image.open(f'{path}/icon/ATTACK_PERCENT.png')
    elif x == "FIGHT_PROP_HP_PERCENT":
        icons = Image.open(f'{path}/icon/HP_PERCENT.png')
    elif x == "FIGHT_PROP_WATER_ADD_HURT":
        if not element:
            icons = Image.open(f'{path}/icon/HYDRO.png')
        else:
            icons = Image.open(f'{path}/icon/HYDRO_UP.png')
    elif x == "FIGHT_PROP_WIND_ADD_HURT":
        if not element:
            icons = Image.open(f'{path}/icon/ANEMO.png')
        else:
            icons = Image.open(f'{path}/icon/ANEMO_UP.png')
    elif x == "FIGHT_PROP_ICE_ADD_HURT":
        if not element:
            icons = Image.open(f'{path}/icon/CRYO.png')
        else:
            icons = Image.open(f'{path}/icon/CRYO_UP.png')
    elif x == "FIGHT_PROP_ROCK_ADD_HURT":
        if not element:
            icons = Image.open(f'{path}/icon/GEO.png')
        else:
            icons = Image.open(f'{path}/icon/GEO_UP.png')
    elif x == "FIGHT_PROP_FIRE_ADD_HURT":
        if not element:
            icons = Image.open(f'{path}/icon/PYRO.png')
        else:
            icons = Image.open(f'{path}/icon/PYRO_UP.png')
    elif x == "FIGHT_PROP_GRASS_ADD_HURT":
        if not element:
            icons = Image.open(f'{path}/icon/DENDRO.png')
        else:
            icons = Image.open(f'{path}/icon/DENDRO_UP.png')
    elif x == "FIGHT_PROP_HEAL_ADD":
        icons = Image.open(f'{path}/icon/HEALED_ADD.png')
    elif x == "FIGHT_PROP_HEAL":
        icons = Image.open(f'{path}/icon/HEAL.png')
    elif x == "FIGHT_PROP_PHYSICAL_ADD_HURT":
        icons = Image.open(f'{path}/icon/PHYSICAL_ADD_HURT.png')
    else:
        return False
    if size:
        icons.thumbnail(size)
        return icons.convert("RGBA").copy()
    else:
        return icons.convert("RGBA").copy()


def centrFive(userImages):
    x,y = userImages.size
    if max(x, y) / min(x, y) < 1.1:
        baseheight = 997
        hpercent = (baseheight / float (y)) 
        wsize = int ((float (x) * float (hpercent)))
        userImages = userImages.resize ((wsize, baseheight), Image.LANCZOS)
        return userImages, (818,0), 1
        # квадратное 
        pass
    elif x > y:
        basewidth = 2605
        wpercent = (basewidth / float(userImages.size[0]))
        hsize = int((float(userImages.size[1]) * float(wpercent)))
        if hsize > 1690:
            baseheight = 997
            hpercent = (baseheight / float (y)) 
            wsize = int ((float (x) * float (hpercent)))
            userImages = userImages.resize ((wsize, baseheight), Image.LANCZOS)
            return userImages, (818,0), 1
        userImages = userImages.resize((basewidth, hsize), Image.LANCZOS)
        return userImages, (0,0), 0
        '''
        baseheight = 1453
        hpercent = (baseheight / float (y)) 
        wsize = int ((float (x) * float (hpercent)))
        print(wsize)
        if wsize < 2605:
            baseheight = 997
            hpercent = (baseheight / float (y)) 
            wsize = int ((float (x) * float (hpercent)))
            userImages = userImages.resize ((wsize, baseheight), Image.LANCZOS)
            return userImages, (818,0), 1
        userImages = userImages.resize ((wsize, baseheight), Image.LANCZOS)
        return userImages, (0,-131), 0'''
    else:
        basewidth = 1087
        wpercent = (basewidth / float(userImages.size[0]))
        hsize = int((float(userImages.size[1]) * float(wpercent)))
        userImages = userImages.resize((basewidth, hsize), Image.LANCZOS)
        return userImages, (759,-61), 2

def openBgElementFive(element):
    if element == "Fire":
        return openFile.PYROTeampleFive
    elif element== "Grass":
        return openFile.DENDROTeampleFive
    elif element == "Electric":
        return openFile.ELECTROTeampleFive
    elif element == "Water":
        return openFile.GYDROTeampleFive
    elif element == "Wind":
        return openFile.ANEMOTeampleFive
    elif element== "Rock":
        return openFile.GEOTeampleFive
    else:
        return openFile.CRYOTeampleFive



async def creatFiveBg(userImages,element = "Rock",adapt = False):
    if adapt:
        img, px, format = centrFive(userImages)
        if format == 0:
            bg = openBgElementFive(element).copy().convert("RGBA")
            bg.alpha_composite(img,px)
            imgBlur = img.filter(ImageFilter.GaussianBlur(radius=15)).resize((2605,997)).convert("RGBA")
            bg = Image.composite(bg, imgBlur, openFile.MASKA_ADAPT_WIDTH.convert("L"))
        elif format == 1:
            bg = openBgElementFive(element).copy().convert("RGBA")
            grandientLeft = userAdaptGrandient(img.convert("RGB").copy(), size = (1302, 997),left = True)
            grandientRight = userAdaptGrandient(img.convert("RGB").copy(), size = (1302, 997))
            bg.alpha_composite(grandientLeft,(0,0))
            bg.alpha_composite(grandientRight,(1303,0))
            Effect = openFile.STARS_BG.copy().convert("RGBA")
            grandient = ImageChops.soft_light(bg,Effect)
            Effect.alpha_composite(img,px)
            bg = Image.composite(Effect, grandient, openFile.MASKA_ADAPT_HEIGHT_TWO.convert("L"))
        else:
            bg = openBgElementFive(element).copy().convert("RGBA")
            grandientLeft = userAdaptGrandient(img.convert("RGB").copy(), size = (1302, 997),left = True)
            grandientRight = userAdaptGrandient(img.convert("RGB").copy(), size = (1302, 997))
            bg.alpha_composite(grandientLeft,(0,0))
            bg.alpha_composite(grandientRight,(1303,0))
            Effect = openFile.STARS_BG.copy().convert("RGBA")
            grandient = ImageChops.soft_light(bg,Effect)
            Effect.alpha_composite(img,px)
            bg = Image.composite(Effect, grandient, openFile.MASKA_ADAPT_HEIGHT.convert("L"))
    else:
        bg = openBgElementFive(element).copy().convert("RGBA")
        effect = bg.copy()
        bg.alpha_composite(userImages,(0,-122))
        bg = Image.composite(bg, effect, openFile.MASKA_ADAPT_SPLASH.convert("L"))
    bg.alpha_composite(openFile.SHADOW_TEAMPLEfive,(0,540))
    return bg


async def openBgElementSeven(element):
    if element == "Fire":
        return openFile.PYRO_SEVEN
    elif element== "Grass":
        return openFile.DENDRO_SEVEN
    elif element == "Electric":
        return openFile.ELECTRO_SEVEN
    elif element == "Water":
        return openFile.GYDRO_SEVEN
    elif element == "Wind":
        return openFile.ANEMO_SEVEN
    elif element== "Rock":
        return openFile.GEO_SEVEN
    else:
        return openFile.CRYO_SEVEN

async def centerSeven(userImages):
    x,y = userImages.size
    if max(x, y) / min(x, y) < 1.1:
        baseheight = 734
        hpercent = (baseheight / float (y)) 
        wsize = int ((float (x) * float (hpercent)))
        userImages = userImages.resize ((wsize, baseheight), Image.LANCZOS)
        return userImages, (108,-50)
        # квадратное 
        pass
    elif x > y:
        basewidth = 940 
        wpercent = (basewidth / float(userImages.size[0]))
        hsize = int((float(userImages.size[1]) * float(wpercent)))
        if hsize > 1690:
            baseheight = 734
            hpercent = (baseheight / float (y)) 
            wsize = int ((float (x) * float (hpercent)))
            userImages = userImages.resize ((wsize, baseheight), Image.LANCZOS)
            return userImages, (108,-50)
        userImages = userImages.resize((basewidth, hsize), Image.LANCZOS)
        return userImages, (0,0)
    else:
        basewidth = 734
        wpercent = (basewidth / float(userImages.size[0]))
        hsize = int((float(userImages.size[1]) * float(wpercent)))
        userImages = userImages.resize((basewidth, hsize), Image.LANCZOS)
        return userImages, (108,-50)


async def creatSevenBg(userImages,element = "Rock",adapt = False):
    if adapt:
        img, px = await centerSeven(userImages)
        color = await colorBg(img)
        bgA = Image.new("RGBA",(940,1010) ,color)
        bg = bgA.copy()
        bgA.alpha_composite(img,px)
        bg = Image.composite(bg, bgA, openFile.MASKA_ADAPT.convert("L"))

        bg = ImageChops.soft_light(bg,openFile.overlay_SEVEN.convert("RGBA"))        
    else:
        bgA = await openBgElementSeven(element)
        bgA = bgA.copy().convert("RGBA")
        bg = bgA.copy()
        bgA.alpha_composite(userImages,(-224,-97))
        bg = Image.composite(bg, bgA, openFile.MASKA_SPLASH.convert("L"))
    bg.alpha_composite(openFile.SHADOW_SEVEN,(0,0))
    bg.alpha_composite(openFile.FRAME_SEVEN,(0,0))    
    return bg

        



async def charterElement(element):
    if element == "Fire":
        return openFile.PYROTeampleFiveElement
    elif element== "Grass":
        return openFile.DENDROTeampleFiveElement
    elif element == "Electric":
        return openFile.ELECTROTeampleFiveElement
    elif element == "Water":
        return openFile.GYDROTeampleFiveElement
    elif element == "Wind":
        return openFile.ANEMOTeampleFiveElement
    elif element== "Rock":
        return openFile.GEOTeampleFiveElement
    else:
        return openFile.CRYOTeampleFiveElement

async def starFive(x,weapon = True):
    if weapon:
        if x == 1:
            return openFile.stars_light1
        elif x == 2:
            return openFile.stars_light2
        elif x == 3:
            return openFile.stars_light3
        elif x == 4:
            return openFile.stars_light4
        elif x == 5:
            return openFile.stars_light5
    else:
        if x == 1:
            return openFile.stars_frame1
        elif x == 2:
            return openFile.stars_frame2
        elif x == 3:
            return openFile.stars_frame3
        elif x == 4:
            return openFile.stars_frame4
        elif x == 5:
            return openFile.stars_frame5