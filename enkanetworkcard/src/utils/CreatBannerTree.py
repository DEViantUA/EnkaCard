# Copyright 2022 DEViantUa <t.me/deviant_ua>
# All rights reserved.

import math,asyncio

from PIL import ImageDraw
from .Generation import * 
from .FunctionsPill import imagSize,centrText,imgD
from .options import *
from . import openFile

async def characterBackground(person,element,imgs,adapt,splash = None):
    if imgs:
        frame = userImageTree(imgs, element = element, adaptation = adapt)
    else:
        if splash:
            banner = await imagSize(link = splash,size = (2351,1168))
        else:
            banner = await imagSize(link = person.images.banner.url,size = (2351,1168))
        frame = maskaAdd(element, banner, teample = 3)
    return frame

async def infoCharter(bg,characters,lvlName):
    d = ImageDraw.Draw(bg)
    d.text((37,46), characters.name, font = fontSize(24), fill=(0,0,0,255))
    d.text((37,45), characters.name, font = fontSize(24), fill=coloring)
    d.text((37,99),f"{lvlName['lvl']}: {characters.level}/90",font = fontSize(24), fill=(0,0,0,255))
    d.text((37,98),f"{lvlName['lvl']}: {characters.level}/90",font = fontSize(24), fill=coloring)
    d.text((83,145), str(characters.friendship_level), font = fontSize(24), fill=(0,0,0,255))
    d.text((83,144), str(characters.friendship_level), font = fontSize(24), fill=coloring)
    bg.alpha_composite(openFile.FRENDS,(37,142))
    return bg

async def talants(characters):
    count = 0
    tallantsRes = []
    for key in characters.skills:
        if key.level > 9:
            talantsBg = openFile.TalantsFrameT_GoldTeampleTree.copy()
        else:
            talantsBg = openFile.TalantsFrameTeampleTree.copy()
        d = ImageDraw.Draw(talantsBg)
        imagesIconTalants = await imgD(link = key.icon.url)
        imagesIconTalants = imagesIconTalants.resize((67,67))
        talantsBg.alpha_composite(imagesIconTalants, (16,0))
        if len(str(key.level)) == 2:
            d.text((39,63), str(key.level), font = fontSize(24), fill=coloring)
        else:
            d.text((41,65), str(key.level), font = fontSize(24), fill=coloring)
        tallantsRes.append(talantsBg)
        count+=1
        if count == 3:
            break
    return tallantsRes

async def weapon(characters,lvlName):
    if characters.detail.artifact_name_set != "":
        return None
    WeaponBg = openFile.WeaponBgTeampleTree.copy()
    d = ImageDraw.Draw(WeaponBg)
    proc = False    
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
        WeaponBg.alpha_composite(imageStats,(318,66))

    stars = star(characters.detail.rarity).resize((93,31))
    image = await imagSize(link = characters.detail.icon.url,size = (143,152))

    WeaponBg.alpha_composite(image,(6,0))
    WeaponBg.alpha_composite(openFile.WeaponLight,(0,143))
    WeaponBg.alpha_composite(stars,(28,136))
    
    position,font = await centrText(name, witshRam = 329, razmer = 24, start = 150)
    d.text((position,10), str(name), font= font, fill=(0,0,0,255)) 
    d.text((position,9), str(name), font= font, fill=coloring) 
    d.text((185 ,114), f"R{lvlUp}", font= fontSize(24), fill=(248,199,135,255))

    position,font = await centrText(f"{lvlName['lvl']}: {lvl}/90", witshRam = 240, razmer = 24, start = 240)
    d.text((position,113), f"{lvlName['lvl']}: {lvl}/90", font= font, fill=coloring) 

    position,font = await centrText(baseAtt, witshRam = 79, razmer = 24, start = 214)    
    d.text((position,64), str(baseAtt), font= font, fill=coloring)

    if proc:
        position,font = await centrText(f'{dopStat}%', witshRam = 97, razmer = 24, start = 350)
        d.text((position,64), f'{dopStat}%', font= font, fill=coloring)
    else:
        position,font = await centrText(str(dopStat), witshRam = 97, razmer = 24, start = 350)
        d.text((position,64), str(dopStat), font= font, fill=coloring)
    
    return WeaponBg
    
