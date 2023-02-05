
import math,re,os,asyncio
from PIL import ImageDraw
from .Generation import *
from .FunctionsPill import imgD,imagSize,centrText
from .options import *
from . import openFile



class Mini:

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
        (316,312),
        (309,373),
        (302,440)
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
        (31,416)
    ]

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


    async def weapon(self,info, nameCharter,element):
        bg = openFile.WEAPON_BG.copy()
        bgTwo = bg.copy()
        linkImgCard = f"https://enka.network/ui/UI_NameCardPic_{nameCharter}_P.png"
        bannerUserNamecard = await imagSize(link = linkImgCard,size = (339,161))
        bg.alpha_composite(bannerUserNamecard,(0,-27))

        #bg.paste(bannerUserNamecard,(0,-27),bannerUserNamecard)
        bg.alpha_composite(openFile.WEAPON_GRANDIENT,(0,0))

        #bg.paste(openFile.WEAPON_GRANDIENT,(0,0),openFile.WEAPON_GRANDIENT)
        bg = Image.composite(bgTwo, bg,openFile.MASKA_WEAPON.convert("L"))
        frame = self.open_frame_weapon_element(element)
        bg.alpha_composite(frame,(0,0))
        #bg.paste(frame,(0,0),frame)
        bg.alpha_composite(openFile.WEAPON_FRAME,(0,0))
        #bg.paste(openFile.WEAPON_FRAME,(0,0),openFile.WEAPON_FRAME)
        image = await imagSize(link = info.detail.icon.url,size = (76,80))
        bg.alpha_composite(image,(18,4))
        #bg.paste(image,(18,4),image)

        name = info.detail.name
        lvl = f"Уровень: {info.level}/90"
        lvlUp = f"R{info.refinement}"
        baseAtt = info.detail.mainstats.value
        imageStats = None
        proc = False
        dopStat = 0

        d = ImageDraw.Draw(bg)
        centrName,fonts = await centrText(name, witshRam = 236, razmer = 15, start = 97) 
        d.text((centrName,11), str(name), font= fonts, fill=coloring)
        d.text((centrName,11), str(name), font= fonts, fill=coloring)
        d.text((137,39), str(baseAtt), font= fontSize(14), fill=coloring)

        for substate in info.detail.substats:
            imageStats = getIconAdd(substate.prop_id, icon = True, size = (20,20))
            if not imageStats:
                continue
            dopStat = substate.value
            if str(substate.type) == "DigitType.PERCENT":
                proc = True
        if imageStats:
            bg.paste(imageStats,(218,37),imageStats)

        if proc:
            d.text((240,39), f"{dopStat}%", font= fontSize(14), fill=coloring)
        else:
            d.text((240,39), str(dopStat), font= fontSize(14), fill=coloring)
        
        d.text((278,65), str(lvlUp), font= fontSize(14), fill=(254,218,154,255))

        d.text((127,65), str(lvl), font= fontSize(14), fill=coloring)

        stars = star(info.detail.rarity)
        bg.alpha_composite(stars,(9,67))
        #bg.paste(stars,(9,67),stars)

        return bg

    async def talants(self,bg,characters):
        i = 0
        talantsBgGold = openFile.TalantsFrameT_GoldTeampleTree.copy()
        talantsBg = openFile.TalantsFrameTeampleTree.copy()
        talantsBgGold = talantsBg.resize((62,61))
        talantsBg = talantsBg.resize((62,61))
        for key in characters.skills:
            if key.level > 9:
                bg.alpha_composite(talantsBgGold,self.positionTalantsFrame[i])
                bg.alpha_composite(talantsBgGold,self.positionTalantsFrame[i])
            else:
                bg.alpha_composite(talantsBg,self.positionTalantsFrame[i])
                bg.alpha_composite(talantsBg,self.positionTalantsFrame[i])

            imagesIconTalants = await imgD(link = key.icon.url)
            imagesIconTalants = imagesIconTalants.resize((34,34))
            bg.alpha_composite(imagesIconTalants, self.positionTalantsIcon[i])
            bg.alpha_composite(imagesIconTalants, self.positionTalantsIcon[i])

            #bg.paste(imagesIconTalants, self.positionTalantsIcon[i],imagesIconTalants)
            #bg.paste(imagesIconTalants, self.positionTalantsIcon[i],imagesIconTalants)

            d = ImageDraw.Draw(bg)
            
            if len(str(key.level)) == 2:
                d.text(self.positionTalantsText[i], str(key.level), font = fontSize(14), fill=coloring)
            else:
                d.text(self.positionTalantsText[i], str(key.level), font = fontSize(14), fill=coloring)
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
                bg.alpha_composite(closedConstBg, self.positionConstFrame[i])
                bg.alpha_composite(imageIcon, self.positionConstIcon[i])
                bg.alpha_composite(closeImg,  self.positionConstIcon[i])

                #bg.paste(closedConstBg, self.positionConstFrame[i],closedConstBg)
                #bg.paste(imageIcon, self.positionConstIcon[i],imageIcon)
                #bg.paste(closeImg,  self.positionConstIcon[i],closeImg)
            else:
                bg.alpha_composite(openConstBg, self.positionConstFrame[i])
                bg.alpha_composite(imageIcon, self.positionConstIcon[i])
                #bg.paste(openConstBg, self.positionConstFrame[i],openConstBg)
                #bg.paste(imageIcon, self.positionConstIcon[i],imageIcon)
            i += 1
        return await self.talants(bg,characters)

    async def creat_bg(self,rarity,element,link,characters,lvl):
        bg,frame = self.open_bg_element(element)
        bgTwo = bg.copy()
        image = await imagSize(link,size = (2048,1024))
        bg.paste(image,(-830,-132),image)
        bg.alpha_composite(openFile.GRANDIENT_BG,(0,0))
        #bg.paste(openFile.GRANDIENT_BG,(0,0),openFile.GRANDIENT_BG)
        bg.alpha_composite(frame,(0,0))
        #bg.paste(frame,(0,0),frame)
        bg = Image.composite(bgTwo, bg,openFile.MASKA_BG.convert("L"))
        imgStar = self.starCharter(rarity)
        bg.alpha_composite(imgStar,(150,7))
        #bg.paste(imgStar,(150,7),imgStar)
        bg.alpha_composite(openFile.FRENDS,(155,537))
        #bg.paste(openFile.FRENDS,(155,537),openFile.FRENDS)
        iconElement = elementIconPanel(element)
        bg.alpha_composite(iconElement,(24,573))
        #bg.paste(iconElement,(24,573),iconElement)

        #==================================================

        d = ImageDraw.Draw(bg)
        centrName,fonts = await centrText(characters.name, witshRam = 326, razmer = 30,start = 14)
        d.text((centrName,474), str(characters.name), font= fonts, fill=coloring)
        lvlText = f"{lvl}: {characters.level}/90"
        centrName,fonts = await centrText(lvlText, witshRam = 151, razmer = 16,start = 101)
        d.text((centrName,515), lvlText, font= fonts, fill=coloring)
        d.text((181,541), str(characters.friendship_level), font = fontSize(20), fill=coloring)
        

        #bg.show()
        bg = await self.addConstant(bg,characters,element)
        return bg



