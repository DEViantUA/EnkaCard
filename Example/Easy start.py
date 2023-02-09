from aioenkanetworkcard import encbanner
import asyncio

async def card():
    async with encbanner.ENC() as encard:
        ENCpy = await encard.enc(uids = "811455610")
        return await encard.creat(ENCpy,1)

result = asyncio.run(card()) 

print(result)


#The result will be a dictionary:
# {"811455610": {"Diona": {"img": PillImage, "id": "10000056"}, {"Diona": {"img": PillImage, "id": "10000056"}, ... }}
