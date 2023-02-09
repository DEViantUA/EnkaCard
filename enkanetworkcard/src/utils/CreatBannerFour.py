
import math,re,os,asyncio
from PIL import ImageDraw
from .Generation import *
from .FunctionsPill import imgD,imagSize,centrText
from .options import *
from . import openFile
import operator as op

positionStatsIcon = [
    (129,14),
    (125,44),
    (123,73),
    (121,103),
    (119,133),
    (116,163), 
    (112,193),
    (109,223),
    (106,253)
]    
    

positionStatsText = [
    (168,16),
    (164,45),
    (162,75),
    (160,105),
    (158,135),
    (155,165),
    (151,195),
    (148,225),
    (145,255)
]

positionArtifactIcon = [
    (406,2),
    (406,28),
    (517,2),
    (517,28),
]

positionArtifactText = [
    (429,4),
    (429,28),
    (540,4),
    (540,28),
]

positionArtifact = [
            (21,110),(14,167),(10,227),(3,287),(0,346)
        ]
positionResultat = [
    (13,139),(699,139),(1378,139),(2059,139)
]

positionTalantsFrame= [
        (290,270),
        (283,331),
        (276,398)
    ]

positionTalantsIcon= [
    (304,272),
    (297,333),
    (290,400)
]

positionTalantsText= [
    (316,311),
    (309,372),
    (302,439)
]


positionConstFrame = [
    (45,104),
    (41,166),
    (36,225),
    (29,283),
    (24,342),
    (16,400)
]

positionConstIcon = [
    (59,119),
    (56,181),
    (50,240),
    (44,298),
    (38,357),
    (30,416)
]

positionC = [
        (108,241),(495,241),(882,241),(1269,241),
    ]
positionW = [
(166,139),(555,139),(944,139),(1333,139),
]