positionStatsIcon = [
    (135,23),
    (130,54),
    (128,85),
    (124,116),
    (120,147),
    (117,178), 
    (114,209),
    (111,240)
]    
    

positionStatsText = [
    (174,25),
    (169,56),
    (167,87),
    (163,118),
    (159,149),
    (156,180),
    (153,211),
    (150,242)
]

positionArtifactIcon = [
    (406,2),
    (406,28),
    (517,2),
    (517,28),
]

positionArtifactText = [
    (429,1),
    (429,25),
    (540,1),
    (540,25),
]

positionArtifact = [
            (21,110),(14,167),(10,227),(3,287),(0,346)
        ]
positionResultat = [
    (13,139),(699,139),(1378,139),(2059,139)
]

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
            return  openFile.PYRO_STAT.copy()


async def stats(g,AttributeBg):
    maxStat = 0
    elementUp = None
    d = ImageDraw.Draw(AttributeBg)
    i = 0
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
       
        
        icon = await imagSize(image = iconImg,fixed_width = 26)

        AttributeBg.paste(icon, positionStatsIcon[i],icon)
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
    d.text((centrName,11), str(val), font= fonts, fill=coloring)
    ArtifactBg.paste(imageStats,(6,3),imageStats)

    d.text((47,26), str(infpart.level), font= fontSize(12), fill=coloring)
    starsImg = star(infpart.detail.rarity).resize((45,13))
    ArtifactBg.paste(starsImg,(7,37),starsImg)
    i = 0

    for key in infpart.detail.substats:
        v = f"+{key.value}"
        if str(key.type) == "DigitType.PERCENT":
            v = f"{v}%"
        imageStats = getIconAdd(key.prop_id, icon = True)
        if not imageStats:
            continue
        imageStats= await imagSize(image = imageStats,fixed_width = 17)
        ArtifactBg.paste(imageStats,positionArtifactIcon[i],imageStats)

        d.text(positionArtifactText[i], v, font= fontSize(15), fill=coloring)
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
        BGT = openFile.ALL_BG.copy()
        positionC = [
            (108,241),(495,241),(882,241),(1269,241),
        ]
        positionW = [
            (166,139),(555,139),(944,139),(1333,139),
        ]
        ran = 0
        for characters in items:
            task = []
            person = assets.character(characters.id)
            task.append(Mini().creat_bg(person.rarity,person.element.value,person.images.banner.url,characters,lang["lvl"]))
            #charter = await Mini().creat_bg(person.rarity,person.element.value,person.images.banner.url,characters,lang["lvl"])
            task.append(Mini().weapon(characters.equipments[-1],characters.image.icon.filename.replace("CostumeFloral","").split("AvatarIcon_")[1],person.element.value))
            #weaponR = await Mini().weapon(characters.equipments[-1],characters.image.icon.filename.replace("CostumeFloral","").split("AvatarIcon_")[1],person.element.value)
            ec = await asyncio.gather(*task)
            BGT.paste(ec[0],(positionC[ran][0],positionC[ran][1]),ec[0])
            BGT.paste(ec[1],(positionW[ran][0],positionW[ran][1]),ec[1])
            ran += 1
        d = ImageDraw.Draw(BGT)
        d.text((77,901), str(userName), font= fontSize(26), fill=coloring)
        d.text((77,935), str(uid), font= fontSize(26), fill=coloring)

    else:
        BGT = openFile.BG_MAX_ALL.copy()
        result = []
        for characters in items:
            BGT_O = openFile.BG_MAX_TEAMPLE.copy()
            i = 0
            person = assets.character(characters.id)
            task = []
            task.append(Mini().creat_bg(person.rarity,person.element.value,person.images.banner.url,characters,lang["lvl"]))
            #charter = await Mini().creat_bg(person.rarity,person.element.value,person.images.banner.url,characters,lang["lvl"])
            task.append(Mini().weapon(characters.equipments[-1],characters.image.icon.filename.replace("CostumeFloral","").split("AvatarIcon_")[1],person.element.value))
            #weaponR = await Mini().weapon(characters.equipments[-1],characters.image.icon.filename.replace("CostumeFloral","").split("AvatarIcon_")[1],person.element.value)
            statBg = open_frame_element(person.element.value)

            task.append(stats(characters.stats,statBg))
            #statsInfo = await stats(characters.stats,statBg)
            task.append(artifactAdd(characters,person.element.value))
            #artBg = await artifactAdd(characters,person.element.value)

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
            BGT.paste(key,(positionResultat[i]),key)
            i += 1            

        d = ImageDraw.Draw(BGT)
        d.text((60,921), str(userName), font= fontSize(26), fill=coloring)
        d.text((60,956), str(uid), font= fontSize(26), fill=coloring)
    return BGT
