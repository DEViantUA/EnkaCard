# Copyright 2022 DEViantUa <t.me/deviant_ua>
# All rights reserved.
from enkanetwork import EnkaNetworkAPI,Assets
import logging,asyncio,random, os, datetime,time
from threading import Thread
from .src.utils.CreatBanner import weaponAdd,nameBanner,stats,constant,create_picture,talants,artifacAdd,signature,appedFrame,openUserImg 
from .src.utils.translate import translate
from .enc_error import ENCardError

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
logging.getLogger('enkanetwork.assets').setLevel(logging.CRITICAL)

def upload():
    client = EnkaNetworkAPI()
    async def main():
        async with client:
            await client.update_assets()
    asyncio.run(main())

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

def generation(charter,assets,img,adapt,uid,RESULT, save,signatureRes,lvl):
    try:
        characters = charter
        frame = create_picture(assets,characters.id,img,adapt)
        weaponRes = weaponAdd(characters.equipments[-1],lvl)
        nameRes = nameBanner(characters,assets,lvl) 
        statRes = stats(characters,assets)
        constantRes = constant(characters,assets)
        talatsRes = talants(characters)
        artifacRes, artifactSet = artifacAdd(characters)
        result = appedFrame(frame,weaponRes,nameRes,statRes,constantRes,talatsRes,artifacRes,artifactSet,signatureRes)
        if not save:
            saveBanner(uid,result,charter.name)
        else:
            if not uid in RESULT:
                RESULT[uid] = {}
            if not charter.name in RESULT[uid]:
                RESULT[uid][charter.name] = result
        return None
    except Exception as e:
        print(f"Ошибка: {e}")

class EnkaGenshinGeneration:
    def __init__(self,lang = "ru",charterImg = None,
            img = None, name = None, adapt = False,
            randomImg = False, hide = False, dowload = False):
        self.assets = Assets(lang=lang)
        self.lang = lang
        self.lvl = translate(lang = self.lang)
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

    def start(self,uids):
        startPotoki = {}
        ResultEnka = {}
        uids = uidCreat(uids)
        for uid in uids:
            r = asyncio.run(info(uid,self.lang))
            if not r:
                continue
            signatureRes = signature(self.hide,uid)
            for key in r.characters:
                self.characterImg(key.name.lower())
                if self.name:
                    if not key.name.lower() in self.name:
                        continue
                self.startNameGeneration(key,uid,startPotoki,ResultEnka,signatureRes)
                time.sleep(0.3)
        return self.dowloadImg(startPotoki,ResultEnka)

    def characterImg(self,name):
        if self.charterImg:
            if name in self.charterImg:
                self.img = openUserImg(self.charterImg[name])
            else:
                self.img = None

    def startNameGeneration(self,key,uid,startPotoki,ResultEnka,signatureRes):
        if not f"{uid}_{key.name.lower()}" in startPotoki:
            if self.randomImg:
                startPotoki[f"{uid}_{key.name.lower()}"] = Thread(target=generation,args=(key,self.assets,openUserImg(random.choice(self.img)),self.adapt,uid,ResultEnka,self.dowload,signatureRes,self.lvl))
            else:
                startPotoki[f"{uid}_{key.name.lower()}"] = Thread(target=generation,args=(key,self.assets,self.img,self.adapt,uid,ResultEnka,self.dowload,signatureRes,self.lvl))
            startPotoki[f"{uid}_{key.name.lower()}"].start()    
    
    def dowloadImg(self,startPotoki,ResultEnka):
        if self.dowload:
            for key in startPotoki:
                startPotoki[key].join()
            return ResultEnka
        return None
