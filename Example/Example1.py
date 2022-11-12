#=====✦Description✦=====
'''
A simple example, with automatic saving of 
finished results to the EnkaImg folder
The folder will be created automatically
'''

from enkanetworkcard import encbanner

ENC = encbanner.EnkaGenshinGeneration() 

result = ENC.start(uids = 724281429)

