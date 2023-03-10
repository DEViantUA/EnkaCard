from . import Generation as gen
from .FunctionsPill import imagSize,imgD
from PIL import ImageDraw,Image
from . import openFile as of
from . import options
import math,asyncio


async def background(imgs,splash,element,signatureRes):
    if splash:
        imgs = await imagSize(imgs,size = (2605,1323))
        frame = await gen.creatFiveBg(imgs, element = element)
    else:
        frame = await gen.creatFiveBg(imgs, element = element, adapt = True)
    d = ImageDraw.Draw(frame)
    d.text((2357,947), signatureRes, font= gen.fontSize(26), fill=options.coloring)
    frame.alpha_composite(of.LK_LOGO_BOT,(1722,890))
    return frame

async def weapon(characters,lvlName):
    if characters.detail.artifact_name_set != "":
        return None
    WeaponBg = of.WeaponTeampleFive.copy()
    d = ImageDraw.Draw(WeaponBg)
    proc = False    
    name = characters.detail.name
    lvl = characters.level
    lvlUp = characters.refinement
    baseAtt = characters.detail.mainstats.value
    imageStats = None
    dopStat = 0

    for substate in characters.detail.substats:
        imageStats = gen.getIconAdd(substate.prop_id, icon = True, size = (28,28))
        if not imageStats:
            continue
        dopStat = substate.value
        if str(substate.type) == "DigitType.PERCENT":
            proc = True
    if imageStats:
        WeaponBg.alpha_composite(imageStats,(210,97))

    stars = await gen.starFive(characters.detail.rarity)
    image = await imagSize(link = characters.detail.icon.url,size = (147,146))

    WeaponBg.alpha_composite(image,(63,4))
    WeaponBg.alpha_composite(stars,(36,141))
    
    d.text((212,28), str(name), font= gen.fontSize(22), fill=options.coloring) 
    d.text((333 ,100), f"R{lvlUp}", font= gen.fontSize(20), fill=(255,212,130,255))

    d.text((333,63), f"{lvlName}: {lvl}/90", font= gen.fontSize(20), fill=options.coloring) 
    d.text((245,63), str(baseAtt), font= gen.fontSize(20), fill=options.coloring)

    if proc:
        d.text((245,100), f'{dopStat}%', font= gen.fontSize(20), fill=(255,212,130,255))
    else:
        d.text((245,100), str(dopStat), font= gen.fontSize(20), fill=(255,212,130,255))
    return WeaponBg



async def stats(characters,assets):
    g = characters.stats
    elementUp = True
    dopval = {}
    posIcon = (47,40)
    posText = (89,40)
    posValue = (597,40)
    AttributeBg = of.BGStatsTeampleFive.copy()

    d = ImageDraw.Draw(AttributeBg)
    for key in g:
        if key[0] in ["BASE_HP","FIGHT_PROP_BASE_ATTACK","FIGHT_PROP_BASE_DEFENSE"]:
            dopval[key[0]] = key[1].value

        if key[1].id in [2000,2001,2002]:
            iconImg = gen.getIconAdd(key[0])
            icon = await imagSize(image = iconImg,fixed_width = 26)
            AttributeBg.alpha_composite(icon,posIcon)
            txt = assets.get_hash_map(key[0])
            if not key[1].id in options.stat_perc:
                value = str(math.ceil(key[1].value))
            else:
                value = f"{round(key[1].value * 100, 1)}%"

            d.text(posText, str(txt), font = gen.fontSize(22), fill=options.coloring)
            xx,y = gen.fontSize(22).getsize(str(value))
            posValueX = (posValue[0] - xx,posValue[1])
            d.text(posValueX, value, font = gen.fontSize(22), fill= options.coloring)

            if key[0] in gen.dopStatAtribute:
                dopStatVal = int(dopval[options.dopStatAtribute[key[0]]])
                dopStatValArtifact = int(key[1].value - dopval[options.dopStatAtribute[key[0]]])
                if dopStatValArtifact != 0:
                    dopArtx,y = gen.fontSize(18).getsize(f"+{dopStatValArtifact}")
                    
                    positionDopArt = (posValue[0] - dopArtx ,posValue[1]+25)
                    d.text(positionDopArt,f"+{dopStatValArtifact}", font = gen.fontSize(18), fill=(0,255,156,255))

                    dopValx,y = gen.fontSize(18).getsize(str(dopStatVal))
                    positionDopVal = (positionDopArt[0] - dopValx - 18,positionDopArt[1])
                    d.text(positionDopVal,str(dopStatVal), font = gen.fontSize(18), fill=options.coloring)

            posIcon = (47, posIcon[1] + 63)
            posText = (89, posText[1] + 63)
            posValue = (597, posValue[1] + 63)

    for key in g:
        if key[1].id in [40,41,42,43,44,45,46]:
            if elementUp:
                key = max((x for x in g if 40 <= x[1].id <= 46), key=lambda x: x[1].value)
                elementUp = False
            else:
                continue
        if key[1].value == 0 or key[1].id in [2000,2001,2002]:
            continue
        iconImg = gen.getIconAdd(key[0])
        if not iconImg:
            continue
        txt = assets.get_hash_map(key[0])
        icon = await imagSize(image = iconImg,fixed_width = 26)
        AttributeBg.alpha_composite(icon,posIcon)

        if not key[1].id in options.stat_perc:
            value = str(math.ceil(key[1].value))
        else:
            value = f"{round(key[1].value * 100, 1)}%"
        xx,y = gen.fontSize(22).getsize(str(value))
        posValueX = (posValue[0] - xx,posValue[1])
        d.text(posValueX, value, font = gen.fontSize(22), fill= options.coloring)
        d.text(posText, str(txt), font = gen.fontSize(22), fill= options.coloring)
        
        posIcon = (47, posIcon[1] + 63)
        posText = (89, posText[1] + 63)
        posValue = (597, posValue[1] + 63)

    return AttributeBg


