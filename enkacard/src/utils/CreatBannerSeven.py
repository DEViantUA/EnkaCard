from . import Generation as gen
from .FunctionsPill import imagSize,imgD
from .options import fontSize
from PIL import ImageDraw,Image
from . import openFile as of
from . import options
import math,asyncio






async def background(imgs,splash,element,signatureRes,characters,player, lvl):
    if splash:
        try:
            imgs = await imagSize(link = imgs,size = (1428,711))
            frame = await gen.creatSevenBg(imgs, element = element)
        except:
            raise
    else:
        frame = await gen.creatSevenBg(imgs, element = element, adapt = True)
    d = ImageDraw.Draw(frame)
    x = fontSize(28).getlength(characters.name)
    z = int(fontSize(28).getlength(player.nickname))
    name = Image.new("RGBA", (z+2,18), (255,255,255,0))
    draw = ImageDraw.Draw(name)
    draw.text((0,0), player.nickname, font= gen.fontSize(15), fill=(255,255,255,100))

    #d.text((int(38+x+34+7),42), player.nickname, font= gen.fontSize(15), fill=(255,255,255,50))
    d.text((38,326), signatureRes, font= gen.fontSize(17), fill=options.coloring)
    d.text((38,33), characters.name, font= gen.fontSize(28), fill=options.coloring)
    frame.alpha_composite(of.Triangle,(int(38+x+17),47))
    frame.alpha_composite(name,(int(38+x+34+7),42))
    level = f'{lvl["lvl"]}: {characters.level}/'
    x = fontSize(28).getlength(level)
    d.text((38,74), level, font= gen.fontSize(28), fill=options.coloring)
    frame.alpha_composite(of.max_lvl,(int(38+x+2),77))
    d.text((79,117), str(characters.friendship_level), font= gen.fontSize(23), fill=options.coloring)
    d.text((38,352), f'{lvl["WL"]}:', font= gen.fontSize(17), fill=options.coloring)
    d.text((93,351), str(player.world_level), font= gen.fontSize(17), fill=(245,222,179,255))
    
    return frame

async def stats(AttributeBg,characters,assets):
    g = characters.stats
    elementUp = True
    dopval = {}
    posText = [
        561,
        606,
        651,
        696,
        741,
        786,
        831,
        875
    ]
    posDopVal = [
        570,
        615,
        660
    ]

    posVal = [
        550,
        595,
        640,
        695,
        740,
        785,
        830,
        874
    ]

    posIcon = [
        558,
        606,
        651,
        693,
        738,
        783,
        828,
        872
    ]
    d = ImageDraw.Draw(AttributeBg)
    i = 0
    for key in g:
        if key[0] in ["BASE_HP","FIGHT_PROP_BASE_ATTACK","FIGHT_PROP_BASE_DEFENSE"]:
            dopval[key[0]] = key[1].value
        if key[1].id in [2000,2001,2002]:
            iconImg = gen.getIconAdd(key[0])
            icon = await imagSize(image = iconImg,fixed_width = 18)
            AttributeBg.alpha_composite(icon,(46,posIcon[i]))
            txt = assets.get_hash_map(key[0])
            if not key[1].id in options.stat_perc:
                value = str(math.ceil(key[1].value))
            else:
                value = f"{round(key[1].value * 100, 1)}%"
            x = fontSize(18).getlength(value)

            
            d.text((int(450-x),posVal[i]), value, font = fontSize(18), fill=options.coloring)
            d.text((88,posText[i]), str(txt), font = fontSize(18), fill=options.coloring)

            if key[0] in options.dopStatAtribute:
                dopStatVal = int(dopval[options.dopStatAtribute[key[0]]])
                dopStatValArtifact = int(key[1].value - dopval[options.dopStatAtribute[key[0]]])

                if dopStatValArtifact != 0:
                    dopStatValArtifact = f"+{dopStatValArtifact}"
                    xx= fontSize(12).getlength(dopStatValArtifact)
                    d.text((int(450-xx),posDopVal[i]),dopStatValArtifact, font = fontSize(12), fill=(141,231,141))
                    x= fontSize(12).getlength(str(dopStatVal))
                    d.text((int(450-xx-x-2), posDopVal[i]),str(dopStatVal), font = fontSize(12), fill=options.coloring)
            i += 1

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
        icon = await imagSize(image = iconImg,fixed_width = 18)
        AttributeBg.alpha_composite(icon,(46,posIcon[i]))

        if not key[1].id in options.stat_perc:
            value = str(math.ceil(key[1].value))
        else:
            value = f"{round(key[1].value * 100, 1)}%"
        x = fontSize(18).getlength(value)
        d.text((int(450-x),posVal[i]), value, font = fontSize(18), fill=options.coloring)
        d.text((88,posText[i]), str(txt), font = fontSize(18), fill=options.coloring)

        i += 1

    return AttributeBg

