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

async def create_picture(person,imgs,adapt,splash = None):
    if imgs:
        frame = userImageTwo(imgs, element = person.element.value, adaptation = adapt)
    else:
        if splash:
            banner = await imagSize(link = splash,size = (1974,1048))
        else:
            banner = await imagSize(link = person.images.banner.url, size = (1974,1048))
        frame = maskaAdd(person.element.value, banner, teample = 2)
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
        WeaponBg.paste(imageStats,(330,59),imageStats)
    
    stars = star(characters.detail.rarity)
    image = await imagSize(link = characters.detail.icon.url, size = (131,138))
    WeaponBg.paste(image,(20,11),image)
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
    WeaponBg.paste(stars,(10,135),stars)
    return WeaponBg

async def nameBanner(characters,lvlName):
    NameBg = openFile.NameBgTeampleTwo.copy()
    d = ImageDraw.Draw(NameBg)
    centrName,fonts = await centrText(characters.name, witshRam = 244, razmer = 24,start = 19, Yram = 29, y = 0)
    d.text((centrName,1), characters.name, font = fonts, fill=coloring) 
    d.text((33,47), str(characters.friendship_level), font = fontSize(24), fill= coloring) 
    centrName,fonts = await centrText(f"{lvlName['lvl']}: {characters.level}/90", witshRam = 209, razmer = 24, start = 77)
    d.text((centrName,47), f"{lvlName['lvl']}: {characters.level}/90", font = fonts, fill= coloring) 
    return NameBg


def starsAdd(person):
    StarsBg = openFile.StarBg.copy()
    starsIcon = star(person.rarity)
    StarsBg.paste(starsIcon,(17,0),starsIcon)
    
    return StarsBg

async def stats(characters,assets):
    postion = (15,10)
    AttributeBg = openFile.AttributeBgTeampleTwo.copy()
    g = characters.stats
    dopVal = {}
    cout = 0
    maxStat = 0
    elementUp = None

    for key in g:
        if key[0] in ["BASE_HP","FIGHT_PROP_BASE_ATTACK","FIGHT_PROP_BASE_DEFENSE"]:
            if not key[0] in dopVal:
                dopVal[key[0]] = int(key[1].value)
                cout += 1
                if cout == 3:
                    break
    for key in reversed(list(g)):
        
        if key[1].value == 0:
            continue
        iconImg = getIconAdd(key[0])
        if not iconImg:
            continue
        if key[1].id in [40,41,42,43,44,45,46]:
            if key[1].value > maxStat:
                elementUp = key
                maxStat = key[1].value
            if key[1].id == 40:
                key = elementUp
            else:
                continue
        txt = assets.get_hash_map(key[0])
        Attribute = openFile.AttributeTeampleTwo.copy()
        d = ImageDraw.Draw(Attribute)
        
        icon = await imagSize(image = iconImg,fixed_width = 26)

        Attribute.paste(icon, (10,4),icon)

        if not key[1].id in stat_perc:
            value = str(math.ceil(key[1].value))
        else:
            value = f"{round(key[1].value * 100, 1)}%"
        pX,fnt = await centrText(value, witshRam = 151, razmer = 24, start = 410)
        d.text((pX,7), value, font = fnt, fill=coloring)

        d.text((67,7), str(txt), font = fontSize(24), fill=coloring)

        AttributeBg.paste(Attribute,(postion[0],postion[1]),Attribute)
        '''
        if key[0] in dopStatAtribute:
            ad = ImageDraw.Draw(AttributeBg)
            dopStatVal  = dopVal[dopStatAtribute[key[0]]]
            dopStatValArtifact = int(key[1].value - dopStatVal)
            if dopStatValArtifact != 0:
                ad.text((pX+5,postion[1]+23), f"{dopStatVal} + {dopStatValArtifact}", font = fontSize(15), fill=(248,199,135))
        '''
        postion = (postion[0],postion[1]+55)
    return AttributeBg
    
async def constant(characters,person):
    constantRes = []  
    for key in characters.constellations:
        closeConstBg = openFile.ClossedBg.copy()
        closeConsticon = openFile.Clossed.copy()
        openConstBg = openImageElementConstant(person.element.value)
        imageIcon = await imgD(link = key.icon.url)
        imageIcon = imageIcon.resize((43,48))
        if not key.unlocked:
            closeConstBg.paste(imageIcon, (19,20),imageIcon)
            closeConstBg.paste(closeConsticon, (0,0),closeConsticon)
            const = closeConstBg
        else:
            openConstBg.paste(imageIcon, (19,20),imageIcon)
            const = openConstBg
        constantRes.append(const)
    
    return constantRes

async def talants(characters):
    count = 0
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
        talantsBg.paste(imagesIconTalants, (7,6),imagesIconTalants)
        px,fnt = await centrText(key.level, witshRam = 25, razmer = 18, start = 1, Yram = 25, y = 1) 
        d.text(px, str(key.level), font = fnt, fill=(248,199,135,255))
        talantsBg.paste(talantsCount, (20,47),talantsCount)
        tallantsRes.append(talantsBg)
        count+=1
        if count == 3:
            break
    return tallantsRes
async def naborArtifact(info,ArtifactNameBg):
    naborAll = []
    for key in info:
        if info[key] > 1:
            ArtifactNameFrame = openFile.ArtifactNameFrameTeampleTwo.copy()
            d = ImageDraw.Draw(ArtifactNameFrame)
            centrName,fonts = await centrText(key, witshRam = 289, razmer = 24, start = 2, Yram = 28, y = 1) 
            d.text(centrName, str(key), font= fonts, fill=coloring)
            d.text((356,0), str(info[key]), font= fontSize(24), fill=coloring)
            naborAll.append(ArtifactNameFrame)
    position = (156,38)
    for key in naborAll:
        if len(naborAll) == 1:
            ArtifactNameBg.paste(key,(156,54),key)
        else:
            ArtifactNameBg.paste(key,position,key)
            position = (position[0],position[1]+34)

    return ArtifactNameBg


