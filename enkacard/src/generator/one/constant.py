from ...utils import pill, git

_of = git.ImageCache()


class Constant:
    def __init__(self,constant, element) -> None:
        self.constant = constant
        self.element = element
    
    async def creat_open(self):
        background = await _of.download_icon_constant(element = f"OPEN_CONST_{self.element}",unlock=self.constant.unlocked, resizes = (108,112))
        icon = await pill.get_dowload_img(self.constant.icon.url, size=((58,58)))
        background.alpha_composite(icon, (25,29))
        
        return background
    
    async def creat_closed(self):
        background = await _of.download_icon_constant(element = f"CLOSE_CONST_{self.element}",unlock=self.constant.unlocked, resizes = (108,112))
        icon = await pill.get_dowload_img(self.constant.icon.url, size=((58,58)))
        background.alpha_composite(icon, (25,29))
        closed_icon = await _of.closed_const
        background.alpha_composite(closed_icon.resize((69,69)), (20,23))
        
        return background
    
    async def start(self):
        if self.constant.unlocked:
            icon = await self.creat_open()
        else:
            icon = await self.creat_closed()
        
        return icon