class Mini:

    def open_bg_element(self,element):
        if element == "Fire":
            return openFile.PYRO_BG.copy(), openFile.PYRO_FRAME.copy()
        elif element== "Grass":
            return openFile.DENDRO_BG.copy(), openFile.DENDRO_FRAME.copy()
        elif element == "Electric":
            return openFile.ELECTRO_BG.copy(), openFile.ELECTRO_FRAME.copy()
        elif element == "Water":
            return openFile.GYDRO_BG.copy(), openFile.GYDRO_FRAME.copy()
        elif element == "Wind":
            return openFile.ANEMO_BG.copy(), openFile.ANEMO_FRAME.copy()
        elif element== "Rock":
            return openFile.GEO_BG.copy(), openFile.GEO_FRAME.copy()
        elif element == "Ice":
            return openFile.CRYO_BG.copy(), openFile.CRYO_FRAME.copy()
        else:
            return openFile.PYRO_BG.copy(), openFile.PYRO_FRAME.copy()

    def open_frame_weapon_element(self,element):
        if element == "Fire":
            return openFile.PYRO_WEAPON.copy()
        elif element== "Grass":
            return openFile.DENDRO_WEAPON.copy()
        elif element == "Electric":
            return openFile.ELECTRO_WEAPON.copy()
        elif element == "Water":
            return openFile.GYDRO_WEAPON.copy()
        elif element == "Wind":
            return openFile.ANEMO_WEAPON.copy()
        elif element== "Rock":
            return openFile.GEO_WEAPON.copy()
        elif element == "Ice":
            return openFile.CRYO_WEAPON.copy()
        else:
            return openFile.PYRO_WEAPON.copy()


    def starCharter(self,x):
        if x == 4:
            imgs = openFile.C_STAR_4
        elif x == 5:
            imgs = openFile.C_STAR_5

        return imgs.copy()


    async def weapon(self,info, nameCharter,element,lvl):
        bg = openFile.WEAPON_BG.copy()
        bgTwo = bg.copy()
        nameCharter = nameCharter.split("Costume")[0]
        if nameCharter in ["PlayerGirl","PlayerBoy"]:
            linkImgCard = "https://api.ambr.top/assets/UI/namecard/UI_NameCardPic_0_P.png"
        else:
            linkImgCard = f"https://enka.network/ui/UI_NameCardPic_{nameCharter}_P.png"
        try:
            bannerUserNamecard = await imagSize(link = linkImgCard,size = (339,161))
        except:
            linkImgCard = f"https://enka.network/ui/UI_NameCardPic_{nameCharter}1_P.png"
            bannerUserNamecard = await imagSize(link = linkImgCard,size = (339,161))
        bg.alpha_composite(bannerUserNamecard,(0,-27))

        bg.alpha_composite(openFile.WEAPON_GRANDIENT,(0,0))

        bg = Image.composite(bgTwo, bg,openFile.MASKA_WEAPON.convert("L"))
        frame = self.open_frame_weapon_element(element)
        bg.alpha_composite(frame,(0,0))
        bg.alpha_composite(openFile.WEAPON_FRAME,(0,0))
        image = await imagSize(link = info.detail.icon.url,size = (76,80))
        bg.alpha_composite(image,(18,4))

        name = info.detail.name
        lvl = f"{lvl}: {info.level}/90"
        lvlUp = f"R{info.refinement}"
        baseAtt = info.detail.mainstats.value
        imageStats = None
        proc = False
        dopStat = 0

        d = ImageDraw.Draw(bg)
        centrName,fonts = await centrText(name, witshRam = 236, razmer = 15, start = 97) 
        d.text((centrName,10), str(name), font= fonts, fill=coloring)
        d.text((centrName,10), str(name), font= fonts, fill=coloring)
        d.text((137,39), str(baseAtt), font= fontSize(14), fill=coloring)

        for substate in info.detail.substats:
            imageStats = getIconAdd(substate.prop_id, icon = True, size = (20,20))
            if not imageStats:
                continue
            dopStat = substate.value
            if str(substate.type) == "DigitType.PERCENT":
                proc = True
        if imageStats:
            bg.alpha_composite(imageStats,(218,37))

        if proc:
            d.text((240,39), f"{dopStat}%", font= fontSize(14), fill=coloring)
        else:
            d.text((240,39), str(dopStat), font= fontSize(14), fill=coloring)
        
        d.text((278,65), str(lvlUp), font= fontSize(14), fill=(254,218,154,255))

        d.text((127,65), str(lvl), font= fontSize(14), fill=coloring)

        stars = star(info.detail.rarity)
        bg.alpha_composite(stars,(9,67))

        return bg

    async def talants(self,bg,characters):
        i = 0
        talantsBgGold = openFile.TalantsFrameT_GoldTeampleTree.copy()
        talantsBg = openFile.TalantsFrameTeampleTree.copy()
        talantsBgGold = talantsBg.resize((62,61))
        talantsBg = talantsBg.resize((62,61))
        for key in characters.skills:
            if key.level > 9:
                bg.alpha_composite(talantsBgGold,positionTalantsFrame[i])
            else:
                bg.alpha_composite(talantsBg,positionTalantsFrame[i])

            imagesIconTalants = await imgD(link = key.icon.url)
            imagesIconTalants = imagesIconTalants.resize((34,34))
            bg.alpha_composite(imagesIconTalants, positionTalantsIcon[i])

            d = ImageDraw.Draw(bg)
            
            if len(str(key.level)) == 2:
                d.text((positionTalantsText[i][0]-1,positionTalantsText[i][1]), str(key.level), font = fontSize(14), fill=(250,188,87,255))
            else:
                d.text(positionTalantsText[i], str(key.level), font = fontSize(14), fill=coloring)
            i += 1
        return bg

    async def addConstant(self,bg,characters,element):
        i = 0
        closeImg = openFile.ClosedConstTree
        closeImg = closeImg.resize((32,32))

        openConstBg,closedConstBg = openImageElementConstant(element, teampt = 3)
        openConstBg = openConstBg.resize((60,62))
        closedConstBg = closedConstBg.resize((60,62))
        for key in characters.constellations:
            imageIcon = await imgD(link = key.icon.url)
            imageIcon = imageIcon.resize((32,32))

            if not key.unlocked:
                bg.alpha_composite(closedConstBg, positionConstFrame[i])
                bg.alpha_composite(imageIcon, positionConstIcon[i])
                bg.alpha_composite(closeImg,  positionConstIcon[i])
            else:
                bg.alpha_composite(openConstBg, positionConstFrame[i])
                bg.alpha_composite(imageIcon, positionConstIcon[i])
            i += 1
        return await self.talants(bg,characters)

    async def creat_bg(self,rarity,element,link,characters,lvl, chartImg):
        bg,frame = self.open_bg_element(element)
        bgTwo = bg.copy()
        if chartImg != None:
            image,posX = centryImage(chartImg, teample = 4)
            bg.alpha_composite(image,(posX,0))
        else:
            image = await imagSize(link,size = (2048,1024))
            bg.alpha_composite(image,(-830,-132))
        bg.alpha_composite(openFile.GRANDIENT_BG,(0,0))
        bg.alpha_composite(frame,(0,0))
        bg = Image.composite(bgTwo, bg,openFile.MASKA_BG.convert("L"))
        imgStar = self.starCharter(rarity)
        bg.alpha_composite(imgStar,(150,7))
        iconElement = elementIconPanel(element)
        bg.alpha_composite(iconElement,(24,573))

        #==================================================

        d = ImageDraw.Draw(bg)
        centrName,fonts = await centrText(characters.name, witshRam = 326, razmer = 30,start = 14)
        d.text((centrName,500), str(characters.name), font= fonts, fill=coloring)
        lvlText = f"{lvl}: {characters.level}/90 |"
        centrName,fonts = await centrText(lvlText, witshRam = 151, razmer = 17,start = 75)
        d.text((centrName,543), lvlText, font= fonts, fill=coloring)
        positionIconFriends = centrName + fonts.getsize(lvlText)[0] + 7

        d.text((positionIconFriends+27,540), str(characters.friendship_level), font = fontSize(20), fill=coloring)
        bg.alpha_composite(openFile.FRENDS,(positionIconFriends,536))
        bg = await self.addConstant(bg,characters,element)
        return bg


