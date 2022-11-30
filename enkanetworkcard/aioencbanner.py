# Copyright 2022 DEViantUa <t.me/deviant_ua>
# All rights reserved.
from enkanetwork import EnkaNetworkAPI,Assets
import logging,asyncio,random, os, datetime
from threading import Thread
from .src.utils.CreatBannerTwo import generationTwo, creatUserInfo
from .src.utils.CreatBannerOne import generationOne, signature, openUserImg 
from .src.utils.userProfile import creatUserProfile
from .src.utils.translation import translationLang,supportLang
from .enc_error import ENCardError

    
logging.getLogger('enkanetwork.assets').setLevel(logging.CRITICAL)

async def upload():
    client = EnkaNetworkAPI()
    async with client:
        await client.update_assets()


async def info(uid = None,lang = None):
    async with EnkaNetworkAPI(lang=lang) as client:
        r = await client.fetch_user(uid)
        if not r.characters:
            return None
    return r

def uidCreat(uids):
    if type(uids) == int or type(uids) == str:
        return str(uids).replace(' ', '').split(",")
    else:
        raise ENCardError(5,"The UIDS parameter must be a number or a string. To pass multiple UIDs, separate them with commas.\nExample: uids = 55363 or uids = '55363,58999,567862,...'")

def saveBanner(uid,res,name):
    data = datetime.datetime.now().strftime("%d_%m_%Y %H_%M")
    path = os.getcwd()
    try:
        os.mkdir(f'{path}/EnkaImg')
    except:
        pass
    try:
        os.mkdir(f'{path}/EnkaImg/{uid}')
    except:
        pass
    res.save(f"{path}/EnkaImg/{uid}/{name}_{data}.png")




def generation(charter,assets,img,adapt,uid,RESULT, save,signatureRes,translateLang,splash,teample = 1):
    if teample == 1:
        result = generationOne(charter,assets,img,adapt,signatureRes,translateLang["lvl"],splash)
    else:
        result = generationTwo(charter,assets,img,adapt,signatureRes,translateLang,splash)
    if not save:
        saveBanner(uid,result,charter.name)
    else:
        if not uid in RESULT:
            RESULT[uid] = {}
        if not charter.name in RESULT[uid]:
            RESULT[uid][charter.name] = result
    return None

