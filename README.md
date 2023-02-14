<p align="center">
 <img src="https://github.com/DEViantUA/EnkaCard/blob/main/readmeFile/BannerCard.png?raw=true" alt="Баннер"/>
</p>

____
<img src="https://github.com/DEViantUA/EnkaCard/blob/main/readmeFile/Shablon_01.png?raw=true" width = 38% alt="Баннер"/>[<img src="https://github.com/DEViantUA/EnkaCard/blob/main/readmeFile/white/Shablon_02.png?raw=true" width = 6% alt="Баннер"/>](https://pypi.org/project/enkacard/) [<img src="https://github.com/DEViantUA/EnkaCard/blob/main/readmeFile/white/Shablon_03.png?raw=true" width = 7% alt="Баннер"/>](https://discord.gg/shRUCDt4)[<img src="https://github.com/DEViantUA/EnkaCard/blob/main/readmeFile/white/Shablon_04.png?raw=true" width = 7% alt="Баннер"/>](https://github.com/DEViantUA/EnkaCard)[<img src="https://github.com/DEViantUA/EnkaCard/blob/main/readmeFile/white/Shablon_05.png?raw=true" width = 6% alt="Баннер"/>](https://enka.network/)
____

## EnkaCard
An asynchronous module and API that allows you to connect to your bot the generation of Genshin character cards from the Enka.Network website. <br><br>
:white_medium_square: 5 templates to choose from.<br>
:white_medium_square: 2 profile templates.<br>
:white_medium_square: Customization of all cards with background adaptation.

## Full Documentation:
  - [Documentation EnkaCard](https://deviantua.github.io/EnkaCard-Documentation/) 
  - [API](https://deviantua.github.io/EnkaCard-Documentation/async/Other/api/)
  - [Little Kazuha](https://discord.gg/TwuBfDbE) - Discord Bot, which perfectly demonstrates the work of the module. Just use the ```/profile``` command

## Installation:
```
pip install enkacard
```

## Launch:
``` python
from enkacard import encbanner
import asyncio

async def card():
    async with encbanner.ENC() as encard:
        ENCpy = await encard.enc(uids = "811455610")
        return await encard.creat(ENCpy,1)

result = asyncio.run(card()) 

print(result)
```
## Languages Supported
| Languege    |  Code   | Languege    |  Code   | Languege    |  Code   |
|-------------|---------|-------------|---------|-------------|---------|
|  English    |     en  |  русский    |     ru  |  Chinese    |    chs  |
|  Tiếng Việt |     vi  |  ไทย        |     th  | Taiwan     |    cht  |
|  português  |     pt  | 한국어      |     kr  | deutsch    |     de  |
|  日本語      |     jp  | 中文        |     zh  | español    |     es  |
|  中文        |     zh  | Indonesian |     id  | français   |     fr  |


## Sample Results:
<details>
<summary>Sample 1 template</summary>
 
[![Adaptation][1]][1]
 
[1]: https://github.com/DEViantUA/EnkaCard/blob/main/readmeFile/7.png?raw=true

[![Without Adaptation][2]][2]
 
[2]: https://github.com/DEViantUA/EnkaCard/blob/main/readmeFile/6.png?raw=true
</details>


<details>
<summary>Sample 2 template</summary>
 
[![Adaptation][3]][3]
 
[3]: https://github.com/DEViantUA/EnkaCard/blob/main/readmeFile/4.png?raw=true
  
</details>


<details>
<summary>Sample 3 template</summary>
 
[![Adaptation][4]][4]
 
[4]: https://github.com/DEViantUA/EnkaCard/blob/main/readmeFile/5.png?raw=true
 
</details>

<details>
<summary>Sample 4 template</summary>
 
[![Without Adaptation MINI INFO][5]][5]
 
[5]: https://github.com/DEViantUA/EnkaCard/blob/main/readmeFile/1.png?raw=true
 
[![Without Adaptation FULL INFO][6]][6]
 
[6]: https://github.com/DEViantUA/EnkaCard/blob/main/readmeFile/2.png?raw=true
 
[![Adaptation MINI INFO][7]][7]
 
[7]: https://github.com/DEViantUA/EnkaCard/blob/main/readmeFile/3.png?raw=true
 
</details>