async def constant(characters):
    constantRes = []  
    for key in characters.constellations:
        openConstBg,closedConstBg = gen.openImageElementConstant(characters.element.value, teampt = 3)
        imageIcon = await imgD(link = key.icon.url)
        imageIcon =  imageIcon.resize((78,78))
        
        if not key.unlocked:
            closedConstBg = closedConstBg.resize((121,123))
            closedIcon = of.ClosedConstTree.resize((78,78))
            closedConstBg.alpha_composite(imageIcon, (22,23))
            closedConstBg.alpha_composite(closedIcon, (21,23))
            
            const = closedConstBg
        else:
            openConstBg = openConstBg.resize((121,123))
            openConstBg.alpha_composite(imageIcon, (22,23))
            const = openConstBg

        constantRes.append(const)
    
    return constantRes

async def talants(skills):
    tallantsRes = []
    for key in skills:
        if key.level > 9:
            talantsBg = of.BIG_LVLTeampleFive.copy()
        else:
            talantsBg = of.LOW_LVLTeampleFive.copy()

        d = ImageDraw.Draw(talantsBg)
        imagesIconTalants = await imgD(link = key.icon.url)
        imagesIconTalants = imagesIconTalants.resize((90,90))
        talantsBg.alpha_composite(imagesIconTalants, (26,0))
        if len(str(key.level)) == 2:
            d.text((57,92), str(key.level), font = gen.fontSize(24), fill= options.coloring)
        else:
            d.text((62,92), str(key.level), font = gen.fontSize(24), fill=options.coloring)
        tallantsRes.append(talantsBg)
    return tallantsRes

async def appendConstant(items,bg):
    positionConstant = 157
    for i in items:
        bg.alpha_composite(i,(704,positionConstant))
        positionConstant += 133
    
    return bg

async def appendTalant(items,bg):
    positionConstant = 369
    for i in items:
        bg.alpha_composite(i,(1762,positionConstant))
        positionConstant += 139
    
    return bg

async def infoCharter(characters,lvlName,element):
    bg = of.NAME_BANNERTeampleFive.copy()
    d = ImageDraw.Draw(bg)
    xx,y = gen.fontSize(26).getsize(characters.name)
    x = 182 - xx/2
    d.text((x,16), characters.name, font = gen.fontSize(26), fill= options.coloring)
    namLvl = f"{lvlName}: {characters.level}/90"
    xx,y = gen.fontSize(22).getsize(namLvl)
    x = 182 - xx/2
    d.text((x,61),namLvl,font = gen.fontSize(22), fill=options.coloring)
    element = await gen.charterElement(element)
    bg.alpha_composite(element,(28,33))
    return bg


positionIconArtifact = ((281,30),(281,91), (463,30),(463,91))
positionTextArtifact = ((323,36),(323,97), (505,36),(505,97))

async def naborArtifact(info):
    ArtifactNameBg = of.ArtifactSETFive.copy()
    count = 0
    for key in info:
        if info[key] > 1:
            count += 1
    if count != 0:
        d = ImageDraw.Draw(ArtifactNameBg)
        positionY = 33
        for key in info:
            if info[key] > 1:
                if count == 1:
                    d.text((153,51), str(key), font= gen.fontSize(22), fill=(120,255,123))
                    d.text((537 ,51), str(info[key]), font= gen.fontSize(22), fill=(120,255,123))
                    break
                else:
                    d.text((153,positionY), str(key), font= gen.fontSize(22), fill=(141,231,141))
                    d.text((537 ,positionY), str(info[key]), font= gen.fontSize(22), fill=(120,255,123))
                    positionY += 38
    return ArtifactNameBg    