class EnkaGenshinGeneration:

    FIX_ASYNCIO_WIN = False

    def __init__(self,lang = "ru",charterImg = None,
            img = None, name = None, adapt = False,
            randomImg = False, hide = False, dowload = False, namecard = False, splash = False):
        if not lang in supportLang:
            raise ENCardError(6,"Dislike language List of available languages: en, ru, vi, th, pt, kr, jp, zh, id, fr, es, de, chs, cht.\nRead more in the documentation: https://github.com/DEViantUA/EnkaNetworkCard")
        self.assets = Assets(lang=lang)
        self.lang = lang
        self.splash = splash
        self.namecard = namecard
        self.translateLang = translationLang[self.lang]
        self.adapt = adapt
        self.dowload = dowload
        self.hide = hide
        self.name = name
        self.img = img
        self.randomImg = randomImg
        self.charterImg = charterImg
        if charterImg:
            if type(charterImg) == dict:
                chImg = {}
                for key in charterImg:
                    if not key in chImg:
                        chImg[key.lower()] = charterImg[key]
                self.charterImg = chImg
            else:
                 raise ENCardError(4,"The charterImg parameter must be a dictionary, where the key is the name of the character, and the parameter is an image.\nExample: charterImg = {'Klee': 'img.png'} or {'Klee': 'img.png', 'Xiao': 'img2.jpg', ...}")
        if name:
            if type(name) == str:
                self.name = name.lower().replace(' ', '').split(",")
            else:
                raise ENCardError(3,"The name parameter must be a string, to pass multiple names, list them separated by commas.\nExample: name = 'Klee' or name = 'Klee, Xiao'")
                
        if type(img) == list:
            if self.randomImg:
                if len(img) > 1:
                    self.img = img
                else:
                   raise ENCardError(2, "The list of images must consist of 2 or more.\nExample: img = ['1.png','2.png', ...]") 
            else:
                raise ENCardError(1, "For a list of images, you need to pass the randomImg parameter\nExample: randomImg = True")
        else:
            self.randomImg = False
            if img:
                self.img = openUserImg(img)
    

    async def profile(self,uid, image = True):
        if type(uid) == int:
            if int(uid) > 0:
                profile = await info(uid,self.lang)
            else:
                raise ENCardError(7, "The UID argument must be a number and greater than 0")
        else:
            raise ENCardError(7, "The UID argument must be a number and greater than 0")
        itog = creatUserProfile(image,profile.player,self.translateLang,self.hide,uid,self.assets)

        return itog
    async def start(self,uids, template = 1, name = None):
        if self.FIX_ASYNCIO_WIN:
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        startPotoki = {}
        ResultEnka = {}
        if name:
            self.name = name
        if template < 1 or template > 2:
            raise ENCardError(1, "The teamle parameter supports values ​​from 1 to 2")
        uids = uidCreat(uids)
        for uid in uids:
            r = await info(uid,self.lang)
            if not r:
                continue
            if template == 1:
                signatureRes = signature(self.hide,uid)
            else:
                signatureRes = creatUserInfo(self.hide,uid,r.player,self.translateLang)
            for key in r.characters:
                if self.namecard and template == 2:
                    signatureRes = creatUserInfo(self.hide,uid,r.player,self.translateLang,key.image.icon.filename.replace("CostumeFloral","").split("AvatarIcon_")[1],self.namecard)
                if self.name:
                    if not key.name.lower() in self.name:
                        continue
                self.characterImg(key.name.lower())
                self.startNameGeneration(key,uid,startPotoki,ResultEnka,signatureRes,template)
        return self.dowloadImg(startPotoki,ResultEnka)
    
    def characterImg(self,name):
        if self.charterImg:
            if name in self.charterImg:
                self.img = openUserImg(self.charterImg[name])
            else:
                self.img = None

    def startNameGeneration(self,key,uid,startPotoki,ResultEnka,signatureRes, teample):
        if not f"{uid}_{key.name.lower()}" in startPotoki:
            if self.randomImg:
                startPotoki[f"{uid}_{key.name.lower()}"] = Thread(target=generation,args=(key,self.assets,openUserImg(random.choice(self.img)),self.adapt,uid,ResultEnka,self.dowload,signatureRes,self.translateLang,self.splash, teample))
            else:
                startPotoki[f"{uid}_{key.name.lower()}"] = Thread(target=generation,args=(key,self.assets,self.img,self.adapt,uid,ResultEnka,self.dowload,signatureRes,self.translateLang,self.splash, teample))
            startPotoki[f"{uid}_{key.name.lower()}"].start()    

    def dowloadImg(self,startPotoki,ResultEnka):
        if self.dowload:
            for key in startPotoki:
                startPotoki[key].join()
            return ResultEnka
        return None

    def attributeSetup(self,lang = None,charterImg = None,
        img = None, name = None, adapt = False,
        randomImg = False, hide = False, dowload = False):
        chImg = {}
        if lang:
            if lang in supportLang:
                self.assets = Assets(lang=lang)
                self.lang = lang
        if randomImg:
            self.randomImg = randomImg

        if charterImg:
            if type(charterImg) == dict:
                for key in charterImg:
                    if not key in chImg:
                        chImg[key.lower()] = charterImg[key]
                self.charterImg = chImg
        if adapt:
            self.adapt = adapt
        if img:
            self.img = img
            if type(img) == list:
                if self.randomImg:
                    if len(img) > 1:
                        self.img = img
            else:
                randomImg = False
                if img:
                    self.img = openUserImg(img)
        if name:
            if type(name) == str:
                self.name = name.lower().replace(' ', '').split(",")
            else:
                pass
        if hide:
            self.hide = hide
        
        if dowload:
            self.dowload = dowload