async def constant(characters):
    constantRes = []  
    for key in characters.constellations:
        openConstBg,closedConstBg = openImageElementConstant(characters.element.value, teampt = 3)
        
        openConstBg = openConstBg.resize((87,89))
        closedConstBg = closedConstBg.resize((87,89))
        imageIcon = await imgD(link = key.icon.url)
        imageIcon =  imageIcon.resize((52,52))
        
        if not key.unlocked:
            closedConstBg.alpha_composite(imageIcon, (18,19))
            closedConstBg.alpha_composite(openFile.ClosedConstTree, (20,21))
            
            const = closedConstBg
        else:
            openConstBg.alpha_composite(imageIcon, (18,19))
            const = openConstBg
        constantRes.append(const)
    
    return constantRes


def appendTalat(bg,talantsL):
    position = (597,426)
    for key in talantsL:
        bg.alpha_composite(key, position)
        position = (position[0],position[1]+118)
    return bg

def appendConst(bg,constL):
    position = (22,284)
    for key in constL:
        bg.alpha_composite(key, position)
        position = (position[0],position[1]+72)
    return bg

def appendArt(bg,artif):
    position = (1327,19)
    for key in artif:
        bg.alpha_composite(key, position)
        position = (position[0],position[1]+156)
    return bg

async def stats(AttributeBg,characters,assets):
    g = characters.stats
    elementUp = True
    dopval = {}
    pos = (752,239)
    d = ImageDraw.Draw(AttributeBg)
    for key in g:
        if key[0] in ["BASE_HP","FIGHT_PROP_BASE_ATTACK","FIGHT_PROP_BASE_DEFENSE"]:
            dopval[key[0]] = key[1].value
        if key[1].id in [2000,2001,2002]:
            iconImg = getIconAdd(key[0])
            icon = await imagSize(image = iconImg,fixed_width = 23)
            AttributeBg.alpha_composite(icon,pos)
            txt = assets.get_hash_map(key[0])
            if not key[1].id in stat_perc:
                value = str(math.ceil(key[1].value))
            else:
                value = f"{round(key[1].value * 100, 1)}%"
            x,y = fontSize(24).getsize(value)
            d.text((pos[0]+520-x,pos[1]), value, font = fontSize(24), fill=coloring)
            d.text((pos[0]+41,pos[1]), str(txt), font = fontSize(18), fill=coloring)
            if key[0] in dopStatAtribute:
                dopStatVal = int(dopval[dopStatAtribute[key[0]]])
                dopStatValArtifact = int(key[1].value - dopval[dopStatAtribute[key[0]]])
                if dopStatValArtifact != 0:
                    xx,y = fontSize(15).getsize(f"+{dopStatValArtifact}")
                    d.text((pos[0]+520-xx,pos[1]+30),f"+{dopStatValArtifact}", font = fontSize(15), fill=(141,231,141))
                    x,y = fontSize(15).getsize(f"+{dopStatVal}")
                    d.text((pos[0]+520-x-xx,pos[1]+30),str(dopStatVal), font = fontSize(15), fill=coloring)
            pos = (pos[0],pos[1]+59)
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
        icon = await imagSize(image = iconImg,fixed_width = 23)
        AttributeBg.alpha_composite(icon,pos)

        if not key[1].id in stat_perc:
            value = str(math.ceil(key[1].value))
        else:
            value = f"{round(key[1].value * 100, 1)}%"
        x,y = fontSize(24).getsize(value)
        d.text((pos[0]+520-x,pos[1]), value, font = fontSize(24), fill=coloring)
        d.text((pos[0]+41,pos[1]), str(txt), font = fontSize(18), fill=coloring)
        pos = (pos[0],pos[1]+53)
        
    return AttributeBg

async def naborArtifact(info,ArtifactNameBg):
    count = 0
    for key in info:
        if info[key] > 1:
            count += 1
    if count != 0:
        d = ImageDraw.Draw(ArtifactNameBg)
        ArtifactNameBg.alpha_composite(openFile.ArtifactSetIcon,(749,721))
        position = (1250,722)
        for key in info:
            if info[key] > 1:
                if count == 1:
                    ArtifactNameBg.alpha_composite(openFile.ArtifactSetCount,(1234,738))
                    centrName,fonts = await centrText(key, witshRam = 367 , razmer = 20, start = 840) 
                    d.text((centrName,740), str(key), font= fonts, fill=(141,231,141))
                    d.text((1245 ,739), str(info[key]), font= fontSize(24), fill=coloring)
                    break
                else:
                    ArtifactNameBg.alpha_composite(openFile.ArtifactSetCount,(1234,position[1]))
                    centrName,fonts = await centrText(key, witshRam = 367 , razmer = 20, start = 840) 
                    d.text((centrName,position[1]), str(key), font= fonts, fill=(141,231,141))
                    d.text((1245 ,position[1]), str(info[key]), font= fontSize(24), fill=coloring)
                    position = (position[0],position[1]+28)
    return ArtifactNameBg

