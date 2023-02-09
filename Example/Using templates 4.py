from aioenkanetworkcard import encbanner
import asyncio

async def card():
    async with encbanner.ENC() as encard:
        ENCpy = await encard.enc(uids = "811455610")
        return await encard.creat(ENCpy,4)

result = asyncio.run(card()) 

print(result)

#The result will be a dictionary:
# {"card": {"1-4": PillImage, "5-8": PillImage}}
