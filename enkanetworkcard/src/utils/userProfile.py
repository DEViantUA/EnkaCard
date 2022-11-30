from PIL import ImageDraw,Image,ImageFont
from threading import Thread
from .FunctionsPill import PillImg
import os,queue



path = os.path.dirname(__file__).replace("utils","assets")
font = f'{path}/font/Genshin_Impact.ttf'

t17 = ImageFont.truetype(font, 17)
t12 = ImageFont.truetype(font, 12)

Avatar = Image.open(f'{path}/InfoCharter/AvatarUser.png') 
Maska = Image.open(f'{path}/InfoCharter/AvatarMaska.png').convert('L')
Background = Image.open(f'{path}/InfoCharter/bg.png') 
UserName = Image.open(f'{path}/InfoCharter/UserName.png') 

def characters(player,assets,image,charactersListImageQ,charactersListQ,charactersArgQ):
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
            iconsCharter = PillImg(link = key.icon.url).imagSize(fixed_width = ((50))) 
            lvlCharter = str(key.level)
            d = ImageDraw.Draw(iconCharter)
            iconCharter.paste(iconsCharter,(3,3),iconsCharter)
            d.text((19,56), lvlCharter, font= t12, fill=(255,255,255,255))
            result.append(iconCharter)
    
    charactersListImageQ.put_nowait(result)
    charactersListQ.put_nowait(charterList)
    charactersArgQ.put_nowait(charactersArg)


def creatUserProfile(image,player,lang,hide,uid,assets):
    charactersListImage,charactersList,charactersArg = queue.Queue(),queue.Queue(),queue.Queue()
    Bg = None
    Thread(target=characters,args=(player.characters_preview,assets,image,charactersListImage,charactersList,charactersArg)).start()
    if image:
        bannerUserNamecard = PillImg(link = player.namecard.navbar.url).imagSize(size = (661,105))
        Background.paste(bannerUserNamecard,(123 ,145),bannerUserNamecard)
        picturesProfile = PillImg(link = player.icon.url.url).imagSize(fixed_width = 179).convert('RGBA')
        Avatar.paste(picturesProfile,(0,0),picturesProfile)
        Background.paste(Avatar,(41,110),Maska)
        d = ImageDraw.Draw(Background)
        d.text((556,264), f"{player.abyss_floor}-{player.abyss_room}", font= t17, fill=(73,81,100,255))
        d.text((290,264), str(player.achievement), font= t17, fill=(73,81,100,255))
        d = ImageDraw.Draw(UserName)
        centrName,fonts = PillImg().centrText(player.nickname, witshRam = 181, razmer = 22, start = 0)
        d.text((centrName,0), player.nickname, font= fonts, fill=(255,255,255,255))

        d.text((12,35), f"{lang['AR']}:{player.level}", font= t17, fill=(255,255,255,255))
        d.text((103,35), f"{lang['WL']}:{player.world_level}", font= t17, fill=(255,255,255,255))
        if hide:
            d.text((66,60), "Hidden", font= t12, fill=(255,255,255,255))
        else:
            d.text((66,61), str(uid), font= t12, fill=(255,255,255,255))

        Background.paste(UserName,(221,156),UserName)

        x = 224
        for key in charactersListImage.get():
            Background.paste(key,(x,70),key)
            x = x+66
        Bg = Background
    return {"characters": charactersList.get(), "charactersArg": charactersArg.get()[:-1], "img": Bg}