from ...utils import options

class Prop:
    def __init__(self, artifact) -> None:
        self.artifact = artifact
        self.prop_value = {}
        self.props = {}
        
    async def creat_prop_value(self):
        for key in self.artifact.detail.substats:      
            self.prop_value[key.prop_id] = key.value
    
    async def creat_prop(self):
        for key in self.artifact.props:
            value = self.prop_value.get(key.prop_id, 0)
            self.props[key.prop_id] = {"name": key.prop_id, "main": options.data_prop_json.get(str(key.id), {}).get("position", 0), "sub": options.data_prop_json.get(str(key.id), {}).get("efficiency", 0), "value": value}
    
    async def start(self):
        await self.creat_prop_value()
        await self.creat_prop()
        
        return self.props
        
        
    
    