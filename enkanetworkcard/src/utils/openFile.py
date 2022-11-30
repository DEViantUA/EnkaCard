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
AnemoBgTeampleOne.load()
CryoBgTeampleOne = Image.open(f'{path}/teapmleOne/background/CRYO.png')
CryoBgTeampleOne.load()
DendroBgTeampleOne = Image.open(f'{path}/teapmleOne/background/DENDRO.png')
DendroBgTeampleOne.load()
ElectroBgTeampleOne = Image.open(f'{path}/teapmleOne/background/ELECTRO.png')
ElectroBgTeampleOne.load()
GeoBgTeampleOne = Image.open(f'{path}/teapmleOne/background/GEO.png')
GeoBgTeampleOne.load()
GydroBgTeampleOne = Image.open(f'{path}/teapmleOne/background/GYDRO.png')
GydroBgTeampleOne.load()
PyroBgTeampleOne = Image.open(f'{path}/teapmleOne/background/PYRO.png')
PyroBgTeampleOne.load()
ErrorBgTeampleOne = Image.open(f'{path}/teapmleOne/background/ERROR.png')
ErrorBgTeampleOne.load()
#=================ArtifactName==================
ArtifactNameBgTeampleOne = Image.open(f'{path}/teapmleOne/artifact/ARTIFACT_SET_BG.png')
ArtifactNameBgTeampleOne.load()
ArtifactNameFrameTeampleOne = Image.open(f'{path}/teapmleOne/artifact/ARTIFACT_SET_FRAME.png')
ArtifactNameFrameTeampleOne.load()
#=================Artifact==================
ArtifactBgTeampleOne = Image.open(f'{path}/teapmleOne/artifact/ARTIFACT_BG.png')
ArtifactBgTeampleOne.load()
ArtifactBgUpTeampleOne = Image.open(f'{path}/teapmleOne/artifact/ARTIFACT_UP.png')
ArtifactBgUpTeampleOne.load()
ArtifactDopValueTeampleOne = Image.open(f'{path}/teapmleOne/artifact/ARTIFACT_BG_DOP_VAL.png')
ArtifactDopValueTeampleOne.load()
#=================Weapon==================
#WeaponBgTeampleOne = Image.open(f'{path}/teapmleOne/weapons/WEAPON_FRAME.png')
WeaponBgTeampleOne = Image.open(f'{path}/teapmleOne/weapons/WEAPON_FRAME_TWO.png')
WeaponBgTeampleOne.load()
WeaponBgUpTeampleOne = Image.open(f'{path}/teapmleOne/weapons/WEAPON_FRAME_TWO_UP.png')
WeaponBgUpTeampleOne.load()
#=================Name==================
NameBgTeampleOne = Image.open(f'{path}/teapmleOne/charterInfo/CHARTER_FRAME.png')
NameBgTeampleOne.load()
#=================Talants==================
TalantsFrameTeampleOne = Image.open(f'{path}/teapmleOne/talants/TALANTS_FRAME.png')
TalantsFrameTeampleOne.load()
TalantsFrameGoldLvlTeampleOne = Image.open(f'{path}/teapmleOne/talants/TALANTS_FRAME_GOLD_LVL.png').convert('RGBA')
TalantsFrameGoldLvlTeampleOne.load()
TalantsCountTeampleOne = Image.open(f'{path}/teapmleOne/talants/TALANTS_COUNT.png')
TalantsCountTeampleOne.load()

#=================Attribute==================
AttributeTeampleOne = Image.open(f'{path}/teapmleOne/stats/STATS.png')
AttributeTeampleOne.load()
AttributeBgTeampleOne = Image.open(f'{path}/teapmleOne/stats/STATS_FRAME.png')
AttributeBgTeampleOne.load()
AttributeDopValueTeampleOne = Image.open(f'{path}/teapmleOne/stats/STATS_DOP_VALUE.png')
AttributeDopValueTeampleOne.load()
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
AnemoBgTeampleTwo.load()
CryoBgTeampleTwo = Image.open(f'{path}/teapmleTwo/background/CRYO.png')
CryoBgTeampleTwo.load()
DendroBgTeampleTwo = Image.open(f'{path}/teapmleTwo/background/DENDRO.png')
DendroBgTeampleTwo.load()
ElectroBgTeampleTwo = Image.open(f'{path}/teapmleTwo/background/ELECTRO.png')
ElectroBgTeampleTwo.load()
GeoBgTeampleTwo = Image.open(f'{path}/teapmleTwo/background/GEO.png')
GeoBgTeampleTwo.load()
GydroBgTeampleTwo = Image.open(f'{path}/teapmleTwo/background/GYDRO.png')
GydroBgTeampleTwo.load()
PyroBgTeampleTwo = Image.open(f'{path}/teapmleTwo/background/PYRO.png')
PyroBgTeampleTwo.load()
ErrorBgTeampleTwo = Image.open(f'{path}/teapmleTwo/background/ERROR.png')
ErrorBgTeampleTwo.load()

