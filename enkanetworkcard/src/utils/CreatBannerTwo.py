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
    ]

import math,asyncio
from PIL import ImageDraw
from .Generation import * 
from .FunctionsPill import centrText,imgD,imagSize
from .options import *
from . import openFile

async def create_picture(person,element,imgs,adapt,splash = None):
    if imgs:
        frame = userImageTwo(imgs, element = element, adaptation = adapt)
    else:
        if splash:
            banner = await imagSize(link = splash,size = (1974,1048))
        else:
            banner = await imagSize(link = person.images.banner.url, size = (1974,1048))
        frame = maskaAdd(element, banner, teample = 2)
    return frame


async def weaponAdd(characters,lvlName):
    if characters.detail.artifact_name_set != "":
        return None
    WeaponBg = openFile.WeaponBgTeampleTwo.copy()
    proc = False    
    d = ImageDraw.Draw(WeaponBg)
    name = characters.detail.name
    lvl = characters.level
    lvlUp = characters.refinement
    baseAtt = characters.detail.mainstats.value
    imageStats = None
    dopStat = 0
    for substate in characters.detail.substats:
        imageStats = getIconAdd(substate.prop_id, icon = True, size = (31,31))
        if not imageStats:
            continue
        dopStat = substate.value
        if str(substate.type) == "DigitType.PERCENT":
            proc = True
    if imageStats:
        WeaponBg.alpha_composite(imageStats,(330,59))
    
    stars = star(characters.detail.rarity)
    image = await imagSize(link = characters.detail.icon.url, size = (131,138))
    WeaponBg.alpha_composite(image,(20,11))
    position,font = await centrText(name, witshRam = 290, razmer = 24, start = 177, Yram = 38, y = 17)
    d.text(position, str(name), font= font, fill=coloring) 
    d.text((195 ,111), str(lvlUp), font= fontSize(24), fill=(248,199,135,255)) 
    position,font = await centrText(f"{lvlName['lvl']}: {lvl}/90", witshRam = 211, razmer = 24, start = 251, Yram = 38, y = 107)
    d.text(position, f"{lvlName['lvl']}: {lvl}/90", font= font, fill=coloring) 

    position,font = await centrText(baseAtt, witshRam = 131, razmer = 24, start = 167, Yram = 38, y = 56)    
    d.text(position, str(baseAtt), font= font, fill=coloring)
    if proc:
        position,font = await centrText(f'{dopStat}%', witshRam = 131, razmer = 24, start = 333, Yram = 38, y = 56)
        d.text(position, f'{dopStat}%', font= font, fill=coloring)
    else:
        position,font = await centrText(str(dopStat), witshRam = 131, razmer = 24, start = 333, Yram = 38, y = 56)
        d.text(position, str(dopStat), font= font, fill=coloring) 
    WeaponBg.alpha_composite(stars,(10,135))
    return WeaponBg

async def nameBanner(characters,lvlName):
    NameBg = openFile.NameBgTeampleTwo.copy()
    d = ImageDraw.Draw(NameBg)
    centrName,fonts = await centrText(characters.name, witshRam = 244, razmer = 24,start = 19, Yram = 29, y = 0)
    d.text((centrName,0), characters.name, font = fonts, fill=coloring) 
    d.text((33,45), str(characters.friendship_level), font = fontSize(24), fill= coloring) 
    centrName,fonts = await centrText(f"{lvlName['lvl']}: {characters.level}/90", witshRam = 209, razmer = 24, start = 77)
    d.text((centrName,45), f"{lvlName['lvl']}: {characters.level}/90", font = fonts, fill= coloring) 
    return NameBg


def starsAdd(person):
    StarsBg = openFile.StarBg.copy()
    starsIcon = star(person.rarity)
    StarsBg.alpha_composite(starsIcon,(17,-1))
    
    return StarsBg

