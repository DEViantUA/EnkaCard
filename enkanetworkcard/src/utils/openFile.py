
from PIL import Image
from PIL import UnidentifiedImageError
import threading
from weakref import WeakValueDictionary
from pathlib import Path
import httpx
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

    #===========================TEAMPLE FOUR===============================
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

def dowload(path,ret = False):
    with open(path, 'wb') as file:
        with httpx.stream('GET', f"https://raw.githubusercontent.com/DEViantUA/EnkaNetworkCardAsset/main/data/2.0.8/assets/{path.relative_to(assets).as_posix()}") as response:
            response.raise_for_status()
            
            for data in response.iter_bytes():
                file.write(data)
    if ret:
        return Image.open(path)
    else:
        return None
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
            if not path.is_file():
                path.parent.mkdir(parents=True, exist_ok=True)
                dowload(path)
            try: 
                cache[name] = image = Image.open(path)
            except UnidentifiedImageError:
                cache[name] = image = dowload(path)
        
        return image