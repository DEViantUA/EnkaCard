# Copyright 2022 DEViantUa <t.me/deviant_ua>
# All rights reserved.
__all__ = ["weaponAdd", 
    "nameBanner", 
    "stats",
    "constant", 
    "create_picture", 
    "talants",
    "naborArtifact", 
    "artifacAdd", 
    "addConst",
    "addTallants", 
    "addArtifact", 
    "signature",
    "appedFrame",
    "openUserImg" 
    ]

from PIL import ImageDraw
from .Generation import * 
from .FunctionsPill import PillImg
import math
import re
import os
from .options import *
from . import openFile

try:
    os.path.dirname(__file__).split("\enkanetworkcard")[0]
    path = os.path.dirname(__file__).split("\enkanetworkcard")[0]
except:
    try:
        os.path.dirname(__file__).split("/enkanetworkcard")[0]
        path = os.path.dirname(__file__).split("/enkanetworkcard")[0]
    except:
        pass



def openUserImg(img):
    if type(img) != str:
        img = img
    elif type(img) == str:
        linkImg = re.search("(?P<url>https?://[^\s]+)", img)
        if linkImg:
            img = PillImg(link=linkImg.group()).imgD()
        else:
            img = Image.open(f'{path}/{img}')
    else:
        return None
    return img.convert("RGBA")
    
    
def weaponAdd(characters,lvlName):
    if characters.detail.artifact_name_set != "":
        return None
    WeaponBg = openFile.WeaponBgTeampleOne.copy()
    WeaponBgUp = openFile.WeaponBgUpTeampleOne.copy()
    proc = False    
    d = ImageDraw.Draw(WeaponBg)
    name = characters.detail.name
    lvl = characters.level
    lvlUp = characters.refinement
    baseAtt = characters.detail.mainstats.value
    imageStats = None
    dopStat = 0
    for substate in characters.detail.substats:
        imageStats = getIconAdd(substate.prop_id, icon = True, size = (26,26))
        if not imageStats:
            continue
        dopStat = substate.value
        if str(substate.type) == "DigitType.PERCENT":
            proc = True
    if imageStats:
        WeaponBg.paste(imageStats,(300,53),imageStats)
    
    stars = star(characters.detail.rarity)
    image = PillImg(characters.detail.icon.url).imagSize(size = (114,121))
    WeaponBg.paste(image,(0,0),image)
    WeaponBg.paste(WeaponBgUp,(0,0),WeaponBgUp)
    position,font = PillImg().centrText(name, witshRam = 315, razmer = 24, start = 159, Yram = 30, y = 13)
    d.text(position, str(name), font= font, fill=coloring) 
    d.text((435 ,53), f"R{lvlUp}", font= t24, fill=(248,199,135,255)) 
    position,font = PillImg().centrText(f"{lvlName}: {lvl}/90", witshRam = 152, razmer = 17, start = 235, Yram = 28, y = 90)
    d.text(position, f"{lvlName}: {lvl}/90", font= font, fill=coloring) 

    position,font = PillImg().centrText(baseAtt, witshRam = 90, razmer = 24, start = 180, Yram = 30, y = 50)    
    d.text(position, str(baseAtt), font= font, fill=coloring)
    if proc:
        position,font = PillImg().centrText(f'{dopStat}%', witshRam = 90, razmer = 24, start = 320, Yram = 30, y = 50)
        d.text(position, f'{dopStat}%', font= font, fill=coloring)
    else:
        position,font = PillImg().centrText(str(dopStat), witshRam = 90, razmer = 24, start = 320, Yram = 30, y = 50)
        d.text(position, str(dopStat), font= font, fill=coloring) 
    WeaponBg.paste(stars,(0,0),stars)
    
    return WeaponBg

def nameBanner(characters,assets,lvlName):
    NameBg = openFile.NameBgTeampleOne.copy()
    d = ImageDraw.Draw(NameBg)
    centrName,fonts = PillImg().centrText(characters.name, witshRam = 220, razmer = 33,start = 2)
    d.text((centrName,28), characters.name, font = fonts, fill=coloring) 
    d.text((187,-1), str(characters.friendship_level), font = t24, fill= coloring) 
    centrName,fonts = PillImg().centrText(f"{lvlName}: {characters.level}/90", witshRam = 148, razmer = 17, start = 5)
    d.text((centrName,2), f"{lvlName}: {characters.level}/90", font = fonts, fill= coloring) 
    person = assets.character(characters.id)
    stars = star(person.rarity)
    NameBg.paste(stars,(63,68),stars)

    return NameBg



