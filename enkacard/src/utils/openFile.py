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




mapping = {
    #===========================TEAMPLE SEVEN===============================
    'ANEMO_SEVEN': assets/'teapmleSeven'/'background'/'ANEMO.png',
    'CRYO_SEVEN': assets/'teapmleSeven'/'background'/'CRYO.png',
    'DENDRO_SEVEN': assets/'teapmleSeven'/'background'/'DENDRO.png',
    'ELECTRO_SEVEN': assets/'teapmleSeven'/'background'/'ELECTRO.png',
    'GEO_SEVEN': assets/'teapmleSeven'/'background'/'GEO.png',
    'GYDRO_SEVEN': assets/'teapmleSeven'/'background'/'GYDRO.png',
    'PYRO_SEVEN': assets/'teapmleSeven'/'background'/'PYRO.png',
    'SHADOW_SEVEN': assets/'teapmleSeven'/'background'/'shadow.png',

    'overlay_SEVEN': assets/'teapmleSeven'/'background'/'overlay.png',
    'FRAME_SEVEN': assets/'teapmleSeven'/'background'/'FRAME.png',
    'MASKA_SPLASH': assets/'teapmleSeven'/'background'/'maska_splash.png',
    'MASKA_ADAPT': assets/'teapmleSeven'/'background'/'maska_adapt.png',
    'Triangle': assets/'teapmleSeven'/'background'/'Triangle.png',
    'max_lvl': assets/'teapmleSeven'/'background'/'max_lvl.png',

    'ART_bg_SEVEN': assets/'teapmleSeven'/'artifact'/'bg.png',
    'ART_frame_SEVEN': assets/'teapmleSeven'/'artifact'/'frame.png',
    'ART_maska_SEVEN': assets/'teapmleSeven'/'artifact'/'maska.png',
    'COUNTS': assets/'teapmleSeven'/'artifact'/'counts.png',

    #===========================TEAMPLE SIX===============================
    'ANEMO_SIX': assets/'teapmleSix'/'background'/'ANEMO.png',
    'CRYO_SIX': assets/'teapmleSix'/'background'/'CRYO.png',
    'DENDRO_SIX': assets/'teapmleSix'/'background'/'DENDRO.png',
    'ELECTRO_SIX': assets/'teapmleSix'/'background'/'ELECTRO.png',
    'GEO_SIX': assets/'teapmleSix'/'background'/'GEO.png',
    'GYDRO_SIX': assets/'teapmleSix'/'background'/'GYDRO.png',
    'PYRO_SIX': assets/'teapmleSix'/'background'/'PYRO.png',
    'ALLSIXBG': assets/'teapmleSix'/'background'/'ALL_BG.png',

    'frame_SIX': assets/'teapmleSix'/'background'/'frame.png',
    'INFO_RAM': assets/'teapmleSix'/'background'/'INFO_RAM.png',
    'MASKA_SIX': assets/'teapmleSix'/'background'/'MASKA.png',
    'SHADOW_SIX': assets/'teapmleSix'/'background'/'SHADOW.png',


    'TALANTS_bg_SIX': assets/'teapmleSix'/'talants'/'bg.png',
    'TALANTS_CoontBig_SIX': assets/'teapmleSix'/'talants'/'CoontBig.png',
    'TALANTS_CoontLow_SIX': assets/'teapmleSix'/'talants'/'CoontLow.png',

    'ART_bg_SIX': assets/'teapmleSix'/'artifact'/'bg.png',
    'ART_maska_SIX': assets/'teapmleSix'/'artifact'/'MASKA.png',
    'TCV': assets/'teapmleSix'/'artifact'/'TCV.png',

    'SIGNATURE4': assets/'SIGNATURE4.png',
    'SIGNATURE4_ARTIST': assets/'SIGNATURE4_ARTIST.png',



    #==========================================================

    'bgProfile': assets/'InfoCharterTwo'/'bg.png',

    'avatar_user': assets/'InfoCharterTwo'/'avatar_user.png',
    'avatar_user_mask': assets/'InfoCharterTwo'/'avatar_user.png',
    'info_user': assets/'InfoCharterTwo'/'info_user.png',
    'ram_avatar': assets/'InfoCharterTwo'/'ram_avatar.png',
    'avatar_user_bg': assets/'InfoCharterTwo'/'avatar_user_bg.png',

    'banner_light': assets/'InfoCharterTwo'/'banner_light.png',
    'banner_mask': assets/'InfoCharterTwo'/'banner_mask.png',


    'charter_bg': assets/'InfoCharterTwo'/'charter_bg.png',
    'charter_icon_4': assets/'InfoCharterTwo'/'charter_icon_4.png',
    'charter_icon_5': assets/'InfoCharterTwo'/'charter_icon_5.png',
    'charter_icon_mask': assets/'InfoCharterTwo'/'charter_icon_mask.png',
    'charter_talants': assets/'InfoCharterTwo'/'charter_talants.png',


    #===========================
    'LK_LOGO_BOT': assets/'teapmleFive'/'Little_Kazuha_Bot_Logo.png',

    'ANEMOTeampleFive': assets/'teapmleFive'/'background'/'ANEMO.png',
    'DENDROTeampleFive': assets/'teapmleFive'/'background'/'DENDRO.png',
    'ELECTROTeampleFive': assets/'teapmleFive'/'background'/'ELECTRO.png',
    'GEOTeampleFive': assets/'teapmleFive'/'background'/'GEO.png',
    'GYDROTeampleFive': assets/'teapmleFive'/'background'/'GYDRO.png',
    'CRYOTeampleFive': assets/'teapmleFive'/'background'/'CRYO.png',
    'PYROTeampleFive': assets/'teapmleFive'/'background'/'PYRO.png',

    'STARS_BG': assets/'teapmleFive'/'background'/'STARS_BG.png',
    'MASKA_ADAPT_HEIGHT_TWO': assets/'teapmleFive'/'background'/'MASKA_ADAPT_HEIGHT_TWO.png',
    'MASKA_ADAPT_HEIGHT': assets/'teapmleFive'/'background'/'MASKA_ADAPT_HEIGHT.png',
    'MASKA_ADAPT_WIDTH': assets/'teapmleFive'/'background'/'MASKA_ADAPT_WIDTH.png',
    'MASKA_ADAPT_SPLASH': assets/'teapmleFive'/'background'/'MASKA_ADAPT_SPLASH.png',
    'SHADOW_TEAMPLEfive': assets/'teapmleFive'/'background'/'SHADOW.png',
    
    'ArtifactBGFive': assets/'teapmleFive'/'artifact'/'bg.png',
    'ArtifactLVLFive': assets/'teapmleFive'/'artifact'/'LVL.png',
    'ArtifactmaskaFive': assets/'teapmleFive'/'artifact'/'maska.png',
    'ArtifactSETFive': assets/'teapmleFive'/'artifact'/'SET.png',
    'artifactMaskaFive': assets/'teapmleFive'/'artifact'/'artifactMaska.png',
     
    
    'ANEMOTeampleFiveElement': assets/'teapmleFive'/'element'/'ANEMO.png',
    'DENDROTeampleFiveElement': assets/'teapmleFive'/'element'/'DENDRO.png',
    'ELECTROTeampleFiveElement': assets/'teapmleFive'/'element'/'ELECTRO.png',
    'GEOTeampleFiveElement': assets/'teapmleFive'/'element'/'GEO.png',
    'GYDROTeampleFiveElement': assets/'teapmleFive'/'element'/'GYDRO.png',
    'CRYOTeampleFiveElement': assets/'teapmleFive'/'element'/'CRYO.png',
    'PYROTeampleFiveElement': assets/'teapmleFive'/'element'/'PYRO.png',

    'WeaponTeampleFive': assets/'teapmleFive'/'weapon'/'bg.png',


    'BIG_LVLTeampleFive': assets/'teapmleFive'/'talants'/'BIG_LVL.png',
    'LOW_LVLTeampleFive': assets/'teapmleFive'/'talants'/'LOW_LVL.png',

    'BGStatsTeampleFive': assets/'teapmleFive'/'stats'/'BG.png',
    'NAME_BANNERTeampleFive': assets/'teapmleFive'/'stats'/'NAME_BANNER.png',

    'stars_frame1': assets/'teapmleFive'/'stars'/'1_stars_frame.png',
    'stars_frame2': assets/'teapmleFive'/'stars'/'2_stars_frame.png',
    'stars_frame3': assets/'teapmleFive'/'stars'/'3_stars_frame.png',
    'stars_frame4': assets/'teapmleFive'/'stars'/'4_stars_frame.png',
    'stars_frame5': assets/'teapmleFive'/'stars'/'5_stars_frame.png',

    'stars_light1': assets/'teapmleFive'/'stars'/'1_stars_light.png',
    'stars_light2': assets/'teapmleFive'/'stars'/'2_stars_light.png',
    'stars_light3': assets/'teapmleFive'/'stars'/'3_stars_light.png',
    'stars_light4': assets/'teapmleFive'/'stars'/'4_stars_light.png',
    'stars_light5': assets/'teapmleFive'/'stars'/'5_stars_light.png',


    #===========================
    'PlayerGirl': assets/'PlayerGirl.png',

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
    'USER_BG_IMG_VERT': assets/'teapmleTree'/'maska'/'USER_BG_IMG_VERT.png',
    'EffectBgTree': assets/'teapmleTree'/'maska'/'EFFECT.png',
    'ClosedConstTree': assets/'teapmleTree'/'constant'/'closed'/'CLOSED.png',
    #===========================
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
    'Signature': assets /'SIGNATURE2.png',


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
    'MaskaArt_TWO': assets/'teapmleTwo'/'maska'/'MaskaArt_TWO.png',
    'MaskaArt_TWO_TREE': assets/'teapmleTwo'/'maska'/'MaskaArt_TWO_TREE.png',
    'UserEffectTeampleTwo': assets/'teapmleTwo'/'maska'/'EFFECT.png',
    'MaskaSplas': assets/'teapmleTwo'/'maska'/'MaskaGrand.png',
    'MasskaEffectDown': assets/'teapmleTwo'/'maska'/'EFFECT_DOWN.png',

    #===========================TEAMPLE FOUR===============================
    'BG_CARD_MINI': assets/'TEAMPLE4'/'bg'/'BG_CARD_MINI.png',
    'BG_CARD_MAX': assets/'TEAMPLE4'/'bg'/'BG_CARD_MAX.png',
    #MAX
    'BG_MAX_TEAMPLE': assets/'TEAMPLE4'/'bg'/'BG_MAX.png',
    'BG_MAX_ALL': assets/'TEAMPLE4'/'bg'/'BG_MAX_ALL.png',

    'ANEMO_ART': assets/'TEAMPLE4'/'artifact'/'ANEMO.png',
    'CRYO_ART': assets/'TEAMPLE4'/'artifact'/'CRYO.png',
    'DENDRO_ART': assets/'TEAMPLE4'/'artifact'/'DENDRO.png',
    'ELECTRO_ART': assets/'TEAMPLE4'/'artifact'/'ELECTRO.png',
    'GEO_ART': assets/'TEAMPLE4'/'artifact'/'GEO.png',
    'GYDRO_ART': assets/'TEAMPLE4'/'artifact'/'GYDRO.png',
    'PYRO_ART': assets/'TEAMPLE4'/'artifact'/'PYRO.png',
    'FRAME_ART': assets/'TEAMPLE4'/'artifact'/'frame.png',

    'ANEMO_STAT': assets/'TEAMPLE4'/'stats'/'ANEMO.png',
    'CRYO_STAT': assets/'TEAMPLE4'/'stats'/'CRYO.png',
    'DENDRO_STAT': assets/'TEAMPLE4'/'stats'/'DENDRO.png',
    'ELECTRO_STAT': assets/'TEAMPLE4'/'stats'/'ELECTRO.png',
    'GEO_STAT': assets/'TEAMPLE4'/'stats'/'GEO.png',
    'GYDRO_STAT': assets/'TEAMPLE4'/'stats'/'GYDRO.png',
    'PYRO_STAT': assets/'TEAMPLE4'/'stats'/'PYRO.png',

    #MINI
    'ANEMO_BG': assets/'TEAMPLE4'/'bg'/'ANEMO.png',
    'CRYO_BG': assets/'TEAMPLE4'/'bg'/'CRYO.png',
    'DENDRO_BG': assets/'TEAMPLE4'/'bg'/'DENDRO.png',
    'ELECTRO_BG': assets/'TEAMPLE4'/'bg'/'ELECTRO.png',
    'GEO_BG': assets/'TEAMPLE4'/'bg'/'GEO.png',
    'GYDRO_BG': assets/'TEAMPLE4'/'bg'/'GYDRO.png',
    'PYRO_BG': assets/'TEAMPLE4'/'bg'/'PYRO.png',
    'ALL_BG': assets/'TEAMPLE4'/'bg'/'BG.png',
    'MASKA_BG': assets/'TEAMPLE4'/'bg'/'maska.png',
    'GRANDIENT_BG': assets/'TEAMPLE4'/'bg'/'GRANDIENT.png',
    "SHADOW_USER_BG": assets/'TEAMPLE4'/'bg'/'SHADOW_USER_BG.png',
    
    'ANEMO_FRAME': assets/'TEAMPLE4'/'bgFrame'/'ANEMO.png',
    'CRYO_FRAME': assets/'TEAMPLE4'/'bgFrame'/'CRYO.png',
    'DENDRO_FRAME': assets/'TEAMPLE4'/'bgFrame'/'DENDRO.png',
    'ELECTRO_FRAME': assets/'TEAMPLE4'/'bgFrame'/'ELECTRO.png',
    'GEO_FRAME': assets/'TEAMPLE4'/'bgFrame'/'GEO.png',
    'GYDRO_FRAME': assets/'TEAMPLE4'/'bgFrame'/'GYDRO.png',
    'PYRO_FRAME': assets/'TEAMPLE4'/'bgFrame'/'PYRO.png',

    'ANEMO_WEAPON': assets/'TEAMPLE4'/'weaponFrame'/'ANEMO.png',
    'CRYO_WEAPON': assets/'TEAMPLE4'/'weaponFrame'/'CRYO.png',
    'DENDRO_WEAPON': assets/'TEAMPLE4'/'weaponFrame'/'DENDRO.png',
    'ELECTRO_WEAPON': assets/'TEAMPLE4'/'weaponFrame'/'ELECTRO.png',
    'GEO_WEAPON': assets/'TEAMPLE4'/'weaponFrame'/'GEO.png',
    'GYDRO_WEAPON': assets/'TEAMPLE4'/'weaponFrame'/'GYDRO.png',
    'PYRO_WEAPON': assets/'TEAMPLE4'/'weaponFrame'/'PYRO.png',
    
    'WEAPON_BG': assets/'TEAMPLE4'/'weapon'/'bg.png',
    "WEAPON_GRANDIENT": assets/'TEAMPLE4'/'weapon'/'grandient.png',
    'WEAPON_FRAME': assets/'TEAMPLE4'/'weapon'/'frame.png',
    'MASKA_WEAPON': assets/'TEAMPLE4'/'weapon'/'maska2.png',

    'C_STAR_4': assets/'stars'/'c_stars_4.png',
    'C_STAR_5': assets/'stars'/'c_stars_5.png',
    

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
