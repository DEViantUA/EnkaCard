# Copyright 2022 DEViantUa <t.me/deviant_ua>
# All rights reserved.
from PIL import Image
import threading
from weakref import WeakValueDictionary
from pathlib import Path

lock = threading.Lock()
cache = WeakValueDictionary()
assets = Path(__file__).parent.parent / 'assets'


font = str(assets / 'font' / 'Genshin_Impact.ttf')


#=================Artifact==================

mapping = {
    'MaskaInfoUser': assets/'InfoCharter'/'AvatarMaska.png',

    'EffectBgTeampleTree': assets/'teapmleTree'/'background'/'EFFECT_DARK.png',

    'ArtifactSetIcon': assets/'teapmleTree'/'artifact'/'ICON.png',
    'ArtifactSetCount': assets/'teapmleTree'/'artifact'/'COUNT.png',

    'ArtifactFrame': assets/'teapmleTree'/'artifact'/'FRAME.png',
    'ArtifactMaska': assets/'teapmleTree'/'artifact'/'maska.png',

    'WeaponBgTeampleTree': assets/'teapmleTree'/'weapon'/'WEAPON_FRAME.png',
    'WeaponLight': assets/'teapmleTree'/'weapon'/'LIGHT.png',

    'TalantsFrameTeampleTree': assets/'teapmleTree'/'talants'/'TALANTS_FRAME.png',
    'TalantsFrameT_GoldTeampleTree': assets/'teapmleTree'/'talants'/'TALANTS_FRAME_GOLD.png',

    'UserBgTeampleTree': assets/'teapmleTree'/'maska'/'USER_BG_SPLASH.png',
    'UserBgTeampleImgTree': assets/'teapmleTree'/'maska'/'USER_BG_IMG.png',
    'EffectBgTree': assets/'teapmleTree'/'maska'/'EFFECT.png',
    'ClosedConstTree': assets/'teapmleTree'/'constant'/'closed'/'CLOSED.png',
    #===========
    'TalantsFrameTeampleOne': assets/'teapmleOne'/'talants'/'TALANTS_FRAME.png',
    'TalantsFrameGoldLvlTeampleOne': assets/'teapmleOne'/'talants'/'TALANTS_FRAME_GOLD_LVL.png',
    'TalantsCountTeampleOne': assets/'teapmleOne'/'talants'/'TALANTS_COUNT.png',

    'AttributeTeampleOne': assets/'teapmleOne'/'stats'/'STATS.png',
    'AttributeBgTeampleOne': assets/'teapmleOne'/'stats'/'STATS_FRAME.png',
    'AttributeDopValueTeampleOne': assets/'teapmleOne'/'stats'/'STATS_DOP_VALUE.png',

    'UserBgTeampleOne': assets/'teapmleOne'/'maska'/'ADAPTATION.png',
    'UserEffectTeampleOne': assets/'teapmleOne'/'maska'/'ADAPTATION5.png',
    'MaskaBgTeampleOne': assets/'teapmleOne'/'maska'/'maska.png',
    'MaskaUserBgTeampleOne': assets/'teapmleOne'/'maska'/'maskaUserArt.png',
    'MaskaUserBg2TeampleOne': assets/'teapmleOne'/'maska'/'ADAPTATION2.png',

    'ClossedBg': assets /'constant'/'CLOSED_BG.png',
    'Clossed': assets /'constant'/'CLOSED.png',
    'ConstantBG': assets /'constant'/'CONSTATN_BG.png',
    'StarBg': assets /'stars'/'bg.png',
    'SignatureOne': assets /'SIGNATURE.png',
    'SignatureTwo': assets /'SIGNATURE3.png',


    'FRENDS': assets /'icon'/'FRIENDS.png',
    'ErrorBgTeampleOne': assets /'teapmleOne'/'background'/'ERROR.png',

    'ArtifactNameBgTeampleOne': assets/'teapmleOne'/'artifact'/'ARTIFACT_SET_BG.png',
    'ArtifactNameFrameTeampleOne': assets/'teapmleOne'/'artifact'/'ARTIFACT_SET_FRAME.png',

    'ArtifactBgTeampleOne': assets/'teapmleOne'/'artifact'/'ARTIFACT_BG.png',
    'ArtifactBgUpTeampleOne': assets/'teapmleOne'/'artifact'/'ARTIFACT_UP.png',
    'ArtifactDopValueTeampleOne': assets/'teapmleOne'/'artifact'/'ARTIFACT_BG_DOP_VAL.png',

    'WeaponBgTeampleOne': assets/'teapmleOne'/'weapons'/'WEAPON_FRAME_TWO.png',
    'WeaponBgUpTeampleOne': assets/'teapmleOne'/'weapons'/'WEAPON_FRAME_TWO_UP.png',

    'NameBgTeampleOne': assets/'teapmleOne'/'charterInfo'/'CHARTER_FRAME.png',
    #===========================

    'ErrorBgTeampleTwo': assets/'teapmleTwo'/'background'/'ERROR.png',

    'ArtifactNameBgTeampleTwo': assets/'teapmleTwo'/'artifact'/'ARTIFACT_SET_BG.png',
    'ArtifactNameFrameTeampleTwo': assets/'teapmleTwo'/'artifact'/'ARTIFACT_SET_FRAME.png',

    'ArtifactBgTeampleTwo': assets/'teapmleTwo'/'artifact'/'ARTIFACT_BG.png',
    'ArtifactBgUpTeampleTwo': assets/'teapmleTwo'/'artifact'/'ARTIFACT_UP.png',
    'ArtifactDopStatTeampleTwo': assets/'teapmleTwo'/'artifact'/'ARTIFACT_DOP_STAT_FRAME.png',

    'WeaponBgTeampleTwo': assets/'teapmleTwo'/'weapon'/'WEAPON_FRAME.png',

    'NameBgTeampleTwo': assets/'teapmleTwo'/'charterInfo'/'CHARTER_FRAME.png',

    'TalantsFrameTeampleTwo': assets/'teapmleTwo'/'talants'/'TALANTS_FRAME.png',
    'TalantsBGTeampleTwo': assets/'teapmleTwo'/'talants'/'TALANTS_BG.png',
    'TalantsFrameGoldLvlTeampleTwo': assets/'teapmleTwo'/'talants'/'TALANTS_FRAME_GOLD_LVL.png',
    'TalantsCountTeampleTwo': assets/'teapmleTwo'/'talants'/'TALANTS_COUNT.png',

    'AttributeTeampleTwo': assets/'teapmleTwo'/'stats'/'STATS.png',
    'AttributeBgTeampleTwo': assets/'teapmleTwo'/'stats'/'STATS_FRAME.png',

    'infoUserFrameTeampleTwo': assets/'teapmleTwo'/'infoUser'/'INFO_USER_FRAMES.png',
    'infoUserBgTeampleTwo': assets/'teapmleTwo'/'infoUser'/'BG.png',
    'infoUserMaskaTeampleTwo': assets/'teapmleTwo'/'infoUser'/'MASKA_BANNER.png',
    'infoUserMaskaAvatarTeampleTwo': assets/'teapmleTwo'/'infoUser'/'MASKA_AVATAR.png',
    'infoUserFrameBannerTeampleTwo': assets/'teapmleTwo'/'infoUser'/'FRAME.png',

    'UserBgTeampleTwo': assets/'teapmleTwo'/'maska'/'USER_ADAPT.png',
    'UserEffectTeampleTwo': assets/'teapmleTwo'/'maska'/'EFFECT.png',
    'MaskaSplas': assets/'teapmleTwo'/'maska'/'MaskaGrand.png',
    'MasskaEffectDown': assets/'teapmleTwo'/'maska'/'EFFECT_DOWN.png',
}

def __dir__():
    return sorted(set([*globals(), *mapping]))

def __getattr__(name):
    try:
        path = mapping[name]
    except KeyError:
        raise AttributeError(name) from None
    
    with lock:
        try:
            image = cache[name]
        except KeyError:
            cache[name] = image = Image.open(path)
        
        return image
