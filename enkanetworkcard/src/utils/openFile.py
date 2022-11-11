# Copyright 2022 DEViantUa <t.me/deviant_ua>
# All rights reserved.
from PIL import Image
import os

path = os.path.dirname(__file__).replace("utils","assets")

#=================Background==================
font = f'{path}/font/Genshin_Impact.ttf'

#=================Background==================
AnemoBg = Image.open(f'{path}/background/ANEMO.png')
CryoBg = Image.open(f'{path}/background/CRYO.png')
DendroBg = Image.open(f'{path}/background/DENDRO.png')
ElectroBg = Image.open(f'{path}/background/ELECTRO.png')
GeoBg = Image.open(f'{path}/background/GEO.png')
GydroBg = Image.open(f'{path}/background/GYDRO.png')
PyroBg = Image.open(f'{path}/background/PYRO.png')
ErrorBg = Image.open(f'{path}/background/ERROR.png')

#=================Constant==================
AnemoConstant = Image.open(f'{path}/constant/ANEMO.png')
CryoConstant= Image.open(f'{path}/constant/CRYO.png')
DendroConstant = Image.open(f'{path}/constant/DENDRO.png')
ElectroConstant = Image.open(f'{path}/constant/ELECTRO.png')
GeoConstant = Image.open(f'{path}/constant/GEO.png')
GydroConstant = Image.open(f'{path}/constant/GYDRO.png')
PyroConstant= Image.open(f'{path}/constant/PYRO.png')
ErrorConstant = Image.open(f'{path}/constant/ERROR.png')
ClossedBg = Image.open(f'{path}/constant/CLOSED_BG.png')
Clossed = Image.open(f'{path}/constant/CLOSED.png')

#=================Star==================
Star1 = Image.open(f'{path}/stars/Star1.png')
Star2 = Image.open(f'{path}/stars/Star2.png')
Star3 = Image.open(f'{path}/stars/Star3.png')
Star4 = Image.open(f'{path}/stars/Star4.png')
Star5 = Image.open(f'{path}/stars/Star5.png')

#=================ArtifactName==================
ArtifactNameBg = Image.open(f'{path}/artifact/ARTIFACT_SET_BG.png')
ArtifactNameFrame = Image.open(f'{path}/artifact/ARTIFACT_SET_FRAME.png')

#=================Artifact==================
ArtifactBg = Image.open(f'{path}/artifact/ARTIFACT_BG.png')
ArtifactBgUp = Image.open(f'{path}/artifact/ARTIFACT_UP.png')

#=================Weapon==================
WeaponBg = Image.open(f'{path}/weapons/WEAPON_FRAME.png')

#=================Signature==================
Signature = Image.open(f'{path}/SIGNATURE.png').convert('RGBA')

#=================Name==================
NameBg = Image.open(f'{path}/charterInfo/CHARTER_FRAME.png')

#=================Talants==================
TalantsFrame = Image.open(f'{path}/talants/TALANTS_FRAME.png')
TalantsFrameGoldLvl = Image.open(f'{path}/talants/TALANTS_FRAME_GOLD_LVL.png').convert('RGBA')
TalantsCount = Image.open(f'{path}/talants/TALANTS_COUNT.png')

#=================Attribute==================
Attribute = Image.open(f'{path}/stats/STATS.png')
AttributeBg = Image.open(f'{path}/stats/STATS_FRAME.png')

#=================Orher==================
UserBg = Image.open(f'{path}/maska/ADAPTATION.png')
UserEffect = Image.open(f'{path}/maska/ADAPTATION5.png').convert('RGBA')
MaskaBg = Image.open(f'{path}/maska/maska.png').convert('L').resize(ErrorBg.size) 
MaskaUserBg = Image.open(f'{path}/maska/maskaUserArt.png').convert('L').resize(ErrorBg.size) 
MaskaUserBg2 = Image.open(f'{path}/maska/ADAPTATION2.png').convert('L').resize(ErrorBg.size) 

#=================ICON==================
FIGHT_PROP_MAX_HP = Image.open(f'{path}/icon/HP.png') 
FIGHT_PROP_HP_PERCENT = Image.open(f'{path}/icon/HP_PERCENT.png')
FIGHT_PROP_CUR_ATTACK = Image.open(f'{path}/icon/ATTACK.png')
FIGHT_PROP_ATTACK_PERCENT = Image.open(f'{path}/icon/ATTACK_PERCENT.png')
FIGHT_PROP_PHYSICAL_ADD_HURT = Image.open(f'{path}/icon/PHYSICAL_ADD_HURT.png')
FIGHT_PROP_CRITICAL = Image.open(f'{path}/icon/CRITICAL_HURT.png')
FIGHT_PROP_CRITICAL_HURT = Image.open(f'{path}/icon/CRITICAL.png')
FIGHT_PROP_CUR_DEFENSE = Image.open(f'{path}/icon/DEFENSE.png')
FIGHT_PROP_DEFENSE_PERCENT = Image.open(f'{path}/icon/DEFENSE_PERCENT.png')
FIGHT_PROP_SHIELD_COST_MINUS_RATIO = Image.open(f'{path}/icon/SHIELD_COST_MINUS_RATIO.png')
FIGHT_PROP_HEAL_ADD = Image.open(f'{path}/icon/HEALED_ADD.png')
FIGHT_PROP_HEAL = Image.open(f'{path}/icon/HEAL.png')
FIGHT_PROP_ELEMENT_MASTERY = Image.open(f'{path}/icon/MASTERY.png')
FIGHT_PROP_CHARGE_EFFICIENCY = Image.open(f'{path}/icon/CHARGE_EFFICIENCY.png')
FIGHT_PROP_ELEC_ADD_HURT = Image.open(f'{path}/icon/ELECTRO.png')
FIGHT_PROP_WATER_ADD_HURT = Image.open(f'{path}/icon/HYDRO.png')
FIGHT_PROP_WIND_ADD_HURT = Image.open(f'{path}/icon/ANEMO.png')
FIGHT_PROP_ICE_ADD_HURT = Image.open(f'{path}/icon/CRYO.png')
FIGHT_PROP_ROCK_ADD_HURT = Image.open(f'{path}/icon/GEO.png')
FIGHT_PROP_FIRE_ADD_HURT = Image.open(f'{path}/icon/PYRO.png')
FIGHT_PROP_GRASS_ADD_HURT = Image.open(f'{path}/icon/DENDRO.png')
