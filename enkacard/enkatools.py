from .enc_error import ENCardError
from .src.modal import enkaToolsModel
import base64
from io import BytesIO
import aiohttp
from contextlib import AsyncExitStack

import_magic = False

try:
    import magic
except ImportError:
    import_magic = True
    import imghdr

IMAGE_TYPES = {
    'image/jpeg',
    'image/png',
}

async def download_image(session, url, headers=None, allow_redirects=True, use_range=None, offset=0, size=None, **kwargs):
    if headers is None:
        headers = {}

    params = {
        'headers': headers,
        'allow_redirects': allow_redirects,
        **kwargs,
    }

    if use_range is None:
        async with session.head(url, **params) as response:
            if response.headers.get('accept-ranges') == 'bytes':
                use_range = True
            else:
                use_range = False

    if use_range:
        if size is None:
            if offset:
                headers['range'] = f"bytes={offset}-"
        else:
            headers['range'] = f"bytes={offset}-{offset + size - 1}"

    async with session.get(url, headers=headers, allow_redirects=allow_redirects, **kwargs) as response:
        if response.status != 416:
            response.raise_for_status()

            buffer = BytesIO()
            async for data in response.content.iter_any():
                length = len(data)

                if use_range:
                    if size is not None and offset + length > offset + size:
                        buffer.write(data[:offset + size - offset])
                        break
                    else:
                        buffer.write(data)
                else:
                    buffer.write(data)

            return buffer.getvalue()

async def get_mimetype(session, url, size=2048, allow_redirects=True, **kwargs):
    async with session:
        data = await download_image(session, url, size=size, allow_redirects=allow_redirects, **kwargs)
        if import_magic:
            mime_type = imghdr.what(None, h=data)
            if mime_type:
                return mime_type
            else:
                return "application/octet-stream"
        else:
            return magic.Magic(mime=True).from_buffer(data)

async def is_valid(session, url, allow_redirects=True, **kwargs):
    async with session:
        try:
            async with session.head(url, allow_redirects=allow_redirects, **kwargs) as response:
                return response.status == 200
        except aiohttp.ClientError:
            return False


class Tools:
    def __init__(self) -> None:
        pass

    async def image_to_base64(self,image, format = "png"):
        buffered = BytesIO()
        image.save(buffered, format= format)
        img_str = base64.b64encode(buffered.getvalue())
        
        return img_str
    
    async def get_link_image(self,img, api_key = None):
        if api_key is None:
            raise ENCardError(800,'Get the API key on the page: https://api.imgbb.com/ (Click on "Get Api Key")')
        
        async with aiohttp.ClientSession() as session:
            url = 'https://api.imgbb.com/1/upload'
            headers = {
                'Accept': 'application/json'
            }
            
            par = {
                'key': api_key,
                'image': await self.image_to_base64(img) if not isinstance(img, str) else img
            }
            async with session.post(url, data=par, headers=headers) as req:
                data = await req.json()
                
                return enkaToolsModel.EnkaCardLink(**data)    

    async def get_pixv_headers(self):
        return {"referer": "https://www.pixiv.net/"}
    
    async def is_valid_image(self, url,session=None,allow_redirects=True,strict=False,**kwargs):
        async with AsyncExitStack() as stack:
            if url is None:
                session, url = url,session
            
            if session is None:
                session = await stack.enter_async_context(aiohttp.ClientSession())
                
            async with session:
                try:
                    async with session.head(url, allow_redirects=allow_redirects, **kwargs) as response:
                        if response.status != 200 or not response.headers.get('content-length'):
                            return False

                        content_type = response.headers.get('content-type')

                        if content_type == 'application/octet-stream' or strict:
                            use_range = response.headers.get('accept-ranges') == 'bytes'
                            content_type = await get_mimetype(session, url, use_range=use_range, allow_redirects=allow_redirects, **kwargs)

                        return content_type in IMAGE_TYPES
                except aiohttp.ClientError:
                    return False