async def weapon(WeaponBg,characters,lvlName):
    if characters.detail.artifact_name_set != "":
        return None
    d = ImageDraw.Draw(WeaponBg)
    proc = False    
    name = characters.detail.name
    lvl = characters.level
    lvlUp = characters.refinement
    baseAtt = characters.detail.mainstats.value
    imageStats = None
    dopStat = 0

    for substate in characters.detail.substats:
        imageStats = gen.getIconAdd(substate.prop_id, icon = True, size = (26,26))
        if not imageStats:
            continue
        dopStat = substate.value
        if str(substate.type) == "DigitType.PERCENT":
            proc = True
    if imageStats:
        WeaponBg.alpha_composite(imageStats,(293,445))

    stars = await gen.starFive(characters.detail.rarity)
    image = await imagSize(link = characters.detail.icon.url,size = (120,125))

    WeaponBg.alpha_composite(image,(38,400))
    WeaponBg.alpha_composite(stars,(6,517))
    mv = of.max_lvl.copy()
    
    d.text((174,406), str(name), font= gen.fontSize(22), fill=options.coloring) 
    d.text((184,488), f"R{lvlUp}", font= gen.fontSize(20), fill=(245,222,179,255))
    level = f"{lvlName}: {lvl}/90"
    x = fontSize(20).getlength(level)
    WeaponBg.alpha_composite(mv.resize((28,18)), (int(320-x/2+x)-25,491))
    d.text((int(320-x/2),488), f"{lvlName}: {lvl}/", font= gen.fontSize(20), fill=options.coloring) 
    d.text((220,447), str(baseAtt), font= gen.fontSize(20), fill=options.coloring)

    if proc:
        d.text((332,447), f'{dopStat}%', font= gen.fontSize(20), fill=options.coloring)
    else:
        d.text((332,447), str(dopStat), font= gen.fontSize(20), fill=options.coloring)
    return WeaponBg

positionTalants = [
    26,
    117,
    207
]

positionTalantsValue = [
    74, 
    166,
    255
]
async def talants(talantsBg,skills):
    i = 0
    for key in skills:
        if key.level > 9:
            coloring= (255,198,0,255)
        else:
            coloring = (255,255,255,255)

        d = ImageDraw.Draw(talantsBg)
        imagesIconTalants = await imgD(link = key.icon.url)
        imagesIconTalants = imagesIconTalants.resize((44,44))
        talantsBg.alpha_composite(imagesIconTalants, (849,positionTalants[i]))

        x = fontSize(19).getlength(str(key.level))
        d.text((int(871-x/2),positionTalantsValue[i]), str(key.level), font = fontSize(19), fill=coloring)

        i += 1
    return talantsBg