async def stats(characters,assets):
    postion = (15,10)
    AttributeBg = openFile.AttributeBgTeampleTwo.copy()
    g = characters.stats
    dopVal = {}
    elementUp = True
    сout = 0
    for key in g:
        if key[0] in ["BASE_HP","FIGHT_PROP_BASE_ATTACK","FIGHT_PROP_BASE_DEFENSE"]:
            if not key[0] in dopVal:
                dopVal[key[0]] = int(key[1].value)
        if key[1].id in [2000,2001,2002]:
            iconImg = getIconAdd(key[0])
            txt = assets.get_hash_map(key[0])
            Attribute = openFile.AttributeTeampleTwo.copy()
            d = ImageDraw.Draw(Attribute)
            icon = await imagSize(image = iconImg,fixed_width = 26)

            Attribute.alpha_composite(icon, (10,4))

            if not key[1].id in stat_perc:
                value = str(math.ceil(key[1].value))
            else:
                value = f"{round(key[1].value * 100, 1)}%"
            pX,fnt = await centrText(value, witshRam = 151, razmer = 24, start = 410)
            d.text((pX,7), value, font = fnt, fill=coloring)

            d.text((67,7), str(txt), font = fontSize(24), fill=coloring)

            AttributeBg.alpha_composite(Attribute,(postion[0],postion[1]))
            postion = (postion[0],postion[1]+55)
            сout += 1
            if сout == 3:
                break
    for key in g:
        if key[1].id in [40,41,42,43,44,45,46]:
            if elementUp:
                key = max((x for x in g if 40 <= x[1].id <= 46), key=lambda x: x[1].value)
                elementUp = False
            else:
                continue
        if key[1].value == 0 or key[1].id in [2000,2001,2002]:
            continue
        iconImg = getIconAdd(key[0])
        if not iconImg:
            continue
        txt = assets.get_hash_map(key[0])
        Attribute = openFile.AttributeTeampleTwo.copy()
        d = ImageDraw.Draw(Attribute)
        
        icon = await imagSize(image = iconImg,fixed_width = 26)

        Attribute.alpha_composite(icon, (10,4))

        if not key[1].id in stat_perc:
            value = str(math.ceil(key[1].value))
        else:
            value = f"{round(key[1].value * 100, 1)}%"
        pX,fnt = await centrText(value, witshRam = 151, razmer = 24, start = 410)
        d.text((pX,7), value, font = fnt, fill=coloring)

        d.text((67,7), str(txt), font = fontSize(24), fill=coloring)

        AttributeBg.alpha_composite(Attribute,(postion[0],postion[1]))
        postion = (postion[0],postion[1]+55)
    return AttributeBg
    
async def constant(characters):
    constantRes = []  
    for key in characters.constellations:
        closeConstBg = openFile.ClossedBg.copy()
        closeConsticon = openFile.Clossed.copy()
        openConstBg = openImageElementConstant(characters.element.value)
        imageIcon = await imgD(link = key.icon.url)
        imageIcon = imageIcon.resize((43,48))
        if not key.unlocked:
            closeConstBg.alpha_composite(imageIcon, (19,20))
            closeConstBg.alpha_composite(closeConsticon, (0,-2))
            const = closeConstBg
        else:
            openConstBg.alpha_composite(imageIcon, (19,20))
            const = openConstBg
        constantRes.append(const)
    
    return constantRes

async def talants(characters):
    tallantsRes = []
    for key in characters.skills:
        if key.level > 9:
            talantsBg = openFile.TalantsFrameGoldLvlTeampleTwo.copy()
        else:
            talantsBg = openFile.TalantsFrameTeampleTwo.copy()
        talantsCount = openFile.TalantsCountTeampleTwo.copy()
        d = ImageDraw.Draw(talantsCount)
        imagesIconTalants = await imgD(link = key.icon.url)
        imagesIconTalants = imagesIconTalants.resize((52,52))
        talantsBg.alpha_composite(imagesIconTalants, (7,6))
        if len(str(key.level)) == 2:
            d.text((3,2), str(key.level), font = fontSize(18), fill=(248,199,135,255))
        else:
            d.text((6,2), str(key.level), font = fontSize(18), fill=(248,199,135,255))
        talantsBg.alpha_composite(talantsCount, (20,47))
        tallantsRes.append(talantsBg)
    return tallantsRes

async def naborArtifact(info,ArtifactNameBg):
    naborAll = []
    for key in info:
        if info[key] > 1:
            ArtifactNameFrame = openFile.ArtifactNameFrameTeampleTwo.copy()
            d = ImageDraw.Draw(ArtifactNameFrame)
            centrName,fonts = await centrText(key, witshRam = 289, razmer = 24, start = 2, Yram = 28, y = 1) 
            d.text((centrName[0],0), str(key), font= fonts, fill=coloring)
            d.text((356,0), str(info[key]), font= fontSize(24), fill=coloring)
            naborAll.append(ArtifactNameFrame)
    position = (156,38)
    for key in naborAll:
        if len(naborAll) == 1:
            ArtifactNameBg.alpha_composite(key,(156,54))
        else:
            ArtifactNameBg.alpha_composite(key,position)
            position = (position[0],position[1]+34)

    return ArtifactNameBg


