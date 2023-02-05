import asyncio
from enkanetwork import EnkaNetworkAPI,Assets
import asyncio,random,os,datetime
from .src.utils.CreatBannerTree import generationTree
from .src.utils.CreatBannerTwo import generationTwo, creatUserInfo
from .src.utils.CreatBannerOne import generationOne, signature, openUserImg 
from .src.utils.CreatBannerFour import generationFour
from .src.utils.userProfile import creatUserProfile
from .src.utils.translation import translationLang,supportLang
from .enc_error import ENCardError


async def upload():
    async with EnkaNetworkAPI() as ena:
        await ena.update_assets()

def uidCreat(uids):
    if type(uids) == int or type(uids) == str:
        return str(uids).replace(' ', '').split(",")
    else:
        raise ENCardError(5,"The UIDS parameter must be a number or a string. To pass multiple UIDs, separate them with commas.\nExample: uids = 55363 or uids = '55363,58999,567862,...'")

async def saveBanner(uid,res,name):
    data = datetime.datetime.now().strftime("%d_%m_%Y %H_%M")
    path = os.getcwd()
    try:
        os.mkdir(f'{path}/AioEnkaImg')
    except:
        pass
    try:
        os.mkdir(f'{path}/AioEnkaImg/{uid}')
    except:
        pass
    res.save(f"{path}/AioEnkaImg/{uid}/{name}_{data}.png")


def sorting(result):
    enc_card = {}
    for key in result:
        if not key["uid"] in enc_card:
            enc_card[key["uid"]] = {}
        if not key["name"] in enc_card[key["uid"]]:
            enc_card[key["uid"]][key["name"]] = key["card"]

    return enc_card



class ENC:
    def __init__(self,lang = "ru", characterImgs = None,
            img = None, characterName = None, adapt = False,
            randomImg = False, hide = False, save = False, nameCards = False, splashArt = False, miniInfo = True) :

        if lang in supportLang:
            self.assets = Assets(lang=lang)
            self.lang = lang
            self.translateLang = translationLang[self.lang]
        else:
            raise ENCardError(6,"Dislike language List of available languages: en, ru, vi, th, pt, kr, jp, zh, id, fr, es, de, chs, cht.\nRead more in the documentation: https://github.com/DEViantUA/EnkaNetworkCard")

        self.splashArt = splashArt
        self.nameCards = nameCards
        self.adapt = adapt
        self.save = save
        self.hide = hide
        self.characterName = characterName
        self.img = None
        self.dopImg = img
        self.randomImg = randomImg
        self.characterImgs = characterImgs
        self.miniInfo = miniInfo
        if characterImgs:
            if isinstance(characterImgs, dict):
                chImg = {}
                for key in characterImgs:
                    if not key in chImg:
                        chImg[key.lower()] = characterImgs[key]
                self.characterImgs = chImg
            else:
                raise ENCardError(4,"The charterImg parameter must be a dictionary, where the key is the name of the character, and the parameter is an image.\nExample: charterImg = {'Klee': 'img.png'} or {'Klee': 'img.png', 'Xiao': 'img2.jpg', ...}")
        
        if characterName:
            if isinstance(characterName, str):
                self.characterName = characterName.lower().replace(' ', '').split(",")
            else:
                raise ENCardError(3,"The name parameter must be a string, to pass multiple names, list them separated by commas.\nExample: name = 'Klee' or name = 'Klee, Xiao'")

        if isinstance(img, list):
            if self.randomImg:
                if len(img) > 1:
                    self.img = img
                else:
                   raise ENCardError(2, "The list of images must consist of 2 or more.\nExample: img = ['1.png','2.png', ...]") 
            else:
                raise ENCardError(1, "For a list of images, you need to pass the randomImg parameter\nExample: randomImg = True")

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        pass

    async def profile(self,enc, image = True):
        for key in enc:
            profile = enc[key].player
            uid = key
            break
        itog = await creatUserProfile(image,profile,self.translateLang,self.hide,uid,self.assets)

        return itog

    async def enc(self,uids = None):
        result = {}
        uids = uidCreat(uids)
        async with EnkaNetworkAPI(lang=self.lang) as client:
            for uid in uids:
                if not uid in result:
                    result[uid] = None
                r = await client.fetch_user(uid)
            if r.characters:
                result[uid] = r
        return result

    async def characterImg(self,name):
        if name in self.charterImg:
            self.img = await openUserImg(self.charterImg[name])
        else:
            self.img = None

    async def creat(self, enc, template = 1):
        if not self.img and self.dopImg:
            self.img = await openUserImg(self.dopImg)
            self.randomImg = False
        template = int(template)
        task = []
        if template != 4:
            for uid in enc:
                r = enc[uid]
                if not r:
                    continue
                if template == 1:
                    signatureRes = signature(self.hide,uid)
                elif template == 2:
                    signatureRes = await creatUserInfo(self.hide,uid,r.player,self.translateLang)
                else:
                    if self.hide:
                        signatureRes = "UID: Hide"
                    else:
                        signatureRes = f"UID: {uid}"
                for key in r.characters:
                    if self.characterName:
                        if not key.name.replace(' ', '').lower() in self.characterName:
                            continue
                    if self.characterImgs:
                        await self.characterImg(key.name.lower())

                    if self.nameCards and template == 2:
                        signatureRes = await creatUserInfo(self.hide,uid,r.player,self.translateLang,key.image.icon.filename.replace("CostumeFloral","").split("AvatarIcon_")[1],self.nameCards)
                    
                    if self.randomImg:
                        task.append(self.generation(key,await openUserImg(random.choice(self.img)),uid,signatureRes,template))
                    else:
                        task.append(self.generation(key,self.img,uid,signatureRes,template))

            result = await asyncio.gather(*task)
            return sorting(result)
        else:
            return await self.teampleFour(enc)

    async def generation(self,charter,img,uid,signatureRes,teample = 1):
        if teample == 1:
            result = await generationOne(charter,self.assets,img,self.adapt,signatureRes,self.translateLang["lvl"],self.splashArt)
        elif teample == 2:
            result =  await generationTwo(charter,self.assets,img,self.adapt,signatureRes,self.translateLang,self.splashArt)
        else:
            result =  await generationTree(charter,self.assets,img,self.adapt,signatureRes,self.translateLang,self.splashArt)
        if self.save:
            await saveBanner(uid,result, charter.name)
            return {"uid": uid, "name": charter.name, "card": result}
        else:
            return {"uid": uid, "name": charter.name, "card": result}

    async def teampleFour(self,enc):
        charterList = []
        result = {"1-4": None, "5-8": None}
        for uid in enc:
            r = enc[uid]
            if not r:
                continue
            if self.hide:
                signatureRes = "UID: Hide"
            else:
                signatureRes = f"UID: {uid}"
            for key in r.characters:
                charterList.append(key)
                if len(charterList) == 4:
                    result[i] = await generationFour(charterList,self.assets,self.translateLang,self.miniInfo,r.player.nickname,signatureRes)
                    charterList = []
                    i = "5-8"
            if charterList != []:
                result[i] = await generationFour(charterList,self.assets,self.translateLang,self.miniInf,r.player.nickname,signatureRes) 
            

        if self.save:
            for key in result:
                await saveBanner(uid,result[key],key)
        return {"uid": uid,"card": result}


