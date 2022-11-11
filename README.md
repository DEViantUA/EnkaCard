<p align="center">
 <img src="img/banner.jpg" alt="Баннер"/>
</p>

# EnkaNetworkCard
Wrapper for [EnkaNetwork.py](https://github.com/mrwan200/EnkaNetwork.py) creation to create character cards in Python.

## Navigation
* Installation
* Dependencies
* Launch
* Description of arguments
* Sample Results

## Installation:

```
pip install enkanetworkcard
```
Or you can copy the given repository.

### Dependencies:
  Dependencies that must be installed for the library to work:
  * googletrans-3.1.0a0
  * Pillow
  * requests
  * io
  * math
  * threading
  * datetime
  * random
  * enkanetwork
  * logging

## Launch:
``` python
from enkanetworkcard import encbanner

ENC = encbanner.EnkaGenshinGeneration() 

result = ENC.start(uids = 724281429)

print(result)

```

## Sample Results:

<img src="img/Example1.png" width='300' alt="Example1"/> <img src="img/Example2.png" width='300' alt="Example2"/> - The result of a custom images and adaptation.
<img src="img/Example3.png" width='300' alt="Example3"/> <img src="img/Example4.png" width='300' alt="Example4"/> - Usual result.