#=================ArtifactName==================
ArtifactNameBgTeampleTwo = Image.open(f'{path}/teapmleTwo/artifact/ARTIFACT_SET_BG.png')
ArtifactNameBgTeampleTwo.load()
ArtifactNameFrameTeampleTwo = Image.open(f'{path}/teapmleTwo/artifact/ARTIFACT_SET_FRAME.png')
ArtifactNameFrameTeampleTwo.load()

#=================Artifact==================
ArtifactBgTeampleTwo = Image.open(f'{path}/teapmleTwo/artifact/ARTIFACT_BG.png')
ArtifactBgTeampleTwo.load()
ArtifactBgUpTeampleTwo = Image.open(f'{path}/teapmleTwo/artifact/ARTIFACT_UP.png')
ArtifactBgUpTeampleTwo.load()
ArtifactDopStatTeampleTwo = Image.open(f'{path}/teapmleTwo/artifact/ARTIFACT_DOP_STAT_FRAME.png')
ArtifactDopStatTeampleTwo.load()

#=================Weapon==================
WeaponBgTeampleTwo = Image.open(f'{path}/teapmleTwo/weapon/WEAPON_FRAME.png')
WeaponBgTeampleTwo.load()
#=================Name==================
NameBgTeampleTwo = Image.open(f'{path}/teapmleTwo/charterInfo/CHARTER_FRAME.png')
NameBgTeampleTwo.load()
#=================Talants==================
TalantsFrameTeampleTwo = Image.open(f'{path}/teapmleTwo/talants/TALANTS_FRAME.png')
TalantsFrameTeampleTwo.load()
TalantsBGTeampleTwo = Image.open(f'{path}/teapmleTwo/talants/TALANTS_BG.png')
TalantsBGTeampleTwo.load()
TalantsFrameGoldLvlTeampleTwo = Image.open(f'{path}/teapmleOne/talants/TALANTS_FRAME_GOLD_LVL.png').convert('RGBA')
TalantsFrameGoldLvlTeampleTwo.load()
TalantsCountTeampleTwo = Image.open(f'{path}/teapmleTwo/talants/TALANTS_COUNT.png')
TalantsCountTeampleTwo.load()
#=================Attribute==================
AttributeTeampleTwo = Image.open(f'{path}/teapmleTwo/stats/STATS.png')
AttributeTeampleTwo.load()
AttributeBgTeampleTwo = Image.open(f'{path}/teapmleTwo/stats/STATS_FRAME.png')
AttributeBgTeampleTwo.load()

#=================User==================
infoUserFrameTeampleTwo = Image.open(f'{path}/teapmleTwo/infoUser/INFO_USER_FRAMES.png')
infoUserFrameTeampleTwo.load()
infoUserBgTeampleTwo = Image.open(f'{path}/teapmleTwo/infoUser/BG.png')
infoUserBgTeampleTwo.load()
infoUserMaskaTeampleTwo = Image.open(f'{path}/teapmleTwo/infoUser/MASKA_BANNER.png').convert('L')
infoUserMaskaTeampleTwo.load()
infoUserMaskaAvatarTeampleTwo = Image.open(f'{path}/teapmleTwo/infoUser/MASKA_AVATAR.png').convert('L')
infoUserMaskaAvatarTeampleTwo.load()
infoUserFrameBannerTeampleTwo = Image.open(f'{path}/teapmleTwo/infoUser/FRAME.png')
infoUserFrameBannerTeampleTwo.load()

#=================charterElement==================
AnemoCharterElementTeampleTwo = Image.open(f'{path}/teapmleTwo/charter_element/ANEMO.png')
AnemoCharterElementTeampleTwo.load()
CryoCharterElementTeampleTwo = Image.open(f'{path}/teapmleTwo/charter_element/CRYO.png')
CryoCharterElementTeampleTwo.load()
DendroCharterElementTeampleTwo = Image.open(f'{path}/teapmleTwo/charter_element/DENDRO.png')
DendroCharterElementTeampleTwo.load()
ElectoCharterElementTeampleTwo = Image.open(f'{path}/teapmleTwo/charter_element/ELECTRO.png')
ElectoCharterElementTeampleTwo.load()
GeoCharterElementTeampleTwo = Image.open(f'{path}/teapmleTwo/charter_element/GEO.png')
GeoCharterElementTeampleTwo.load()
GydroCharterElementTeampleTwo = Image.open(f'{path}/teapmleTwo/charter_element/GYDRO.png')
GydroCharterElementTeampleTwo.load()
PyroCharterElementTeampleTwo = Image.open(f'{path}/teapmleTwo/charter_element/PYRO.png')
PyroCharterElementTeampleTwo.load()
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
AnemoConstant.load()
CryoConstant= Image.open(f'{path}/constant/CRYO.png')
CryoConstant.load()
DendroConstant = Image.open(f'{path}/constant/DENDRO.png')
DendroConstant.load()
ElectroConstant = Image.open(f'{path}/constant/ELECTRO.png')
ElectroConstant.load()
GeoConstant = Image.open(f'{path}/constant/GEO.png')
GeoConstant.load()
GydroConstant = Image.open(f'{path}/constant/GYDRO.png')
GydroConstant.load()
PyroConstant= Image.open(f'{path}/constant/PYRO.png')
PyroConstant.load()
ErrorConstant = Image.open(f'{path}/constant/ERROR.png')
ErrorConstant.load()
ClossedBg = Image.open(f'{path}/constant/CLOSED_BG.png')
ClossedBg.load()
Clossed = Image.open(f'{path}/constant/CLOSED.png')
Clossed.load()
ConstantBG = Image.open(f'{path}/constant/CONSTATN_BG.png')
ConstantBG.load()

