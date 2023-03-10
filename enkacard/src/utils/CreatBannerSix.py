from . import openFile
from .Generation import *
from .FunctionsPill import imgD,imagSize
from PIL import ImageDraw
import math,asyncio

def open_bg_element(element):
    if element == "Fire":
        return openFile.PYRO_SIX.copy()
    elif element== "Grass":
        return openFile.DENDRO_SIX.copy()
    elif element == "Electric":
        return openFile.ELECTRO_SIX.copy()
    elif element == "Water":
        return openFile.GYDRO_SIX.copy()
    elif element == "Wind":
        return openFile.ANEMO_SIX.copy()
    elif element== "Rock":
        return openFile.GEO_SIX.copy()
    elif element == "Ice":
        return openFile.ANEMO_SIX.copy()
    else:
        return openFile.PYRO_SIX.copy()

async def artifact(artifact):
    CRIT_DMG = 0
    CRIT_RATE = 0
    artifactData = []
    for infpart in artifact:
        if infpart.detail.artifact_name_set == "":
            continue
        bg = openFile.ART_bg_SIX.copy()
        bgs = bg.copy()
        artifactMaskaFive = openFile.ART_maska_SIX.convert('L')
        artimg = await imagSize(link = infpart.detail.icon.url,size = (171,171))
        bgs.alpha_composite(artimg,(-46,-29))
        bg = Image.composite(bg,bgs,artifactMaskaFive)
        imageStats = getIconAdd(infpart.detail.mainstats.prop_id, icon = True, size = (20,19))
        bg.alpha_composite(imageStats,(74,3))
        d = ImageDraw.Draw(bg)
        if str(infpart.detail.mainstats.type) == "DigitType.PERCENT":
            val = f"{infpart.detail.mainstats.value}%"
        else:
            val = infpart.detail.mainstats.value
        if infpart.detail.mainstats.prop_id == "FIGHT_PROP_CRITICAL_HURT":
            CRIT_DMG += infpart.detail.mainstats.value
        if infpart.detail.mainstats.prop_id == "FIGHT_PROP_CRITICAL":
            CRIT_RATE +=infpart.detail.mainstats.value
        x = fontSize(24).getlength(str(val))
        d.text((int(95-x),23), str(val), font = fontSize(24), fill=(0,0,0,255))
        d.text((int(96-x),24), str(val), font = fontSize(24), fill=coloring)

        x = fontSize(24).getlength(f"+{infpart.level}")
        d.text((int(95-x),51), f"+{infpart.level}", font = fontSize(24), fill=(0,0,0,255))
        d.text((int(96-x),51), f"+{infpart.level}", font = fontSize(24), fill=coloring)
        stars = star(infpart.detail.rarity)
        bg.alpha_composite(stars,(0,74))
        artifactData.append(bg)
        for key in infpart.detail.substats:
            if key.prop_id == "FIGHT_PROP_CRITICAL_HURT":
                CRIT_DMG += key.value
            if key.prop_id == "FIGHT_PROP_CRITICAL":
                CRIT_RATE +=key.value
    TCV = float('{:.2f}'.format(CRIT_DMG + (CRIT_RATE*2)))
    TCVBG = openFile.TCV.copy()
    d = ImageDraw.Draw(TCVBG)
    x = fontSize(19).getlength(f"{TCV}CV")
    d.text((int(94-x),60), f"{TCV}CV", font = fontSize(19), fill=(0,0,0,255))
    d.text((int(94-x+1),60), f"{TCV}CV", font = fontSize(19), fill=(255,198,0,255))
    artifactData.append(TCVBG)

    return artifactData



async def talants(skills):
    tallantsRes = []
    for key in skills:
        talantsBg = openFile.TALANTS_bg_SIX.copy()
        if key.level > 9:
            talantsCount = openFile.TALANTS_CoontBig_SIX
        else:
            talantsCount = openFile.TALANTS_CoontLow_SIX
        d = ImageDraw.Draw(talantsBg)
        imagesIconTalants = await imgD(link = key.icon.url)
        imagesIconTalants = imagesIconTalants.resize((67,68))
        talantsBg.alpha_composite(imagesIconTalants, (19,0))
        talantsBg.alpha_composite(talantsCount, (0,0))
        x = fontSize(18).getlength(str(key.level))
        d.text((int(54-x/2),65), str(key.level), font = fontSize(18), fill=coloring)
        tallantsRes.append(talantsBg)
    return tallantsRes


