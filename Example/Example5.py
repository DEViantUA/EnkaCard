'''
This example will generate a card with a 
custom image, adapting the background to 
fit them, and return the result in the response.
'''

from enkanetworkcard import encbanner

ENC = encbanner.EnkaGenshinGeneration(img = "9.png", adapt = True, dowload = True) 

result = ENC.start(uids = 724281429)

print(result)
