#=====✦Description✦=====
'''
An example using a custom image. 
And adapting the background to the image.
'''

from enkanetworkcard import encbanner

client = encbanner.EnkaGenshinGeneration(img = "8.png", adapt = True) 

b = client.start(uids = 724281429)