#=================Star==================
Star1 = Image.open(f'{path}/stars/Star1.png')
Star1.load()
Star2 = Image.open(f'{path}/stars/Star2.png')
Star2.load()
Star3 = Image.open(f'{path}/stars/Star3.png')
Star3.load()
Star4 = Image.open(f'{path}/stars/Star4.png')
Star4.load()
Star5 = Image.open(f'{path}/stars/Star5.png')
Star5.load()
StarBg = Image.open(f'{path}/stars/bg.png')
StarBg.load()

#=================Signature==================
SignatureOne = Image.open(f'{path}/SIGNATURE.png').convert('RGBA')
SignatureTwo = Image.open(f'{path}/SIGNATURE3.png').convert('RGBA')

#=================ICON==================
FIGHT_PROP_MAX_HP = Image.open(f'{path}/icon/HP.png') 
FIGHT_PROP_MAX_HP.load()
FIGHT_PROP_HP_PERCENT = Image.open(f'{path}/icon/HP_PERCENT.png')
FIGHT_PROP_HP_PERCENT.load()
FIGHT_PROP_CUR_ATTACK = Image.open(f'{path}/icon/ATTACK.png')
FIGHT_PROP_CUR_ATTACK.load()
FIGHT_PROP_ATTACK_PERCENT = Image.open(f'{path}/icon/ATTACK_PERCENT.png')
FIGHT_PROP_ATTACK_PERCENT.load()
FIGHT_PROP_PHYSICAL_ADD_HURT = Image.open(f'{path}/icon/PHYSICAL_ADD_HURT.png')
FIGHT_PROP_PHYSICAL_ADD_HURT.load()
FIGHT_PROP_CRITICAL = Image.open(f'{path}/icon/CRITICAL_HURT.png')
FIGHT_PROP_CRITICAL.load()
FIGHT_PROP_CRITICAL_HURT = Image.open(f'{path}/icon/CRITICAL.png')
FIGHT_PROP_CRITICAL_HURT.load()
FIGHT_PROP_CUR_DEFENSE = Image.open(f'{path}/icon/DEFENSE.png')
FIGHT_PROP_CUR_DEFENSE.load()
FIGHT_PROP_DEFENSE_PERCENT = Image.open(f'{path}/icon/DEFENSE_PERCENT.png')
FIGHT_PROP_DEFENSE_PERCENT.load()
FIGHT_PROP_SHIELD_COST_MINUS_RATIO = Image.open(f'{path}/icon/SHIELD_COST_MINUS_RATIO.png')
FIGHT_PROP_SHIELD_COST_MINUS_RATIO.load()
FIGHT_PROP_HEAL_ADD = Image.open(f'{path}/icon/HEALED_ADD.png')
FIGHT_PROP_HEAL_ADD.load()
FIGHT_PROP_HEAL = Image.open(f'{path}/icon/HEAL.png')
FIGHT_PROP_HEAL.load()
FIGHT_PROP_ELEMENT_MASTERY = Image.open(f'{path}/icon/MASTERY.png')
FIGHT_PROP_ELEMENT_MASTERY.load()
FIGHT_PROP_CHARGE_EFFICIENCY = Image.open(f'{path}/icon/CHARGE_EFFICIENCY.png')
FIGHT_PROP_CHARGE_EFFICIENCY.load()
FIGHT_PROP_ELEC_ADD_HURT = Image.open(f'{path}/icon/ELECTRO.png')
FIGHT_PROP_ELEC_ADD_HURT.load()
FIGHT_PROP_WATER_ADD_HURT = Image.open(f'{path}/icon/HYDRO.png')
FIGHT_PROP_WATER_ADD_HURT.load()
FIGHT_PROP_WIND_ADD_HURT = Image.open(f'{path}/icon/ANEMO.png')
FIGHT_PROP_WIND_ADD_HURT.load()
FIGHT_PROP_ICE_ADD_HURT = Image.open(f'{path}/icon/CRYO.png')
FIGHT_PROP_ICE_ADD_HURT.load()
FIGHT_PROP_ROCK_ADD_HURT = Image.open(f'{path}/icon/GEO.png')
FIGHT_PROP_ROCK_ADD_HURT.load()
FIGHT_PROP_FIRE_ADD_HURT = Image.open(f'{path}/icon/PYRO.png')
FIGHT_PROP_FIRE_ADD_HURT.load()
FIGHT_PROP_GRASS_ADD_HURT = Image.open(f'{path}/icon/DENDRO.png')
FIGHT_PROP_GRASS_ADD_HURT.load()