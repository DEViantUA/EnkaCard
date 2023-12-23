from pydantic import BaseModel
from typing import Optional

class ImageInfo(BaseModel):
    filename: Optional[str]
    name: Optional[str]
    mime: Optional[str]
    extension: Optional[str]
    url: Optional[str]

class DataInfo(BaseModel):
    id: Optional[str]
    title: Optional[str]
    url_viewer: Optional[str]
    url: Optional[str]
    display_url: Optional[str]
    width: Optional[int]
    height: Optional[int]
    size: Optional[int]
    time: Optional[int]
    expiration: Optional[int]
    image: Optional[ImageInfo]
    thumb: Optional[ImageInfo]
    medium: Optional[ImageInfo]
    delete_url: Optional[str]

class EnkaCardLink(BaseModel):
    data: Optional[DataInfo]
    success: Optional[bool]
    status: Optional[int]