async def creatArtifact(infpart,imageStats):
    ArtifactBg = openFile.ArtifactFrame.copy()
    ArtifactBgs = ArtifactBg.copy()
    ArtifactUp = openFile.ArtifactMaska.copy().convert('L')

    artimg = await imagSize(link = infpart.detail.icon.url,size = (233,233))
    ArtifactBg.alpha_composite(artimg,(-57,-53))
    ArtifactBg = Image.composite(ArtifactBg, ArtifactBgs, ArtifactUp)

    d = ImageDraw.Draw(ArtifactBg)
    if str(infpart.detail.mainstats.type) == "DigitType.PERCENT":
        val = f"{infpart.detail.mainstats.value}%"
    else:
        val = infpart.detail.mainstats.value
    x,y = fontSize(32).getsize(str(val))
    d.text((174-x,56), str(val), font= fontSize(32), fill=coloring)
    ArtifactBg.alpha_composite(imageStats,(150,20))
    d.text((136,100), f"+{infpart.level}", font= fontSize(17), fill=coloring)

    starsImg = star(infpart.detail.rarity).resize((83,29))
    ArtifactBg.alpha_composite(starsImg,(51,96))
    cs = 0
    positionIcon = (221,26)
    for key in infpart.detail.substats:
        v = f"+{key.value}"
        if str(key.type) == "DigitType.PERCENT":
            v = f"{v}%"
        imageStats = getIconAdd(key.prop_id, icon = True)
        if not imageStats:
            continue
        imageStats= await imagSize(image = imageStats,fixed_width = 26) 
        ArtifactBg.alpha_composite(imageStats,positionIcon)
        d.text((positionIcon[0]+32,positionIcon[1]), v, font= fontSize(24), fill=coloring)
        cs += 1
        positionIcon = (positionIcon[0]+143,positionIcon[1])
        if cs == 2:
            positionIcon = (221,86)

    return ArtifactBg

async def artifacAdd(characters):
    count = 0
    listArt = {}
    artifacRes = []
    for key in characters.equipments:
        if key.detail.artifact_name_set == "":
            continue
        if not key.detail.artifact_name_set in listArt:
            listArt[key.detail.artifact_name_set] = 1
        else:
            listArt[key.detail.artifact_name_set] += 1

        imageStats = getIconAdd(key.detail.mainstats.prop_id, icon = True, size = (22,27))
        if not imageStats:
            continue

        count += 1
        artifacRes.append(await creatArtifact(key,imageStats))

    return {"artifact": artifacRes, "nabor": listArt}

async def itog(listArt,talansRes,rezConstant,weaponRes,rezArt,signatureRes):
    res = appendTalat(listArt,talansRes)
    res = appendConst(res,rezConstant)
    res = appendArt(res,rezArt)
    res.alpha_composite(weaponRes,(746,33))
    d = ImageDraw.Draw(res)
    d.text((31,757), signatureRes, font= fontSize(24), fill=coloring)

    return res

async def generationTree(characters,assets,img,adapt,signatureRes,lvl, splash):
    person = assets.character(characters.id)
    task = []
    try:
        if splash:
            task.append(characterBackground(person,characters.element.value,img,adapt,characters.image.banner.url))
        else:
            task.append(characterBackground(person,characters.element.value,img,adapt))
        task.append(talants(characters))
        task.append(constant(characters))
        task.append(weapon(characters.equipments[-1],lvl))
        task.append(artifacAdd(characters))

        ec = await asyncio.gather(*task)
        nameRes = await infoCharter(ec[0],characters,lvl)
        statRes = await stats(nameRes,characters,assets)
        listArt = await naborArtifact(ec[4]["nabor"],statRes)
        return await itog(listArt, ec[1],ec[2],ec[3],ec[4]["artifact"],signatureRes)
    except Exception as e:
        raise
        print("ERROR: ", e)