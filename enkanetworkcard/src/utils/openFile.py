# Copyright 2022 DEViantUa <t.me/deviant_ua>
# All rights reserved.
from PIL import Image
import os

path = os.path.dirname(__file__).replace("utils","assets")
font = f'{path}/font/Genshin_Impact.ttf'

#=================TeampleOne==================
#
#=================Background ==================
AnemoBgTeampleOne = Image.open(f'{path}/teapmleOne/background/ANEMO.png')
CryoBgTeampleOne = Image.open(f'{path}/teapmleOne/background/CRYO.png')
DendroBgTeampleOne = Image.open(f'{path}/teapmleOne/background/DENDRO.png')
ElectroBgTeampleOne = Image.open(f'{path}/teapmleOne/background/ELECTRO.png')
GeoBgTeampleOne = Image.open(f'{path}/teapmleOne/background/GEO.png')
GydroBgTeampleOne = Image.open(f'{path}/teapmleOne/background/GYDRO.png')
PyroBgTeampleOne = Image.open(f'{path}/teapmleOne/background/PYRO.png')
ErrorBgTeampleOne = Image.open(f'{path}/teapmleOne/background/ERROR.png')

#=================ArtifactName==================
ArtifactNameBgTeampleOne = Image.open(f'{path}/teapmleOne/artifact/ARTIFACT_SET_BG.png')
ArtifactNameFrameTeampleOne = Image.open(f'{path}/teapmleOne/artifact/ARTIFACT_SET_FRAME.png')

#=================Artifact==================
ArtifactBgTeampleOne = Image.open(f'{path}/teapmleOne/artifact/ARTIFACT_BG.png')
ArtifactBgUpTeampleOne = Image.open(f'{path}/teapmleOne/artifact/ARTIFACT_UP.png')
ArtifactDopValueTeampleOne = Image.open(f'{path}/teapmleOne/artifact/ARTIFACT_BG_DOP_VAL.png')

#=================Weapon==================
#WeaponBgTeampleOne = Image.open(f'{path}/teapmleOne/weapons/WEAPON_FRAME.png')
WeaponBgTeampleOne = Image.open(f'{path}/teapmleOne/weapons/WEAPON_FRAME_TWO.png')
WeaponBgUpTeampleOne = Image.open(f'{path}/teapmleOne/weapons/WEAPON_FRAME_TWO_UP.png')

#=================Name==================
NameBgTeampleOne = Image.open(f'{path}/teapmleOne/charterInfo/CHARTER_FRAME.png')

#=================Talants==================
TalantsFrameTeampleOne = Image.open(f'{path}/teapmleOne/talants/TALANTS_FRAME.png')
TalantsFrameGoldLvlTeampleOne = Image.open(f'{path}/teapmleOne/talants/TALANTS_FRAME_GOLD_LVL.png').convert('RGBA')
TalantsCountTeampleOne = Image.open(f'{path}/teapmleOne/talants/TALANTS_COUNT.png')

#=================Attribute==================
AttributeTeampleOne = Image.open(f'{path}/teapmleOne/stats/STATS.png')
AttributeBgTeampleOne = Image.open(f'{path}/teapmleOne/stats/STATS_FRAME.png')
AttributeDopValueTeampleOne = Image.open(f'{path}/teapmleOne/stats/STATS_DOP_VALUE.png')

#=================Orher==================
UserBgTeampleOne = Image.open(f'{path}/teapmleOne/maska/ADAPTATION.png')
UserEffectTeampleOne = Image.open(f'{path}/teapmleOne/maska/ADAPTATION5.png').convert('RGBA')
MaskaBgTeampleOne = Image.open(f'{path}/teapmleOne/maska/maska.png').convert('L').resize(ErrorBgTeampleOne.size) 
MaskaUserBgTeampleOne = Image.open(f'{path}/teapmleOne/maska/maskaUserArt.png').convert('L').resize(ErrorBgTeampleOne.size) 
MaskaUserBg2TeampleOne = Image.open(f'{path}/teapmleOne/maska/ADAPTATION2.png').convert('L').resize(ErrorBgTeampleOne.size) 





#=================TeampleTwo==================
#
#=================Background ==================
AnemoBgTeampleTwo = Image.open(f'{path}/teapmleTwo/background/ANEMO.png')
CryoBgTeampleTwo = Image.open(f'{path}/teapmleTwo/background/CRYO.png')
DendroBgTeampleTwo = Image.open(f'{path}/teapmleTwo/background/DENDRO.png')
ElectroBgTeampleTwo = Image.open(f'{path}/teapmleTwo/background/ELECTRO.png')
GeoBgTeampleTwo = Image.open(f'{path}/teapmleTwo/background/GEO.png')
GydroBgTeampleTwo = Image.open(f'{path}/teapmleTwo/background/GYDRO.png')
PyroBgTeampleTwo = Image.open(f'{path}/teapmleTwo/background/PYRO.png')
ErrorBgTeampleTwo = Image.open(f'{path}/teapmleTwo/background/ERROR.png')

