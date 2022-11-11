# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['enkanetworkcard', 'enkanetworkcard.src.utils']

package_data = \
{'': ['*'],
 'enkanetworkcard': ['dist/*',
                     'src/assets/*',
                     'src/assets/artifact/*',
                     'src/assets/background/*',
                     'src/assets/charterInfo/*',
                     'src/assets/constant/*',
                     'src/assets/elementColor/*',
                     'src/assets/font/*',
                     'src/assets/icon/*',
                     'src/assets/maska/*',
                     'src/assets/stars/*',
                     'src/assets/stats/*',
                     'src/assets/talants/*',
                     'src/assets/weapons/*']}

install_requires = \
['Pillow>=9.3.0,<10.0.0',
 'enkanetwork.py>=1.2.10,<2.0.0',
 'googletrans>=3.1.0a0,<4.0.0']

setup_kwargs = {
    'name': 'enkanetworkcard',
    'version': '0.1.2',
    'description': 'Wrapper module for enkanetwork.py for creating character cards.',
    'long_description': None,
    'author': 'None',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/DEViantUA/EnkaNetworkCard/wiki/Dokumentation-enkanetworkcard',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