async def const(charter):
    constantRes = []  
    for key in charter.constellations:
        openConstBg,closedConstBg = gen.openImageElementConstant(charter.element.value, teampt = 3)
        imageIcon = await imgD(link = key.icon.url)
        imageIcon =  imageIcon.resize((41,41))
        
        if not key.unlocked:
            closedConstBg = closedConstBg.resize((73,76))
            closedConstBg.alpha_composite(closedConstBg, (0,0))
            closedIcon = of.ClosedConstTree.resize((47,48))
            closedConstBg.alpha_composite(closedConstBg, (0,0))
            closedConstBg.alpha_composite(imageIcon, (16,18))
            closedConstBg.alpha_composite(closedIcon, (12,15))
            
            const = closedConstBg
        else:
            openConstBg = openConstBg.resize((73,76))
            openConstBg.alpha_composite(openConstBg, (0,0))
            openConstBg.alpha_composite(imageIcon, (16,18))
            const = openConstBg
        constantRes.append(const)
    
    return constantRes

async def addConst(bg,items):
    pos = [
        241,320,401,482,561,642
    ]
    i = 0
    for key in items:
        bg.alpha_composite(key, (pos[i],316))
        i += 1
    return bg



positionIconArtifact = ((185,19),(310,19), (185,65),(310,65))
positionTextArtifact = ((217,21),(342,21), (217,66),(342,66))

async def artifact(characters):
    
    TOTAL_CV = 0
    artifactData = []
    listArt = {}
    for infpart in characters:
        CRIT_DMG = 0
        CRIT_RATE = 0
        if infpart.detail.artifact_name_set == "":
            continue
        if not infpart.detail.artifact_name_set in listArt:
            listArt[infpart.detail.artifact_name_set] = 1
        else:
            listArt[infpart.detail.artifact_name_set] += 1

        ArtifactBgOn = of.ART_bg_SEVEN.copy()
        ArtifactBg = of.ART_bg_SEVEN.copy()
        ART_frame_SEVEN = of.ART_frame_SEVEN.copy()
        ART_maska_SEVEN = of.ART_maska_SEVEN.convert('L')

        artimg = await imagSize(link = infpart.detail.icon.url,size = (159,190))
        ArtifactBgOn.alpha_composite(artimg,(-20,-39))
        ArtifactBg = Image.composite(ArtifactBg, ArtifactBgOn, ART_maska_SEVEN)
        ArtifactBg.alpha_composite(ART_frame_SEVEN,(0,0))
        d = ImageDraw.Draw(ArtifactBg)



        if str(infpart.detail.mainstats.type) == "DigitType.PERCENT":
            val = f"{infpart.detail.mainstats.value}%"
        else:
            val = str(infpart.detail.mainstats.value)

        x = fontSize(26).getlength(val)
        d.text((int(138-x),43), val, font= gen.fontSize(26), fill=options.coloring)
        x = fontSize(14).getlength(f"+{infpart.level}")
        d.text((int(125-x/2),77), f"+{infpart.level}", font= gen.fontSize(14), fill=options.coloring)

        starsImg = gen.star(infpart.detail.rarity)

        ArtifactBg.alpha_composite(starsImg.resize((78,25)),(25,76))
        imageStats = gen.getIconAdd(infpart.detail.mainstats.prop_id, icon = True, size = (19,24))
        ArtifactBg.alpha_composite(imageStats,(121,14)) 

        if infpart.detail.mainstats.prop_id == "FIGHT_PROP_CRITICAL_HURT":
            CRIT_DMG += infpart.detail.mainstats.value
        if infpart.detail.mainstats.prop_id == "FIGHT_PROP_CRITICAL":
            CRIT_RATE += infpart.detail.mainstats.value

        

        i = 0
        for key in infpart.detail.substats:
            v = f"+{key.value}"
            if str(key.type) == "DigitType.PERCENT":
                v = f"{v}%"
            imageStats = gen.getIconAdd(key.prop_id, icon = True)
            if not imageStats:
                continue
            imageStats= await imagSize(image = imageStats,fixed_width = 22) 
            ArtifactBg.alpha_composite(imageStats,positionIconArtifact[i])
            d.text(positionTextArtifact[i], v, font= gen.fontSize(19), fill=options.coloring)
            if key.prop_id == "FIGHT_PROP_CRITICAL_HURT":
                CRIT_DMG += key.value
            if key.prop_id == "FIGHT_PROP_CRITICAL":
                CRIT_RATE +=key.value

            i += 1
        tcvR = float('{:.2f}'.format(CRIT_DMG + (CRIT_RATE*2)))
        TCV = f"{tcvR}CV"
        TOTAL_CV += tcvR
        x = fontSize(15).getlength(TCV)
        d.text((int(43-x/2),6), TCV, font= gen.fontSize(15), fill=options.coloring)
        artifactData.append(ArtifactBg)

    return {"art": artifactData, "set": listArt, "TCV": float('{:.2f}'.format(TOTAL_CV))}


