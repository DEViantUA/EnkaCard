<p align="center">
 <img src="https://github.com/DEViantUA/EnkaCard/blob/main/readmeFile/BannerCard3.png?raw=true" alt="Баннер"/>
</p>

____
[<img src="https://raw.githubusercontent.com/DEViantUA/EnkaCard/main/readmeFile/icon_ream_me/IconReadMe_01.png" width="26%" height="1" alt="Изображение 1"/>](https://raw.githubusercontent.com/DEViantUA/EnkaCard/main/readmeFile/icon_ream_me/IconReadMe_01.png)
[<img src="https://raw.githubusercontent.com/DEViantUA/EnkaCard/main/readmeFile/icon_ream_me/IconReadMe_02.png" width="8%" alt="Изображение 2"/>](https://t.me/enkacardchat)
[<img src="https://raw.githubusercontent.com/DEViantUA/EnkaCard/main/readmeFile/icon_ream_me/IconReadMe_03.png" width="8%" alt="Изображение 3"/>](https://github.com/DEViantUA/EnkaCard)
[<img src="https://raw.githubusercontent.com/DEViantUA/EnkaCard/main/readmeFile/icon_ream_me/IconReadMe_04.png" width="8%" alt="Изображение 4"/>](https://enka.network/)
[<img src="https://raw.githubusercontent.com/DEViantUA/EnkaCard/main/readmeFile/icon_ream_me/IconReadMe_05.png" width="8%" alt="Изображение 5"/>](https://pypi.org/project/enkacard/)
[<img src="https://raw.githubusercontent.com/DEViantUA/EnkaCard/main/readmeFile/icon_ream_me/IconReadMe_06.png" width="8%" alt="Изображение 6"/>](https://www.patreon.com/deviantapi)
[<img src="https://raw.githubusercontent.com/DEViantUA/EnkaCard/main/readmeFile/icon_ream_me/IconReadMe_07.png" width="8%" alt="Изображение 6"/>](https://akasha.cv/)





____

## EnkaCard
An asynchronous module and API that allows you to connect to your bot the generation of Genshin character cards from the Enka.Network website. <br><br>
:white_medium_square: [Documentation](https://github.com/DEViantUA/EnkaCard/wiki)<br>
:white_medium_square: [Telegram Bot](https://t.me/mf_morax_bot)<br>
:white_medium_square: [Generation results](https://github.com/DEViantUA/EnkaCard/wiki/Resultate)<br>
:white_medium_square: [StarRailCard](https://github.com/DEViantUA/StarRailCard)<br>
:white_medium_square: [Additional module](https://github.com/DEViantUA/ENCard)<br>
:white_medium_square: [Assets](https://github.com/DEViantUA/EnkaCard)
## Installation:
```
pip install enkacard
```

## Launch:
``` python
from enkacard import encbanner
import asyncio

async def card():
    async with encbanner.ENC(uid = "811455610") as encard:
        return await encard.creat()

result = asyncio.run(card()) 

print(result)
```

<details>
<summary>Launch Profile</summary>

``` python
from enkacard import encbanner
import asyncio

async def card():
    async with encbanner.ENC(uid = "811455610") as encard:
        return await encard.profile(card = True)

result = asyncio.run(card()) 

print(result)
```
</details>

<details>
<summary>Update enkanetwork.py data</summary>

``` python
from enkacard import encbanner
import asyncio

async def main():
    await encbanner.update()

result = asyncio.run(main()) 

print(result)
```
> _**Aliternative method: [Tools](https://github.com/DEViantUA/EnkaCard/wiki/Tools)**_

</details>

## Languages Supported
| Languege    |  Code   | Languege    |  Code   | Languege    |  Code   |
|-------------|---------|-------------|---------|-------------|---------|
|  English    |     en  |  русский    |     ru  |  Chinese    |    chs  |
|  Tiếng Việt |     vi  |  ไทย        |     th  | Taiwan     |    cht  |
|  português  |     pt  | 한국어      |     kr  | deutsch    |     de  |
|  日本語      |     jp  | 中文        |     zh  | español    |     es  |
|  中文        |     zh  | Indonesian |     id  | français   |     fr  |
|  Khaenri'ah  |     kh  | Khaenri'ah |