def stats(characters,assets):
    postion = (26,37)
    AttributeBg = openFile.AttributeBgTeampleOne.copy()
    g = characters.stats
    dopVal = {}
    cout = 0
    for key in g:
        if key[0] in ["BASE_HP","FIGHT_PROP_BASE_ATTACK","FIGHT_PROP_BASE_DEFENSE"]:
            if not key[0] in dopVal:
                dopVal[key[0]] = int(key[1].value)
                cout += 1
                if cout == 3:
                    break
    for key in reversed(list(g)):
        Attribute = openFile.AttributeTeampleOne.copy()
        d = ImageDraw.Draw(Attribute)
        if key[1].value == 0:
            continue
        txt = assets.get_hash_map(key[0])
        
        iconImg = getIconAdd(key[0])
        if not iconImg:
            continue
        icon = PillImg(image = iconImg).imagSize(fixed_width = 23)

        Attribute.paste(icon, (4,0),icon)

        if not key[1].id in stat_perc:
            value = str(math.ceil(key[1].value))
        else:
            value = f"{round(key[1].value * 100, 1)}%"
        pX,fnt = PillImg().centrText(value, witshRam = 119, razmer = 20, start = 325)
        d.text((pX,3), value, font = fnt, fill=coloring)

        d.text((42,4), str(txt), font = t18, fill=coloring)

        AttributeBg.paste(Attribute,(postion[0],postion[1]),Attribute)
        dopValueBg = AttributeDopValueTeampleOne.copy()
        dv = ImageDraw.Draw(dopValueBg)
        if key[0] in dopStatAtribute:
            dopStatVal  = dopVal[dopStatAtribute[key[0]]]
            dopStatValArtifact = int(key[1].value - dopStatVal)
            if dopStatValArtifact != 0:
                pX,fnt = PillImg().centrText(f"{dopStatVal} + {dopStatValArtifact}", witshRam = 113, razmer = 13, start = 0)
                dv.text((pX,-1),f"{dopStatVal} + {dopStatValArtifact}", font = fnt, fill=(248,199,135))
                AttributeBg.paste(dopValueBg,(354,postion[1]+27),dopValueBg)

        postion = (postion[0],postion[1]+39)

    return AttributeBg

def constant(characters,assets):
    person = assets.character(characters.id)
    constantRes = []  
    for key in characters.constellations:
        closeConstBg = ClossedBg.copy()
        closeConsticon = Clossed.copy()
        openConstBg = openImageElementConstant(person.element.value)  
        imageIcon = PillImg(key.icon.url).imgD().resize((43,48))
        if not key.unlocked:
            closeConstBg.paste(imageIcon, (19,20),imageIcon)
            closeConstBg.paste(closeConsticon, (0,0),closeConsticon)
            const = closeConstBg
        else:
            openConstBg.paste(imageIcon, (19,20),imageIcon)
            const = openConstBg
        constantRes.append(const)
    
    return constantRes

def create_picture(assets,id,imgs,adapt,splash = None):
    person = assets.character(id)
    if imgs:
        frame = userImage(imgs, element = person.element.value, adaptation = adapt)
    else:
        if splash:
            banner = PillImg(link = splash).imagSize(size = (2048,1024))
        else:
            banner = PillImg(link = person.images.banner.url).imagSize(size = (2048,1024))
        frame = maskaAdd(person.element.value,banner)
    return frame.copy()

def talants(characters):
    count = 0
    tallantsRes = []
    for key in characters.skills:
        if key.level > 9:
            talantsBg = TalantsFrameGoldLvlTeampleOne.copy()
        else:
            talantsBg = TalantsFrameTeampleOne.copy()
        talantsCount = TalantsCountTeampleOne.copy()
        d = ImageDraw.Draw(talantsCount)
        imagesIconTalants = PillImg(link = key.icon.url).imgD().resize((50,50))
        talantsBg.paste(imagesIconTalants, (8,7),imagesIconTalants)
        talantsBg.paste(imagesIconTalants, (8,7),imagesIconTalants)
        px,fnt = PillImg().centrText(key.level, witshRam = 25, razmer = 17, start = 3, Yram = 16, y = -1) 
        d.text(px, str(key.level), font = fnt, fill=(248,199,135,255))
        talantsBg.paste(talantsCount, (19,53),talantsCount)
        tallantsRes.append(talantsBg)
        count+=1
        if count == 3:
            break

    return tallantsRes

def naborArtifact(info):
    ArtifactNameBg = openFile.ArtifactNameBgTeampleOne.copy()
    naborAll = []
    for key in info:
        if info[key] > 1:
            ArtifactNameFrame = openFile.ArtifactNameFrameTeampleOne.copy()
            d = ImageDraw.Draw(ArtifactNameFrame)
            centrName,fonts = PillImg().centrText(key, witshRam = 240, razmer = 15, start = 4, Yram = 24, y = 1) 
            d.text(centrName, str(key), font= fonts, fill=coloring)
            d.text((267,-2), str(info[key]), font= t24, fill=coloring)
            naborAll.append(ArtifactNameFrame)
    position = (151,34)
    for key in naborAll:
        if len(naborAll) == 1:
            ArtifactNameBg.paste(key,(151,54),key)
        else:
            ArtifactNameBg.paste(key,position,key)
            position = (position[0],position[1]+29)

    return ArtifactNameBg