async def generationBg(element,link,characters,lvl, chartImg,uid,artist):
    bgElement = open_bg_element(element)
    bg = openFile.frame_SIX.copy()
    if chartImg != None:
        image,posX = centryImage(chartImg, teample = 6)
        bgElement.alpha_composite(image,(posX,0))
        castum = True
    else:
        image = await imagSize(link,size = (4040,2020))
        bgElement.alpha_composite(image,(-1557 ,-224))
        castum = False

    bgElement.alpha_composite(openFile.SHADOW_SIX,(0,0))
    bgElement.alpha_composite(openFile.INFO_RAM,(0,0))
    bgElement.alpha_composite(openFile.FRENDS,(339,1100))
    sign = openFile.SIGNATURE4
    if castum:
        if artist != None:
            sign = openFile.SIGNATURE4_ARTIST
    bgElement.alpha_composite(sign,(533 ,1007))
    bg = Image.composite(bg,bgElement,openFile.MASKA_SIX.convert("L"))
    level = f"{lvl}: {characters.level}/90"
    
    d = ImageDraw.Draw(bg)
    if castum:
        if artist != None:
            d.text((638 ,1014), artist, font = fontSize(23), fill=coloring)
    x = fontSize(27).getlength(characters.name)
    d.text((int(286-x/2),1064), characters.name, font = fontSize(27), fill=coloring)
    x = fontSize(27).getlength(level)
    d.text((int(195-x/2),1100), level, font = fontSize(27), fill=coloring)
    d.text((369 ,1100), str(characters.friendship_level), font = fontSize(27), fill=coloring)
    d.text((173 ,1027), uid, font = fontSize(27), fill=(0,0,0,255))
    d.text((175 ,1027), uid, font = fontSize(27), fill=coloring)
    return bg


async def addTalants(bg,listT):
    position = [
        515,
        643,
        780
    ]
    i = 0
    for key in listT:
        bg.alpha_composite(key,(position[i],1384))
        i += 1

    return bg

async def addArtifact(bg,listA):
    position = [
        (539,1146),
        (666,1146),
        (798,1146),
        (539,1273),
        (666,1273),
        (798,1273),
    ]
    i = 0
    for key in listA:
        bg.alpha_composite(key, position[i])
        i += 1
    return bg



async def addConst(bg,listC):
    position = [
        55,
        183,
        310,
        438,
        559,
        686
    ]
    i = 0
    for key in listC:
        bg.alpha_composite(key,(position[i],1463))
        i += 1

    return bg

async def weapon(bg,info,lvl):
    image = await imagSize(link = info.detail.icon.url,size = (136,131))
    bg.alpha_composite(image,(23,1308))

    name = info.detail.name
    lvl = f"{lvl}: {info.level}/90"
    lvlUp = f"R{info.refinement}"
    baseAtt = info.detail.mainstats.value
    imageStats = None
    proc = False
    dopStat = 0

    d = ImageDraw.Draw(bg)
    d.text((177 ,1327), name, font= fontSize(24), fill=coloring)

    d.text((203,1363), str(baseAtt), font= fontSize(24), fill=coloring)

    for substate in info.detail.substats:
        imageStats = getIconAdd(substate.prop_id, icon = True, size = (24,26))
        if not imageStats:
            continue
        dopStat = substate.value
        if str(substate.type) == "DigitType.PERCENT":
            proc = True
    if imageStats:
        bg.alpha_composite(imageStats,(299,1362))

    if proc:
        d.text((329 ,1363), f"{dopStat}%", font= fontSize(24), fill=coloring)
    else:
        d.text((329,1363), str(dopStat), font= fontSize(24), fill=coloring)
    
    d.text((43,1314), str(lvlUp), font= fontSize(24), fill=(255,207,42,255))

    d.text((177,1405), str(lvl), font= fontSize(24), fill=coloring)

    stars = await starFive(info.detail.rarity)
    bg.alpha_composite(stars,(17,1430))

    return bg


