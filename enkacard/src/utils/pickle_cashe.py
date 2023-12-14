import os
from os import PathLike
from zlib import decompress, compress
from pickle import loads
from pathlib import Path
from pickletools import optimize
import time

try:
    from cloudpickle import dumps
except ImportError:
    from pickle import dumps

MISSING = object()
pickle_name = [
    "data_characters","data_card"
]
def save_pkz(obj, file, *, protocol=5, compresslevel=9):
    if isinstance(file, int):
        with open(file, 'wb') as file:
            save_pkz(obj, file, protocol=protocol, compresslevel=compresslevel)
    elif isinstance(file, (str, bytes, PathLike)):
        path = Path(file).expanduser()
        temp = Path(f"{file}~").expanduser()
        
        with open(temp, 'wb') as file:
            save_pkz(obj, file, protocol=protocol, compresslevel=compresslevel)
        
        temp.replace(path)
    elif any(
        callable(getattr(file, name, None))
        for name in ['read', 'write']
    ):
        file.write(
            compress(
                optimize(
                    dumps(
                        obj,
                        protocol=protocol,
                    ),
                ),
                level=compresslevel,
            ),
        )
    else:
        raise TypeError(
            'expected int, str, bytes, path-like or file-like object, not'
            f" {file.__class__.__name__}"
        )


def load_pkz(
    file,
    default=MISSING,
    *,
    default_factory=MISSING,
    protocol=5,
    compresslevel=9,
):
    if isinstance(file, int):
        with open(file, 'rb') as file:
            return load_pkz(
                file,
                default,
                default_factory=default_factory,
                protocol=protocol,
                compresslevel=compresslevel,
            )
    elif isinstance(file, (str, bytes, PathLike)):
        path = Path(file).expanduser()
        temp = Path(f"{file}~").expanduser()
        
        if temp.exists():
            if path.exists():
                temp.unlink()
            else:
                temp.replace(path)
        elif not path.exists():
            if default is MISSING:
                if default_factory is MISSING:
                    raise FileNotFoundError(path)
                else:
                    obj = default_factory()
            else:
                obj = default
            
            save_pkz(obj, path, protocol=protocol, compresslevel=compresslevel)
        
        with open(path, 'rb') as file:
            return load_pkz(
                file,
                default,
                default_factory=default_factory,
                protocol=protocol,
                compresslevel=compresslevel,
            )
    elif any(
        callable(getattr(file, name, None))
        for name in ['read', 'write']
    ):
        return loads(decompress(file.read()))
    else:
        raise TypeError(
            'expected int, str, bytes, path-like or file-like object, not'
            f" {file.__class__.__name__}"
        )


from collections import UserDict

async def get_file_size(file_size_bytes):
    if file_size_bytes < 1024:
        return f"{file_size_bytes} Byte"
    elif 1024 <= file_size_bytes < 1024 * 1024:
        return f"{file_size_bytes / 1024:.2f} KB ({file_size_bytes} Byte)"
    elif 1024 * 1024 <= file_size_bytes < 1024 * 1024 * 1024:
        return f"{file_size_bytes / (1024 * 1024):.2f} MB ({file_size_bytes} Byte)"
    else:
        return f"{file_size_bytes / (1024 * 1024 * 1024):.2f} GB ({file_size_bytes} Byte)"

class PickleCache(UserDict):
    def __init__(self, uid) -> None:
        super().__init__()

        self.uid = uid
    
    def __getitem__(self, key):
        current_time = time.time()
        
        default = {'timestamp': current_time}
        
        try:
            value = super().__getitem__(key)
        except KeyError:
            value = load_pkz(Path(__file__).parent.parent / 'pickle_cashe' / f"{key}.pkz", default)
            
            super().__setitem__(key, value)
        
        if key == 'data_card':
            if current_time > value['timestamp'] + 5 * 60:
                self[key] = value = default
        
        return value
    
    def __setitem__(self, key, item):
        super().__setitem__(key, item)
        
        save_pkz(item, Path(__file__).parent.parent / 'pickle_cashe' / f"{key}.pkz")
    
    async def get_data(self, data):
        if self.uid in self['data_characters']:
            new_data = []
            true_id = []
            for keys in data:
                true_id.append(keys.id)
            
            for key in self['data_characters'][self.uid]:
                if not str(key) in str(true_id):
                    new_data.append(self['data_characters'][self.uid][key])
            return new_data
        
        return []
    
    async def add_data(self, data):
        self['data_characters'][self.uid] = {f"{key.id}": key for key in data}
        self['data_characters'] = self['data_characters']
    
    async def get_generator(self,teamplate):
        if not self.uid in self['data_card']:
            self['data_card'][self.uid] = {}
        if teamplate in self['data_card'][self.uid]:
            return self['data_card'][self.uid][teamplate]
        return []
            
    async def add_generator(self, teamplate,data):
        for key in data:
            if not self.uid in self['data_card']:
                self['data_card'][self.uid] = {}
            
            if not teamplate in self['data_card'][self.uid]:
                self['data_card'][self.uid][teamplate] = {}
                
            self['data_card'][self.uid][teamplate][key["id"]] = key
            
        self['data_card'] = self['data_card']
    
    async def setting_charters(self,pickles,data):
        
        if pickles["add_characters"]:
            await self.add_data(data)
            
        if pickles["get_characters"]:
            cash_pickle = await self.get_data(data)
            if cash_pickle != []:
                return data + cash_pickle
            
        return data
    
    async def size_pickle(self):
        data = []
        for key in pickle_name:
            file_path = Path(__file__).parent.parent / 'pickle_cashe' / f"{key}.pkz"
            if os.path.exists(file_path):
                file_size = os.path.getsize(file_path)
                text = f"File size '{key}' amounts to {await get_file_size(file_size)}"
                data.append({"name": key, "size":file_size , "text": text})
            else:
                data.append({"name": key, "size": 0 , "text": "File does not exist"})
        return data