#=================ArtifactName==================
ArtifactNameBgTeampleTwo = Image.open(f'{path}/teapmleTwo/artifact/ARTIFACT_SET_BG.png')
ArtifactNameFrameTeampleTwo = Image.open(f'{path}/teapmleTwo/artifact/ARTIFACT_SET_FRAME.png')

#=================Artifact==================
ArtifactBgTeampleTwo = Image.open(f'{path}/teapmleTwo/artifact/ARTIFACT_BG.png')
ArtifactBgUpTeampleTwo = Image.open(f'{path}/teapmleTwo/artifact/ARTIFACT_UP.png')
ArtifactDopStatTeampleTwo = Image.open(f'{path}/teapmleTwo/artifact/ARTIFACT_DOP_STAT_FRAME.png')

#=================Weapon==================
WeaponBgTeampleTwo = Image.open(f'{path}/teapmleTwo/weapon/WEAPON_FRAME.png')

#=================Name==================
NameBgTeampleTwo = Image.open(f'{path}/teapmleTwo/charterInfo/CHARTER_FRAME.png')

#=================Talants==================
TalantsFrameTeampleTwo = Image.open(f'{path}/teapmleTwo/talants/TALANTS_FRAME.png')
TalantsBGTeampleTwo = Image.open(f'{path}/teapmleTwo/talants/TALANTS_BG.png')
TalantsFrameGoldLvlTeampleTwo = Image.open(f'{path}/teapmleOne/talants/TALANTS_FRAME_GOLD_LVL.png').convert('RGBA')
TalantsCountTeampleTwo = Image.open(f'{path}/teapmleTwo/talants/TALANTS_COUNT.png')

#=================Attribute==================
AttributeTeampleTwo = Image.open(f'{path}/teapmleTwo/stats/STATS.png')
AttributeBgTeampleTwo = Image.open(f'{path}/teapmleTwo/stats/STATS_FRAME.png')

#=================User==================
infoUserFrameTeampleTwo = Image.open(f'{path}/teapmleTwo/infoUser/INFO_USER_FRAMES.png')
infoUserBgTeampleTwo = Image.open(f'{path}/teapmleTwo/infoUser/BG.png')
infoUserMaskaTeampleTwo = Image.open(f'{path}/teapmleTwo/infoUser/MASKA_BANNER.png').convert('L')
infoUserMaskaAvatarTeampleTwo = Image.open(f'{path}/teapmleTwo/infoUser/MASKA_AVATAR.png').convert('L')
infoUserFrameBannerTeampleTwo = Image.open(f'{path}/teapmleTwo/infoUser/FRAME.png')

#=================charterElement==================
AnemoCharterElementTeampleTwo = Image.open(f'{path}/teapmleTwo/charter_element/ANEMO.png')
CryoCharterElementTeampleTwo = Image.open(f'{path}/teapmleTwo/charter_element/CRYO.png')
DendroCharterElementTeampleTwo = Image.open(f'{path}/teapmleTwo/charter_element/DENDRO.png')
ElectoCharterElementTeampleTwo = Image.open(f'{path}/teapmleTwo/charter_element/ELECTRO.png')
GeoCharterElementTeampleTwo = Image.open(f'{path}/teapmleTwo/charter_element/GEO.png')
GydroCharterElementTeampleTwo = Image.open(f'{path}/teapmleTwo/charter_element/GYDRO.png')
PyroCharterElementTeampleTwo = Image.open(f'{path}/teapmleTwo/charter_element/PYRO.png')

#=================Orher==================
UserBgTeampleTwo = Image.open(f'{path}/teapmleTwo/maska/USER_ADAPT.png').convert('L').resize(ErrorBgTeampleTwo.size) 
UserEffectTeampleTwo = Image.open(f'{path}/teapmleTwo/maska/EFFECT.png').convert('RGB')
MaskaSplas= Image.open(f'{path}/teapmleTwo/maska/MaskaGrand.png').convert('L').resize(ErrorBgTeampleTwo.size) 
MasskaEffectDown = Image.open(f'{path}/teapmleTwo/maska/EFFECT_DOWN.png')
#MaskaUserBg2TeampleTwo = Image.open(f'{path}/teapmleOne/maska/ADAPTATION2.png').convert('L').resize(ErrorBgTeampleTwo.size) 



#=================ALL==================
#
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
ConstantBG = Image.open(f'{path}/constant/CONSTATN_BG.png')

#=================Star==================
Star1 = Image.open(f'{path}/stars/Star1.png')
Star2 = Image.open(f'{path}/stars/Star2.png')
Star3 = Image.open(f'{path}/stars/Star3.png')
Star4 = Image.open(f'{path}/stars/Star4.png')
Star5 = Image.open(f'{path}/stars/Star5.png')
StarBg = Image.open(f'{path}/stars/bg.png')

#=================Signature==================
SignatureOne = Image.open(f'{path}/SIGNATURE.png').convert('RGBA')
SignatureTwo = Image.open(f'{path}/SIGNATURE3.png').convert('RGBA')

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