async def stats(bg, characters):
    g = characters.stats
    elementUp = True
    dopval = {}

    posIcon = [
        77,
        238,
        395
    ]

    posText = [
        114,
        275,
        432
    ]

    d = ImageDraw.Draw(bg)
    i = 0
    for key in g:
        if key[0] in ["BASE_HP","FIGHT_PROP_BASE_ATTACK","FIGHT_PROP_BASE_DEFENSE"]:
            dopval[key[0]] = key[1].value

        if key[1].id in [2000,2001,2002]:
            iconImg = getIconAdd(key[0])
            icon = await imagSize(image = iconImg,fixed_width = 26)
            bg.alpha_composite(icon,(posIcon[i],1155))

            if not key[1].id in stat_perc:
                value = str(math.ceil(key[1].value))
            else:
                value = f"{round(key[1].value * 100, 1)}%"
            if key[0] in dopStatAtribute:
                d.text((posText[i],1157), value, font = fontSize(24), fill= coloring) 
                dopStatVal = int(dopval[dopStatAtribute[key[0]]])
                dopStatValArtifact = int(key[1].value - dopval[dopStatAtribute[key[0]]])
                if dopStatValArtifact != 0:
                    dopValx = fontSize(17).getlength(str(dopStatVal))
                    d.text((posText[i]-dopValx,1190),str(dopStatVal), font = fontSize(17), fill=(255,255,255,255))
                    d.text((posText[i]+5,1190),f"+{dopStatValArtifact}", font = fontSize(17), fill=(255,198,0,255))
            i += 1
            if i == 3:
                break
    
    posIcon = [
        (69,1230),
        (220,1230),
        (364,1230),
        (69,1266),
        (220,1266),
        (364,1266)
    ]

    posText = [
        (107,1233),
        (258,1233),
        (402,1233),
        (107,1269),
        (258,1269),
        (402,1269),
    ]
    i = 0

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
        icon = await imagSize(image = iconImg,fixed_width = 26)
        bg.alpha_composite(icon,(posIcon[i]))

        if not key[1].id in stat_perc:
            value = str(math.ceil(key[1].value))
        else:
            value = f"{round(key[1].value * 100, 1)}%"

        d.text(posText[i], value, font = fontSize(22), fill= coloring)
        i += 1

    return bg

async def const(charter):
    constantRes = []  
    for key in charter.constellations:
        openConstBg,closedConstBg = openImageElementConstant(charter.element.value, teampt = 3)
        imageIcon = await imgD(link = key.icon.url)
        imageIcon =  imageIcon.resize((79,79))
        
        if not key.unlocked:
            closedConstBg = closedConstBg.resize((128,131))
            closedIcon = openFile.ClosedConstTree.resize((81,81))
            closedConstBg.alpha_composite(closedConstBg, (0,0))
            closedConstBg.alpha_composite(imageIcon, (24,26))
            closedConstBg.alpha_composite(closedIcon, (23,26))
            
            const = closedConstBg
        else:
            openConstBg = openConstBg.resize((128,131))
            openConstBg.alpha_composite(imageIcon, (24,26))
            const = openConstBg

        constantRes.append(const)
    
    return constantRes



async def generationSix(items,assets,lang, uid = "UID: Hide", cards = None,artist = None):
    result = {}
    positions = [
        (17,0),
        (887,0),
        (1761,0),
        (2633,0),
    ]
    i = 0
    
    ALL_BG = openFile.ALLSIXBG.copy()
    if len(items) == 3:
        ALL_BG = ALL_BG.crop((0,0,2839,1615))
    elif len(items) == 2:
        ALL_BG = ALL_BG.crop((0,0,1950,1615))
    elif len(items) == 1:
        ALL_BG = ALL_BG.crop((0,0,1066,1615))
    for characters in items:
        charactersImg = characters[1]
        characters = characters[0]
        if cards != None and characters.name in cards:
            if not characters.name in result:
                result[characters.name] = {"img": cards[characters.name]["img"].copy(), "id": characters.id}
        else:
            task = []
            person = assets.character(characters.id)
            task.append(generationBg(characters.element.value,person.images.banner.url,characters,lang["lvl"],charactersImg, uid,artist))
            task.append(talants(characters.skills))
            task.append(artifact(characters.equipments))
            task.append(const(characters))
            ec = await asyncio.gather(*task)

            bg = await addTalants(ec[0],ec[1])
            bg = await weapon(bg,characters.equipments[-1],lang["lvl"])
            bg = await addArtifact(bg,ec[2])
            bg = await stats(bg, characters)
            bg = await addConst(bg,ec[3])
            if not characters.name in result:
                result[characters.name] = {"img": bg, "id": characters.id}

    for key in result:
        ALL_BG.alpha_composite(result[key]["img"],positions[i])
        i += 1         
    return {"img": ALL_BG, "cards": result}