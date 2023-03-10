from pydantic import BaseModel, Field,validator
from typing import List
from PIL import Image



info = {"uid": '724281429', "Cards": [{"name": 'Чун Юнь', 'img': "<PIL.Image.Image image mode=RGBA size=1502x787 at 0x18854BD0700>", 'id': 10000036}]}


class EnkaCardCread(BaseModel):
    uid: int
    cards: list

class EnkaCardCharters(BaseModel):
    name: str
    id: int
    card: Image.Image
    class Config:
        arbitrary_types_allowed = True

