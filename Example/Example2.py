#=====✦Description✦=====
'''
An example using a custom image. 
And adapting the background to the image.
'''

from enkanetworkcard import encbanner

ENC = encbanner.EnkaGenshinGeneration(img = "8.png", adapt = True) 

result = ENC.start(uids = 724281429)