async def artifact(characters):
    artifactData = []
    listArt = {}
    for infpart in characters:

        if infpart.detail.artifact_name_set == "":
            continue
        if not infpart.detail.artifact_name_set in listArt:
            listArt[infpart.detail.artifact_name_set] = 1
        else:
            listArt[infpart.detail.artifact_name_set] += 1

        ArtifactBgOn = of.ArtifactBGFive.copy()
        ArtifactBg = of.ArtifactBGFive.copy()
        ArtifactLVLFive = of.ArtifactLVLFive.copy()
        artifactMaskaFive = of.artifactMaskaFive.convert('L')
        artimg = await imagSize(link = infpart.detail.icon.url,size = (277,277))
        ArtifactBgOn.alpha_composite(artimg,(-40,-58))

        ArtifactBg = Image.composite(ArtifactBg, ArtifactBgOn, artifactMaskaFive)
        d = ImageDraw.Draw(ArtifactBg)
        lvl = ImageDraw.Draw(ArtifactLVLFive)
        if str(infpart.detail.mainstats.type) == "DigitType.PERCENT":
            val = f"{infpart.detail.mainstats.value}%"
        else:
            val = infpart.detail.mainstats.value
        x,y = gen.fontSize(37).getsize(str(val))
        d.text((193-x-2,65), str(val), font= gen.fontSize(37), fill=(0,0,0,255))
        d.text((193-x,65), str(val), font= gen.fontSize(37), fill=options.coloring)

        if len(str(infpart.level)) == 2:
            lvl.text((1,-2), f"+{infpart.level}", font= gen.fontSize(22), fill=options.coloring)
        else:
            lvl.text((9,-2), f"+{infpart.level}", font= gen.fontSize(22), fill=options.coloring)

        ArtifactBg.alpha_composite(ArtifactLVLFive,(147,109))
        starsImg = await gen.starFive(infpart.detail.rarity,weapon = False)
        ArtifactBg.alpha_composite(starsImg,(19,130))
        imageStats = gen.getIconAdd(infpart.detail.mainstats.prop_id, icon = True, size = (167,28))
        ArtifactBg.alpha_composite(imageStats,(167,28))                  
        i = 0
        for key in infpart.detail.substats:
            v = f"+{key.value}"
            if str(key.type) == "DigitType.PERCENT":
                v = f"{v}%"
            imageStats = gen.getIconAdd(key.prop_id, icon = True)
            if not imageStats:
                continue
            imageStats= await imagSize(image = imageStats,fixed_width = 33) 
            ArtifactBg.alpha_composite(imageStats,positionIconArtifact[i])
            d.text(positionTextArtifact[i], v, font= gen.fontSize(25), fill=options.coloring)

            i += 1
        artifactData.append(ArtifactBg)
    
    return {"art": artifactData, "set": await naborArtifact(listArt)}

async def appendArtifact(items,bg):
    positionConstant = 43
    for i in items:
        bg.alpha_composite(i,(1933,positionConstant))
        positionConstant += 184
    
    return bg



async def build(frame,weapon,stat,info,const,talant,artf,set):
    frame.alpha_composite(weapon,(26,43))
    frame.alpha_composite(stat,(26,215))
    frame.alpha_composite(info,(704,43))
    frame = await appendConstant(const,frame)
    frame = await appendTalant(talant,frame)
    frame = await appendArtifact(artf,frame)
    frame.alpha_composite(set,(26,839))
    
    return frame

async def generationFive(characters,assets,img,lvl,splash,signatureRes):
    person = assets.character(characters.id)
    task = []
    if img != None:
        task.append(background(img,False,characters.element,signatureRes))
    else:
        if splash:
            task.append(background(characters.image.banner.url,True,characters.element,signatureRes))
        else:
            task.append(background(person.images.banner.url,True,characters.element,signatureRes))
    task.append(weapon(characters.equipments[-1],lvl))
    task.append(stats(characters,assets))
    task.append(infoCharter(characters,lvl,characters.element))
    task.append(constant(characters))
    task.append(talants(characters.skills))
    task.append(artifact(characters.equipments))

    ec = await asyncio.gather(*task)

    return await build(ec[0],ec[1],ec[2],ec[3],ec[4],ec[5],ec[6]["art"], ec[6]["set"])