async def creatArtifact(infpart,imageStats):
    ArtifactBg = openFile.ArtifactBgTeampleTwo.copy()
    ArtifactUp = openFile.ArtifactBgUpTeampleTwo.copy()
    artimg = await imagSize(link = infpart.detail.icon.url,size = (120,107))
    ArtifactBg.alpha_composite(artimg,(-5,0))
    ArtifactBg.alpha_composite(ArtifactUp,(0,0))
    d = ImageDraw.Draw(ArtifactBg)
    if str(infpart.detail.mainstats.type) == "DigitType.PERCENT":
        val = f"{infpart.detail.mainstats.value}%"
    else:
        val = infpart.detail.mainstats.value
    centrName,fonts = await centrText(val, witshRam = 62, razmer = 17, start = 50)
    d.text((centrName,76), str(val), font= fonts, fill=coloring)
    
    ArtifactBg.alpha_composite(imageStats,(7,2))
    d.text((81,97), str(infpart.level), font= fontSize(17), fill=coloring)
    starsImg = star(infpart.detail.rarity).resize((77,22))
    ArtifactBg.alpha_composite(starsImg,(2,97))
    cs = 0
    positionIcon = (130,21)
    for key in infpart.detail.substats:
        ArtifactBgStat = openFile.ArtifactDopStatTeampleTwo.copy()
        d = ImageDraw.Draw(ArtifactBgStat)
        v = f"+{key.value}"
        if str(key.type) == "DigitType.PERCENT":
            v = f"{v}%"
        imageStats = getIconAdd(key.prop_id, icon = True)
        if not imageStats:
            continue
        imageStats= await imagSize(image = imageStats,fixed_width = 24) 
        ArtifactBgStat.alpha_composite(imageStats,(3,1))
        d.text((57,2), v, font= fontSize(24), fill=coloring)
        ArtifactBg.alpha_composite(ArtifactBgStat,positionIcon)
        cs += 1
        positionIcon = (positionIcon[0]+185,positionIcon[1])
        if cs == 2:
            positionIcon = (130,72)
    return ArtifactBg

async def artifacAdd(characters):
    count = 0
    listArt = {}
    artifacRes = []
    ArtifactNameBg = openFile.ArtifactNameBgTeampleTwo.copy()
    for key in characters.equipments:
        if key.detail.artifact_name_set == "":
            continue
        if not key.detail.artifact_name_set in listArt:
            listArt[key.detail.artifact_name_set] = 1
        else:
            listArt[key.detail.artifact_name_set] += 1

        imageStats = getIconAdd(key.detail.mainstats.prop_id, icon = True, size = (21,27))
        if not imageStats:
            continue

        count += 1
        artifacRes.append(await creatArtifact(key,imageStats))

    rezArtSet = await naborArtifact(listArt,ArtifactNameBg)

    return {"art": artifacRes,"nab": rezArtSet}


