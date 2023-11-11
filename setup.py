# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['enkacard', 'enkacard.src.modal', 'enkacard.src.utils']

package_data = \
{'': ['*'],
 'enkacard': ['src/assets/*',
              'src/assets/InfoCharter/*',
              'src/assets/InfoCharterTwo/*',
              'src/assets/TEAMPLE4/artifact/*',
              'src/assets/TEAMPLE4/bg/*',
              'src/assets/TEAMPLE4/bgFrame/*',
              'src/assets/TEAMPLE4/stats/*',
              'src/assets/TEAMPLE4/weapon/*',
              'src/assets/TEAMPLE4/weaponFrame/*',
              'src/assets/constant/*',
              'src/assets/font/*',
              'src/assets/icon/*',
              'src/assets/stars/*',
              'src/assets/teapmleFive/*',
              'src/assets/teapmleFive/artifact/*',
              'src/assets/teapmleFive/background/*',
              'src/assets/teapmleFive/element/*',
              'src/assets/teapmleFive/stars/*',
              'src/assets/teapmleFive/stats/*',
              'src/assets/teapmleFive/talants/*',
              'src/assets/teapmleFive/weapon/*',
              'src/assets/teapmleOne/artifact/*',
              'src/assets/teapmleOne/background/*',
              'src/assets/teapmleOne/charterInfo/*',
              'src/assets/teapmleOne/maska/*',
              'src/assets/teapmleOne/stats/*',
              'src/assets/teapmleOne/talants/*',
              'src/assets/teapmleOne/weapons/*',
              'src/assets/teapmleSeven/artifact/*',
              'src/assets/teapmleSeven/background/*',
              'src/assets/teapmleSix/artifact/*',
              'src/assets/teapmleSix/background/*',
              'src/assets/teapmleSix/talants/*',
              'src/assets/teapmleTree/artifact/*',
              'src/assets/teapmleTree/background/*',
              'src/assets/teapmleTree/constant/closed/*',
              'src/assets/teapmleTree/constant/open/*',
              'src/assets/teapmleTree/maska/*',
              'src/assets/teapmleTree/name/*',
              'src/assets/teapmleTree/talants/*',
              'src/assets/teapmleTree/weapon/*',
              'src/assets/teapmleTwo/artifact/*',
              'src/assets/teapmleTwo/background/*',
              'src/assets/teapmleTwo/charterInfo/*',
              'src/assets/teapmleTwo/charter_element/*',
              'src/assets/teapmleTwo/infoUser/*',
              'src/assets/teapmleTwo/maska/*',
              'src/assets/teapmleTwo/stats/*',
              'src/assets/teapmleTwo/talants/*',
              'src/assets/teapmleTwo/weapon/*']}

install_requires = \
['Pillow>=9.4.0,<10.0.0',
 'asyncache>=0.3.1,<0.4.0',
 'cachetools>=5.2.0,<6.0.0',
 'enkanetwork.py>=1.4.0,<2.0.0']

setup_kwargs = {
    'name': 'enkacard',
    'version': '1.1.4',
    'description': 'An asynchronous module and API that allows you to connect to your bot the generation of Genshin character cards from the Enka.Network website.',
    'long_description': '<p align="center">\n <img src="https://github.com/DEViantUA/EnkaCard/blob/main/readmeFile/BannerCard.png?raw=true" alt="Баннер"/>\n</p>\n\n____\n<img src="https://github.com/DEViantUA/EnkaCard/blob/main/readmeFile/Shablon_01.png?raw=true" width = 38% alt="Баннер"/>[<img src="https://github.com/DEViantUA/EnkaCard/blob/main/readmeFile/dark/Shablon_02.png?raw=true" width = 6% alt="Баннер"/>](https://pypi.org/project/enkacard/)[<img src="https://github.com/DEViantUA/EnkaCard/blob/main/readmeFile/dark/Shablon_03.png?raw=true" width = 7% alt="Баннер"/>](https://discord.gg/shRUCDt4)[<img src="https://github.com/DEViantUA/EnkaCard/blob/main/readmeFile/dark/Shablon_04.png?raw=truee" width = 7% alt="Баннер"/>](https://github.com/DEViantUA/EnkaCard)[<img src="https://github.com/DEViantUA/EnkaCard/blob/main/readmeFile/dark/Shablon_05.png?raw=true" width = 6% alt="Баннер"/>](https://enka.network/)\n____\n\n## EnkaCard \nAn asynchronous module and API that allows you to connect to your bot the generation of Genshin character cards from the Enka.Network website. <br><br>\n* 5 templates to choose from.<br>\n* 2 profile templates.<br>\n* Customization of all cards with background adaptation.\n\n## Full Documentation:\n  - [Documentation EnkaCard](https://deviantua.github.io/EnkaCard-Documentation/) \n  - [API](https://deviantua.github.io/EnkaCard-Documentation/async/Other/api/)\n  - [Little Kazuha](https://discord.gg/fnh4WBbqDW) - Discord Bot, which perfectly demonstrates the work of the module. Just use the ```/profile``` command\n\n## Installation:\n```\npip install enkacard\n```\n\n## Launch:\n``` python\nfrom enkacard import encbanner\nimport asyncio\n\nasync def card():\n    async with encbanner.ENC() as encard:\n        ENCpy = await encard.enc(uids = "811455610")\n        return await encard.creat(ENCpy,1)\n\nresult = asyncio.run(card()) \n\nprint(result)\n```\n## Languages Supported\n| Languege    |  Code   | Languege    |  Code   | Languege    |  Code   |\n|-------------|---------|-------------|---------|-------------|---------|\n|  English    |     en  |  русский    |     ru  |  Chinese    |    chs  |\n|  Tiếng Việt |     vi  |  ไทย        |     th  | Taiwan     |    cht  |\n|  português  |     pt  | 한국어      |     kr  | deutsch    |     de  |\n|  日本語      |     jp  | 中文        |     zh  | español    |     es  |\n|  中文        |     zh  | Indonesian |     id  | français   |     fr  |\n\n\n## Sample Results:\n<details>\n<summary>Sample 1 template</summary>\n \n[![Adaptation][1]][1]\n \n[1]: https://github.com/DEViantUA/EnkaCard/blob/main/readmeFile/7.png?raw=true\n\n[![Without Adaptation][2]][2]\n \n[2]: https://github.com/DEViantUA/EnkaCard/blob/main/readmeFile/6.png?raw=true\n</details>\n\n\n<details>\n<summary>Sample 2 template</summary>\n \n[![Adaptation][3]][3]\n \n[3]: https://github.com/DEViantUA/EnkaCard/blob/main/readmeFile/4.png?raw=true\n  \n</details>\n\n\n<details>\n<summary>Sample 3 template</summary>\n \n[![Adaptation][4]][4]\n \n[4]: https://github.com/DEViantUA/EnkaCard/blob/main/readmeFile/5.png?raw=true\n \n</details>\n\n<details>\n<summary>Sample 4 template</summary>\n \n[![Without Adaptation MINI INFO][5]][5]\n \n[5]: https://github.com/DEViantUA/EnkaCard/blob/main/readmeFile/1.png?raw=true\n \n[![Without Adaptation FULL INFO][6]][6]\n \n[6]: https://github.com/DEViantUA/EnkaCard/blob/main/readmeFile/2.png?raw=true\n \n[![Adaptation MINI INFO][7]][7]\n \n[7]: https://github.com/DEViantUA/EnkaCard/blob/main/readmeFile/3.png?raw=true\n \n</details>\n\n',
    'author': 'None',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/DEViantUA/EnkaNetworkCard/wiki/Dokumentation-enkanetworkcard',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