async def artifactAdd(bg,items,TCV,sets):
    positionArtifact = [400,519,638,757,876]
    i = 0
    for key in items:
        bg.alpha_composite(key,(480,positionArtifact[i]))
        i += 1
    d = ImageDraw.Draw(bg)
    x = fontSize(19).getlength(f"{TCV}TCV")
    d.text((int(860-x/2),353), f"{TCV}TCV", font= gen.fontSize(19), fill=options.coloring)

    if sets != {}:
        max_val = max(sets.values())
        max_keys = [k for k, v in sets.items() if v == max_val]
        if max_val == 4:
            result = max_keys[0]
        else:
            unique_vals = list(set(sets.values()))
            if unique_vals.count(2) == 2:
                result = [k for k, v in sets.items() if v == 2]
            elif 2 in unique_vals and 3 in unique_vals:
                result = [k for k, v in sets.items() if v in [2, 3]]
            else:
                result = max_keys[:2]
        if len(result) == 2 and type(result) == list:
            position,coun  = [923,951],[922,950]
        else:
            if type(result) == str:
                result = [result]
            position,coun = [937],[936]
        i = 0
        for key in result:
            if sets[key] != 1:
                x = fontSize(16).getlength(key)
                d.text((int(256-x/2),position[i]), key, font= gen.fontSize(16), fill=(127,229,164,255))
                counts = of.COUNTS.copy()
                dc = ImageDraw.Draw(counts)
                dc.text((9,0), str(sets[key]), font= gen.fontSize(18), fill=options.coloring)
                bg.alpha_composite(counts,(422,coun[i]))
                i += 1
        
    return bg

'''async def generationSeven(characters,assets,img,lvl,splash,signatureRes,player):
    person = assets.character(characters.id)
    task = []
    if img != None:
        task.append(background(img,False,characters.element,signatureRes,characters,player,lvl))
    else:
        if splash:
            task.append(background(characters.image.banner.url,True,characters.element,signatureRes,characters,player,lvl))
        else:
            task.append(background(person.images.banner.url,True,characters.element,signatureRes,characters,player,lvl))
    task.append(const(characters))
    task.append(artifact(characters.equipments))
    res = await asyncio.gather(*task)
    bg = await weapon(res[0],characters.equipments[-1],lvl["lvl"])
    bg = await stats(bg,characters,assets)
    bg = await stats(bg,characters,assets)
    bg = await talants(bg,characters.skills)
    bg = await addConst(bg,res[1])
    bg = await artifactAdd(bg,res[2]["art"],res[2]["TCV"],res[2]["set"])

    return bg'''

async def generationSeven(characters, assets, img, lvl, splash, signatureRes, player):
    person = assets.character(characters.id)
    task = []
    if img:
        task.append(background(img, False, characters.element, signatureRes, characters, player, lvl))
    else:
        task.append(background(characters.image.banner.url, True, characters.element, signatureRes, characters, player, lvl) if splash else background(person.images.banner.url, True, characters.element, signatureRes, characters, player, lvl))
    task.extend((const(characters), artifact(characters.equipments)))
    res = await asyncio.gather(*task)
    bg = await weapon(res[0], characters.equipments[-1], lvl["lvl"])
    bg = await stats(bg, characters, assets)
    bg = await talants(bg, characters.skills)
    bg = await addConst(bg, res[1])
    bg = await artifactAdd(bg, res[2]["art"], res[2]["TCV"], res[2]["set"])

    return bg