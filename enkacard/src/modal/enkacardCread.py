from pydantic import BaseModel,Field
from typing import List, Optional,Dict,Union
from PIL import Image


class CharacterRank(BaseModel):
    id: Optional[int]
    rank: Optional[int]
    out: Optional[int]
    precent: Optional[int]

class AkashaRank(BaseModel):
    akasha: list[CharacterRank]


class Info(BaseModel):
    uid: Optional[str]
    lang: Optional[str]
    save: Optional[bool]

class Card(BaseModel):
    id: Optional[int]
    name: Optional[str]
    element: Optional[str]
    rarity: Optional[int]
    card: Optional[Union[str, bytes, Image.Image]]

    class Config:
        arbitrary_types_allowed = True

class PickleSize(BaseModel):
    name: Optional[str]
    size: Optional[int]
    text: Optional[str]

class EnkaCard(BaseModel):
    info: Optional[Info]
    card: Optional[List[Card]]
    character_id: Optional[List[Union[str,int]]]
    character_name: Optional[List[Union[str,int]]]
    pickle_size: Optional[List[PickleSize]]
    
    
    async def get_charter(self, setting = False, name = False):
        if setting:
            card_ids = [str(card.id) for card in self.card]

            if name:
                return {name: id for id, name in zip(self.character_id, self.character_name) if id in card_ids}
            return {id: name for id, name in zip(self.character_id, self.character_name) if id in card_ids}
        
        if name:
            return {name: id for id, name in zip(self.character_id, self.character_name)}
        return {id: name for id, name in zip(self.character_id, self.character_name)}

from typing import List, Optional
from pydantic import BaseModel, HttpUrl

class Player(BaseModel):
    name: Optional[str]
    uid: Optional[str]
    lang: Optional[str]
    achievement: Optional[int]
    level: Optional[int]
    world_level: Optional[int]
    abyss: Optional[str]
    avatar: Optional[HttpUrl]

class Characters(BaseModel):
    count: Optional[int]
    character_name: Optional[List[Union[str,int]]]
    character_id: Optional[List[Union[str,int]]]

    async def get_charter(self,name = False):
        if name:
            return {name: id for id, name in zip(self.character_id, self.character_name)}
        return {id: name for id, name in zip(self.character_id, self.character_name)}
    
class Profile(BaseModel):
    player: Optional[Player]
    characters: Optional[Characters]
    card: Optional[Union[str, bytes, Image.Image]]

    class Config:
        arbitrary_types_allowed = True