def open_frame_element(element, artifact = False):
    if artifact:
        if element == "Fire":
            return openFile.PYRO_ART.copy()
        elif element== "Grass":
            return openFile.DENDRO_ART.copy()
        elif element == "Electric":
            return openFile.ELECTRO_ART.copy()
        elif element == "Water":
            return openFile.GYDRO_ART.copy()
        elif element == "Wind":
            return openFile.ANEMO_ART.copy()
        elif element== "Rock":
            return openFile.GEO_ART.copy()
        elif element == "Ice":
            return openFile.CRYO_ART.copy()
        else:
            return openFile.PYRO_ART.copy()
    else:
        if element == "Fire":
            return openFile.PYRO_STAT.copy()
        elif element== "Grass":
            return openFile.DENDRO_STAT.copy()
        elif element == "Electric":
            return openFile.ELECTRO_STAT.copy()
        elif element == "Water":
            return  openFile.GYDRO_STAT.copy()
        elif element == "Wind":
            return openFile.ANEMO_STAT.copy()
        elif element== "Rock":
            return openFile.GEO_STAT.copy()
        elif element == "Ice":
            return openFile.CRYO_STAT.copy()
        else:
            return openFile.PYRO_STAT.copy()


async def stats(g,AttributeBg):
    elementUp = True
    d = ImageDraw.Draw(AttributeBg)
    i = 0

    for key in g:
        if key[1].id in [2000,2001,2002]:
            iconImg = getIconAdd(key[0])
            icon = await imagSize(image = iconImg,fixed_width = 22)
            AttributeBg.alpha_composite(icon,positionStatsIcon[i])
            if not key[1].id in stat_perc:
                value = str(math.ceil(key[1].value))
            else:
                value = f"{round(key[1].value * 100, 1)}%"
            d.text(positionStatsText[i], value, font = fontSize(20), fill=coloring)
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
        iconImg = getIconAdd(key[0])
        if not iconImg:
            continue
        icon = await imagSize(image = iconImg,fixed_width = 22)
        AttributeBg.alpha_composite(icon, positionStatsIcon[i])
        if not key[1].id in stat_perc:
            value = str(math.ceil(key[1].value))
        else:
            value = f"{round(key[1].value * 100, 1)}%"

        d.text(positionStatsText[i], value, font = fontSize(20), fill=coloring)

        i += 1
    return AttributeBg
    

