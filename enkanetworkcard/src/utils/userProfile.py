from PIL import ImageDraw,Image,ImageFont
from .FunctionsPill import imagSize,centrText
import os
import time
from . import openFile

path = os.path.dirname(__file__).replace("utils","assets")

async def characters(player,assets,image):
    t12 = ImageFont.truetype(openFile.font, 12)
    result = []
    charterList = {}
    charactersArg = ""
    for key in player:
        person = assets.character(key.id)
        if not key.name in charterList:
            charterList[key.name] = {"rarity": person.rarity, "image": key.icon.url, "element": person.element.value}
            charactersArg += f"{key.name},"
        if image:
            if person.rarity == 4:
                iconCharter = Image.open(f'{path}/InfoCharter/iconCharter4.png')
            else:
                iconCharter = Image.open(f'{path}/InfoCharter/iconCharter5.png')
            iconsCharter = await imagSize(link = key.icon.url, fixed_width = 50) 
            lvlCharter = str(key.level)
            d = ImageDraw.Draw(iconCharter)
            iconCharter.paste(iconsCharter,(3,3),iconsCharter)
            d.text((19,56), lvlCharter, font= t12, fill=(255,255,255,255))
            result.append(iconCharter)
    
    return result,charterList,charactersArg



async def creatUserProfile(image,player,lang,hide,uid,assets):
    t12 = ImageFont.truetype(openFile.font, 12)
    t17 = ImageFont.truetype(openFile.font, 17)
    
    Avatar = Image.open(f'{path}/InfoCharter/AvatarUser.png') 
    Background = Image.open(f'{path}/InfoCharter/bg.png') 
    UserName = Image.open(f'{path}/InfoCharter/UserName.png')
    start = time.time()
    Bg = None
    charactersListImage,charactersList,charactersArg = await characters(player.characters_preview,assets,image)
    if image:
        bannerUserNamecard = await imagSize(link = player.namecard.navbar.url, size = (661,105))
        Background.paste(bannerUserNamecard,(123 ,145),bannerUserNamecard)
        picturesProfile = await imagSize(link = player.avatar.icon.url,fixed_width = 179)
        picturesProfile = picturesProfile.convert('RGBA')
        Avatar.paste(picturesProfile,(0,0),picturesProfile)
        Background.paste(Avatar,(41,110),openFile.MaskaInfoUser.convert("L"))
        d = ImageDraw.Draw(Background)
        d.text((556,264), f"{player.abyss_floor}-{player.abyss_room}", font= t17, fill=(73,81,100,255))
        d.text((290,264), str(player.achievement), font= t17, fill=(73,81,100,255))
        d = ImageDraw.Draw(UserName)
        centrName,fonts = await centrText(player.nickname, witshRam = 181, razmer = 22, start = 0)
        d.text((centrName,0), player.nickname, font= fonts, fill=(255,255,255,255))

        d.text((12,35), f"{lang['AR']}:{player.level}", font= t17, fill=(255,255,255,255))
        d.text((103,35), f"{lang['WL']}:{player.world_level}", font= t17, fill=(255,255,255,255))
        if hide:
            d.text((66,60), "Hidden", font= t12, fill=(255,255,255,255))
        else:
            d.text((66,61), str(uid), font= t12, fill=(255,255,255,255))

        Background.paste(UserName,(221,156),UserName)

        x = 224
        for key in charactersListImage:
            Background.paste(key,(x,70),key)
            x = x+66
        Bg = Background
    return {"characters": charactersList, "charactersArg": charactersArg, "img": Bg, "performed":float('{:.2f}'.format(time.time()-start))}