async def creatUserInfo(hide,uid,player,lang, nameCharter = None, namecard = False):
    if not namecard:
        bannerUserNamecard = await imagSize(link = player.namecard.banner.url, size = (601,283))
    else:
        nameCharter = nameCharter.split("Costume")[0]
        try:
            if nameCharter in ["PlayerGirl","PlayerBoy"]:
                linkImgCard = "https://api.ambr.top/assets/UI/namecard/UI_NameCardPic_0_P.png"
            else:
                linkImgCard = f"https://enka.network/ui/UI_NameCardPic_{nameCharter}_P.png"
            bannerUserNamecard = await imagSize(link = linkImgCard,size = (601,283))
        except:
            linkImgCard = f"https://enka.network/ui/UI_NameCardPic_{nameCharter}1_P.png"
            bannerUserNamecard = await imagSize(link = linkImgCard,size = (601,283))
    bannerUserNamecard = bannerUserNamecard.crop((0, 32, 601, 255))
    defoldBgNamecard = openFile.infoUserBgTeampleTwo.copy()
    maskaBannerNamecard = openFile.infoUserMaskaTeampleTwo.copy().convert('L')
    defoldBgNamecard = Image.composite(defoldBgNamecard, bannerUserNamecard, maskaBannerNamecard)
    frameUserNamecard = openFile.infoUserFrameTeampleTwo.copy()
    defoldBgNamecard.alpha_composite(openFile.infoUserFrameBannerTeampleTwo,(0,0))
    avatar = await imagSize(link = player.avatar.icon.url,size = (150,150))
    avatar = Image.composite(frameUserNamecard, avatar, openFile.infoUserMaskaAvatarTeampleTwo.convert('L'))
    frameUserNamecard.alpha_composite(avatar,(0,0))
    d = ImageDraw.Draw(frameUserNamecard)
    centrName,fonts = await  centrText(player.nickname, witshRam = 150, razmer = 19, start = 0)
    d.text((centrName,155), player.nickname, font= fonts, fill=coloring)
    d.text((163,34), f"{lang['AR']}:{player.level}", font= fonts, fill=coloring)
    d.text((163,65), f"{lang['WL']}:{player.world_level}", font= fonts, fill=coloring)
    d.text((163,99), f"{lang['AB']}:{player.abyss_floor}-{player.abyss_room}", font= fonts, fill=coloring)
    d.text((163,131), f"{lang['AC']}:{player.achievement}", font= fonts, fill=coloring)
    if hide:
        d.text((205,3), "Hidden", font= fontSize(17), fill=coloring)
    else:
        d.text((205,3), str(uid), font= fontSize(17), fill=coloring)
    defoldBgNamecard.alpha_composite(frameUserNamecard,(17,21))
    
    return defoldBgNamecard

def addConst(frameConst,constantRes):
    position = (83,0)
    bgConstant = openFile.ConstantBG.copy()

    for key in constantRes:
        bgConstant.alpha_composite(key ,(position[0],position[1]))
        position = (position[0]+87,position[1])
    frameConst.alpha_composite(bgConstant ,(698 ,899))
    return frameConst

def addTallants(frameTallants,talatsRes):
    position = (49,0)
    bgTallatns = openFile.TalantsBGTeampleTwo.copy()
    for key in talatsRes:
        bgTallatns.alpha_composite(key ,(position[0],position[1]))
        position = (position[0]+90,position[1])

    frameTallants.alpha_composite(bgTallatns ,(851  ,826))
    return frameTallants

def addArtifact(frameArtifact,artifacRes):
    position = (1455 ,290)
    for key in artifacRes:
        frameArtifact.alpha_composite(key ,(position[0],position[1]))
        position = (position[0],position[1]+140)
    return frameArtifact

def appedFrame(frame,weaponRes,nameRes,statRes,constantRes,talatsRes,artifacRes,artifactSet,signatureRes,elementRes,starsRes):
    banner = addConst(frame,constantRes) 
    banner = addTallants(banner,talatsRes)
    banner = addArtifact(banner,artifacRes)
    banner = frame
    banner.alpha_composite(starsRes ,(964,710))
    banner.alpha_composite(nameRes ,(889,746))
    banner.alpha_composite(elementRes ,(893,990))
    banner.alpha_composite(signatureRes ,(27,67))
    banner.alpha_composite(statRes ,(30,302))
    if artifactSet:
        banner.alpha_composite(artifactSet ,(27,839))
    banner.alpha_composite(weaponRes ,(1455 ,65))
    banner.alpha_composite(openFile.SignatureTwo ,(1583 ,992))
    return banner


async def generationTwo(characters,assets,img,adapt,signatureRes,lvl, splash):
    person = assets.character(characters.id)
    starsRes = starsAdd(person)
    elementRes = elementIconPanel(characters.element.value)
    tassk = []
    if splash:
        tassk.append(create_picture(person,characters.element.value,img,adapt,characters.image.banner.url))
    else:
        tassk.append(create_picture(person,characters.element.value,img,adapt))
    tassk.append(weaponAdd(characters.equipments[-1],lvl))
    tassk.append(nameBanner(characters,lvl))
    tassk.append(stats(characters,assets))
    tassk.append(constant(characters))
    tassk.append(talants(characters))
    tassk.append(artifacAdd(characters))
    ec = await asyncio.gather(*tassk)
    result = appedFrame(ec[0].convert("RGBA"),ec[1],ec[2],ec[3],ec[4],ec[5],ec[6]["art"],ec[6]["nab"],signatureRes,elementRes,starsRes)
    return result
