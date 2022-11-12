'''
This example will create cards with only 
the characters specified in the name and 
select random images for them.
'''

from enkanetworkcard import encbanner

ENC  = encbanner.EnkaGenshinGeneration(img = ["8.png", "9.png"], adapt = True, name = "Klee, Albedo", randomImg = True) 

result = ENC .start(uids = 724281429)
