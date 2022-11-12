'''
This example will generate a card with a 
custom image, adapting the background to 
fit them, and return the result in the response.
'''

from enkanetworkcard import encbanner

client = encbanner.EnkaGenshinGeneration(img = "9.png", adapt = True, dowload = True) 

b = client.start(uids = 724281429)

print(b)
