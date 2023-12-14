import pickle
import os
import gzip
    
pickle_name = [
    "data_characters","data_card"
]




class PiclkeCashe:
    def __init__(self, data, uid) -> None:
        self.data = data
        self.uid = uid

    async def delete_user_characters(self):
        if self.uid in self.cashe_data:
            del self.cashe_data[self.uid]
            await self.save_pickle("data_characters")
    
    async def delete_user_generate(self):
        if self.uid in self.cashe_data:
            del self.cashe_data[self.uid]
            await self.save_pickle("data_card")
    
    async def del_all(self):
        #Удаляем все данные кеша
        for key in pickle_name:
            del self.cashe_data
            await self.save_pickle(key)
            
    async def delete_characters_pickle(self):
        #Удаляем все данные о персонажах кеша
        del self.cashe_data
        await self.save_pickle("data_characters")
        
    async def delete_generate_pickle(self):
        #Удаляем все данные о генерации кеша
        del self.cashe_data
        await self.save_pickle("data_card")
            
    async def setting_delete(self,pickles):
        if pickles["delete_user_characters"]:
            await self.delete_user_characters()
        
        if pickles["delete_user_generate"]:
            await self.delete_user_generate()
            
        if pickles["delete_characters_pickle"]:
            await self.delete_characters_pickle()
        
        if pickles["delete_generate_pickle"]:
            await self.delete_generate_pickle()
            
        if pickles["delete_all_pickle"]:
            await self.del_all()
    
    

    