def artifacAdd(characters):
    ArtifactBgUp = openFile.ArtifactBgUpTeampleOne.copy()
    
    listArt = {}
    artifacRes = []
    for key in characters.equipments:
        ArtifactBg = openFile.ArtifactBgTeampleOne.copy()
        if key.detail.artifact_name_set == "":
            continue
        if not key.detail.artifact_name_set in listArt:
            listArt[key.detail.artifact_name_set] = 1
        else:
            listArt[key.detail.artifact_name_set] += 1

        artimg = PillImg(key.detail.icon.url).imagSize(size = (175,175))
        ArtifactBg.paste(artimg,(-32,-27),artimg)
        ArtifactBg.paste(ArtifactBgUp,(0,0),ArtifactBgUp)
        d = ImageDraw.Draw(ArtifactBg)
        if str(key.detail.mainstats.type) == "DigitType.PERCENT":
            val = f"{key.detail.mainstats.value}%"
        else:
            val = key.detail.mainstats.value
        centrName,fonts = PillImg().centrText(val, witshRam = 52, razmer = 17, start = 65)
        d.text((centrName,62), str(val), font= fonts, fill=coloring)
        imageStats = getIconAdd(key.detail.mainstats.prop_id, icon = True, size = (19,24))
        if not imageStats:
            continue
        ArtifactBg.paste(imageStats,(3,0),imageStats)
        d.text((77,82), str(key.level), font= t17, fill=coloring)
        starsImg = star(key.detail.rarity)
        ArtifactBg.paste(starsImg,(16,96),starsImg)

        cs = 0
        positions = (159,8)
        for key in key.detail.substats:
            ArtifactDopStat = openFile.ArtifactDopValueTeampleOne.copy()
            v = f"+{key.value}"
            if str(key.type) == "DigitType.PERCENT":
                v = f"{v}%"
            imageStats = getIconAdd(key.prop_id, icon = True)
            if not imageStats:
                continue
            imageStats= PillImg(image = imageStats).imagSize(fixed_width = 17) 
            ArtifactDopStat.paste(imageStats,(3,1),imageStats)
            px,fnt = PillImg().centrText(v, witshRam = 142, razmer = 24, start = 33, Yram = 23, y = 1) 
            d = ImageDraw.Draw(ArtifactDopStat)
            d.text((px[0],px[1]-3), v, font= fnt, fill=coloring)
            cs += 1
            ArtifactBg.paste(ArtifactDopStat,(positions),ArtifactDopStat)
            positions = (positions[0],positions[1]+28)
        
        artifacRes.append(ArtifactBg)
    
    return artifacRes, naborArtifact(listArt)

def addConst(frameConst,constantRes):
    position = (2,157)
    for key in constantRes:
        frameConst.paste(key ,(position[0],position[1]),key)
        position = (position[0],position[1]+84)

    return frameConst

def addTallants(frameTallants,talatsRes):
    position = (530,342)
    for key in talatsRes:
        frameTallants.paste(key ,(position[0],position[1]),key)
        position = (position[0],position[1]+95)

    return frameTallants

def addArtifact(frameArtifact,artifacRes):
    position = (1141 ,42)
    for key in artifacRes:
        frameArtifact.paste(key ,(position[0],position[1]),key)
        position = (position[0],position[1]+143)
    return frameArtifact

def signature(hide,uid):
    SignatureText = openFile.SignatureOne.copy()
    d = ImageDraw.Draw(SignatureText)

    if not hide:
        d.text((440,7), str(uid), font= t18, fill=coloring)
    else:
        d.text((440,7), "Hidden", font= t18, fill=coloring)

    return SignatureText
    
def appedFrame(frame,weaponRes,nameRes,statRes,constantRes,talatsRes,artifacRes,artifactSet,signatureRes):
    banner = addConst(frame,constantRes) 
    banner = addTallants(banner,talatsRes)
    banner = addArtifact(banner,artifacRes)
    banner.paste(weaponRes ,(610,39),weaponRes )
    banner.paste(nameRes ,(138,646),nameRes )
    banner.paste(statRes ,(610,189),statRes)
    banner.paste(artifactSet ,(610,617),artifactSet)
    banner.paste(signatureRes ,(910,747),signatureRes)

    return banner


def generationOne(characters,assets,img,adapt,signatureRes,lvl,splash):
    try:
        if splash:
            frame = create_picture(assets,characters.id,img,adapt,characters.image.banner.url)
        else:
            frame = create_picture(assets,characters.id,img,adapt)
        weaponRes = weaponAdd(characters.equipments[-1],lvl)
        nameRes = nameBanner(characters,assets,lvl) 
        statRes = stats(characters,assets)
        constantRes = constant(characters,assets)
        talatsRes = talants(characters)
        artifacRes, artifactSet = artifacAdd(characters)
        result = appedFrame(frame,weaponRes,nameRes,statRes,constantRes,talatsRes,artifacRes,artifactSet,signatureRes)
        return result
    except Exception as e:
        print(f"Error: {e}")