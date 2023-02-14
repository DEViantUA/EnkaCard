<p align="center">
  <img src="https://raw.githubusercontent.com/DEViantUA/EnkaNetworkCard/main/img/banner.jpg" alt="Баннер"/>
</p>

**<p align="center"> <a href="https://github.com/DEViantUA/EnkaNetworkCard/wiki/EnkaNetworkCard-RU">Русская версия</a> | <a href="https://github.com/DEViantUA/EnkaNetworkCard/tree/main/Example">Example</a> | <a href = "https://discord.gg/xq5EXu94"> Discord <a> </p>**

# EnkaNetworkCard
Wrapper for [EnkaNetwork.py](https://github.com/mrwan200/EnkaNetwork.py) to create character cards in Python.

## Full Documentation:

EN: 
  - [Documentation EnkanetworkCard](https://deviantua.github.io/EnkaNetworkCard-Documentation/) 
  - [API](https://deviantua.github.io/EnkaNetworkCard-Documentation/async/Other/api/) 

## Navigation
* Installation
* Dependencies
* Launch
* Languages Supported
* Sample Results

## Installation:
```
pip install aioenkanetworkcard
```

### Dependencies:
  Dependencies that must be installed for the library to work:
  * Pillow
  * requests
  * io
  * math
  * datetime
  * random
  * enkanetwork
  * logging

## Launch:
``` python
from aioenkanetworkcard import encbanner
import asyncio

async def card():
    async with encbanner.ENC() as encard:
        ENCpy = await encard.enc(uids = "811455610")
        return await encard.creat(ENCpy,1)

result = asyncio.run(card()) 

print(result)
```
## Languages Supported
| Languege    |  Code   | Languege    |  Code   |
|-------------|---------|-------------|---------|
|  English    |     en  |  русский    |     ru  |
|  Tiếng Việt |     vi  |  ไทย        |     th  |
|  português  |     pt  | 한국어      |     kr  |
|  日本語      |     jp  | 中文        |     zh  |
|  中文        |     zh  | Indonesian |     id  |
|  français   |     fr  | español    |     es  |
|  deutsch    |     de  | Taiwan     |    cht  |
|  Chinese    |    chs  |      |      |

## Sample Results:


### The result of a custom images and adaptation (template= 1).
<img src="https://raw.githubusercontent.com/DEViantUA/EnkaNetworkCard/main/img/Example1.png" width='300' alt="Example1"/> <img src="https://raw.githubusercontent.com/DEViantUA/EnkaNetworkCard/main/img/Example2.png" width='300' alt="Example2"/> 

### Usual result (template= 1).
<img src="https://raw.githubusercontent.com/DEViantUA/EnkaNetworkCard/main/img/Example3.png" width='300' alt="Example3"/> <img src="https://raw.githubusercontent.com/DEViantUA/EnkaNetworkCard/main/img/Example4.png" width='300' alt="Example4"/> 

### The result of a custom images and adaptation (template= 2).
<img src="https://raw.githubusercontent.com/DEViantUA/EnkaNetworkCard/main/img/Example5.png.png" width='300' alt="namecard = True"/> <img src="https://raw.githubusercontent.com/DEViantUA/EnkaNetworkCard/main/img/Example6.png.png" width='300' alt="namecard = False"/> 

### Usual result (template= 2).
<img src="https://raw.githubusercontent.com/DEViantUA/EnkaNetworkCard/main/img/Example8.png.png" width='300' alt="namecard = True"/> <img src="https://raw.githubusercontent.com/DEViantUA/EnkaNetworkCard/main/img/Example7.png.png" width='300' alt="namecard = False"/> 


### Usual result (template= 3).
<img src="https://raw.githubusercontent.com/DEViantUA/EnkaNetworkCard/main/img/Венти_11_12_2022 17_15.png" width='300' alt="namecard = True"/> <img src="https://raw.githubusercontent.com/DEViantUA/EnkaNetworkCard/main/img/Чжун%20Ли_11_12_2022%2017_15.png" width='300' alt="namecard = False"/> 

### Usual result (template= 4).
<img src="https://raw.githubusercontent.com/DEViantUA/EnkaNetworkCard/main/img/Example9.png" width='500' alt="MINI_VERSIA = True"/> 
<img src="https://raw.githubusercontent.com/DEViantUA/EnkaNetworkCard/main/img/Example10.png" alt="MAX_VERSIA = False"/> 