async def creatArtifact(infpart,imageStats):
    ArtifactBg = openFile.ArtifactBgTeampleTwo.copy()
    ArtifactUp = openFile.ArtifactBgUpTeampleTwo.copy()
    artimg = await imagSize(link = infpart.detail.icon.url,size = (120,107))
    ArtifactBg.paste(artimg,(-5,0),artimg)
    ArtifactBg.paste(ArtifactUp,(0,0),ArtifactUp)
    d = ImageDraw.Draw(ArtifactBg)
    if str(infpart.detail.mainstats.type) == "DigitType.PERCENT":
        val = f"{infpart.detail.mainstats.value}%"
    else:
        val = infpart.detail.mainstats.value
    centrName,fonts = await centrText(val, witshRam = 62, razmer = 17, start = 53)
    d.text((centrName,77), str(val), font= fonts, fill=coloring)
    
    ArtifactBg.paste(imageStats,(7,2),imageStats)
    d.text((81,97), str(infpart.level), font= fontSize(17), fill=coloring)
    starsImg = star(infpart.detail.rarity).resize((77,22))
    ArtifactBg.paste(starsImg,(2,97),starsImg)
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
        ArtifactBgStat.paste(imageStats,(3,1),imageStats)
        d.text((57,2), v, font= fontSize(24), fill=coloring)
        ArtifactBg.paste(ArtifactBgStat,positionIcon,ArtifactBgStat)
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
        linkImgCard = f"https://enka.network/ui/UI_NameCardPic_{nameCharter}_P.png"
        bannerUserNamecard = await imagSize(link = linkImgCard,size = (601,283))
    bannerUserNamecard = bannerUserNamecard.crop((0, 32, 601, 255))
    defoldBgNamecard = openFile.infoUserBgTeampleTwo.copy()
    maskaBannerNamecard = openFile.infoUserMaskaTeampleTwo.copy().convert('L')
    defoldBgNamecard = Image.composite(defoldBgNamecard, bannerUserNamecard, maskaBannerNamecard)
    frameUserNamecard = openFile.infoUserFrameTeampleTwo.copy()
    defoldBgNamecard.paste(openFile.infoUserFrameBannerTeampleTwo,(0,0),openFile.infoUserFrameBannerTeampleTwo)
    avatar = await imagSize(link = player.avatar.icon.url,size = (150,150))
    avatar = Image.composite(frameUserNamecard, avatar, openFile.infoUserMaskaAvatarTeampleTwo.convert('L'))
    frameUserNamecard.paste(avatar,(0,0),avatar)
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
    defoldBgNamecard.paste(frameUserNamecard,(17,21),frameUserNamecard)
    
    return defoldBgNamecard

def addConst(frameConst,constantRes):
    position = (83,0)
    bgConstant = openFile.ConstantBG.copy()

    for key in constantRes:
        bgConstant.paste(key ,(position[0],position[1]),key)
        position = (position[0]+87,position[1])
    frameConst.paste(bgConstant ,(698 ,899),bgConstant)
    return frameConst

def addTallants(frameTallants,talatsRes):
    position = (49,0)
    bgTallatns = openFile.TalantsBGTeampleTwo.copy()
    for key in talatsRes:
        bgTallatns.paste(key ,(position[0],position[1]),key)
        position = (position[0]+90,position[1])

    frameTallants.paste(bgTallatns ,(851  ,826),bgTallatns)
    return frameTallants

def addArtifact(frameArtifact,artifacRes):
    position = (1455 ,290)
    for key in artifacRes:
        frameArtifact.paste(key ,(position[0],position[1]),key)
        position = (position[0],position[1]+140)
    return frameArtifact

def appedFrame(frame,weaponRes,nameRes,statRes,constantRes,talatsRes,artifacRes,artifactSet,signatureRes,elementRes,starsRes):
    banner = addConst(frame,constantRes) 
    banner = addTallants(banner,talatsRes)
    banner = addArtifact(banner,artifacRes)
    banner = frame
    banner.paste(starsRes ,(964,710),starsRes)
    banner.paste(nameRes ,(889,746),nameRes)
    banner.paste(elementRes ,(893,990),elementRes)
    banner.paste(signatureRes ,(27,67),signatureRes)
    banner.paste(statRes ,(30,302),statRes)
    if artifactSet:
        banner.paste(artifactSet ,(27,839),artifactSet)
    banner.paste(weaponRes ,(1455 ,65),weaponRes)
    banner.paste(openFile.SignatureTwo ,(1583 ,992),openFile.SignatureTwo)
    return banner


async def generationTwo(characters,assets,img,adapt,signatureRes,lvl, splash):
    person = assets.character(characters.id)
    starsRes = starsAdd(person)
    elementRes = elementIconPanel(person.element.value)
    tassk = []
    if splash:
        tassk.append(create_picture(person,img,adapt,characters.image.banner.url))
    else:
        tassk.append(create_picture(person,img,adapt))
    tassk.append(weaponAdd(characters.equipments[-1],lvl))
    tassk.append(nameBanner(characters,lvl))
    tassk.append(stats(characters,assets))
    tassk.append(constant(characters,person))
    tassk.append(talants(characters))
    tassk.append(artifacAdd(characters))
    ec = await asyncio.gather(*tassk)
    result = appedFrame(ec[0],ec[1],ec[2],ec[3],ec[4],ec[5],ec[6]["art"],ec[6]["nab"],signatureRes,elementRes,starsRes)
    return result
