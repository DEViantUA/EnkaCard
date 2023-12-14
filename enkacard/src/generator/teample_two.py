import asyncio
from PIL import ImageDraw,Image
from ..utils import pill, git
from enkanetwork.enum import EquipmentsType
from .two import background, artifact, weapon, constant, skill, stat, prop
_of = git.ImageCache()







class Creat:
    def __init__(self,characters,lang,img,hide,uid,name) -> None:
        self.character = characters
        self.lang = lang["lvl"]
        self.img = img
        self.hide = hide
        self.uid = uid
        self.name = name
        
        
    async def start(self):
        pass