async def creatArtifact(infpart,ArtifactBg,imageStats):
    ArtifactUp = openFile.FRAME_ART.copy()
    artimg = await imagSize(link = infpart.detail.icon.url,size = (65,72))
    ArtifactBg.alpha_composite(artimg,(3,-8))
    ArtifactBg.alpha_composite(ArtifactUp,(0,0))
    
    d = ImageDraw.Draw(ArtifactBg)
    if str(infpart.detail.mainstats.type) == "DigitType.PERCENT":
        val = f"{infpart.detail.mainstats.value}%"
    else:
        val = infpart.detail.mainstats.value
    centrName,fonts = await centrText(val, witshRam = 34, razmer = 10, start = 39)
    d.text((centrName,11), str(val), font= fonts, fill=(0,0,0,0))
    d.text((centrName,10), str(val), font= fonts, fill=coloring)
    ArtifactBg.alpha_composite(imageStats,(6,3))

    d.text((47,26), str(infpart.level), font= fontSize(12), fill=coloring)
    starsImg = star(infpart.detail.rarity).resize((45,13))
    ArtifactBg.alpha_composite(starsImg,(7,37))
    i = 0

    for key in infpart.detail.substats:
        v = f"+{key.value}"
        if str(key.type) == "DigitType.PERCENT":
            v = f"{v}%"
        imageStats = getIconAdd(key.prop_id, icon = True)
        if not imageStats:
            continue
        imageStats= await imagSize(image = imageStats,fixed_width = 17)
        ArtifactBg.alpha_composite(imageStats,positionArtifactIcon[i])

        d.text(positionArtifactText[i], v, font= fontSize(16), fill=coloring)
        i += 1
    return ArtifactBg

async def artifactAdd(characters,element):
    resurs = []
    for key in characters.equipments:
        AttributeBg = open_frame_element(element, artifact = True)
        if key.detail.artifact_name_set == "":
            continue
        imageStats = getIconAdd(key.detail.mainstats.prop_id, icon = True, size = (18,18))
        if not imageStats:
            continue
        resurs.append(await creatArtifact(key,AttributeBg,imageStats))
        
    return resurs
    
async def generationFour(items,assets,lang, mini = True, userName = "User", uid = "UID: Hide"):
    if mini:
        BGT = openFile.ALL_BG.copy().convert("RGBA")
        if len(items) == 3:
            BGT = BGT.crop((0,0,1416,997))
        elif len(items) == 2:
            BGT = BGT.crop((0,0,1051,997))
        elif len(items) == 1:
            BGT = BGT.crop((0,0,623,997))
        ran = 0
        for characters in items:
            charactersImg = characters[1]
            characters = characters[0]
            task = []
            person = assets.character(characters.id)
            task.append(Mini().creat_bg(person.rarity,characters.element.value,person.images.banner.url,characters,lang["lvl"],charactersImg))
            task.append(Mini().weapon(characters.equipments[-1],characters.image.icon.filename.replace("CostumeFloral","").split("AvatarIcon_")[1],characters.element.value,lang["lvl"]))
            ec = await asyncio.gather(*task)
            BGT.alpha_composite(ec[0],(positionC[ran][0],positionC[ran][1]))
            BGT.alpha_composite(ec[1],(positionW[ran][0],positionW[ran][1]))
            ran += 1
        d = ImageDraw.Draw(BGT)
        d.text((77,901), str(userName), font= fontSize(26), fill=coloring)
        d.text((77,935), str(uid), font= fontSize(26), fill=coloring)

    else:
        BGT = openFile.BG_MAX_ALL.copy().convert("RGBA")
        if len(items) == 3:
            BGT = BGT.crop((0,0,2047,997))
        elif len(items) == 2:
            BGT = BGT.crop((0,0,1355,997))
        elif len(items) == 1:
            BGT = BGT.crop((0,0,678,997))

        result = []
        for characters in items:
            charactersImg = characters[1]
            characters = characters[0]
            BGT_O = openFile.BG_MAX_TEAMPLE.copy()
            i = 0
            person = assets.character(characters.id)
            task = []
            task.append(Mini().creat_bg(person.rarity,characters.element.value,person.images.banner.url,characters,lang["lvl"],charactersImg))
            task.append(Mini().weapon(characters.equipments[-1],characters.image.icon.filename.replace("CostumeFloral","").split("AvatarIcon_")[1],characters.element.value,lang["lvl"]))
            statBg = open_frame_element(characters.element.value)

            task.append(stats(characters.stats,statBg))
            task.append(artifactAdd(characters,characters.element.value))

            ec = await asyncio.gather(*task)

            BGT_O.alpha_composite(ec[2],(278,408))
            
            BGT_O.alpha_composite(ec[1],(94,0))
            for key in ec[3]:
                BGT_O.alpha_composite(key,positionArtifact[i])
                i += 1
            BGT_O.alpha_composite(ec[0],(35,102))
            result.append(BGT_O)
        i = 0
        
        for key in result:
            BGT.alpha_composite(key,(positionResultat[i]))
            i += 1            

        d = ImageDraw.Draw(BGT)
        d.text((60,921), str(userName), font= fontSize(26), fill=coloring)
        d.text((60,956), str(uid), font= fontSize(26), fill=coloring)
    return BGT
