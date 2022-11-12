#=====✦Description✦=====
'''
An example using multiple custom images 
for random selection. With adapting 
the background to the image.
'''

from enkanetworkcard import encbanner

ENC = encbanner.EnkaGenshinGeneration(img = ["8.png", "9.png"], adapt = True, randomImg = True) 

result = ENC.start(uids = 724281429)
