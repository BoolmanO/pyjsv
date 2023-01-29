from __future__ import annotations
import json
from .files import PathLike
from .interfaces import _IJsonLikeObj

class SimpleJson(_IJsonLikeObj):
    "Implement interface"
    
    @staticmethod
    def upload_from_dict(to_json: dict) -> SimpleJson:
        return SimpleJson(to_json)
    
    @staticmethod
    def upload_from_file(to_json: PathLike) -> SimpleJson:
        with open(to_json) as json_file:
            return SimpleJson(json.loads(json_file.read()))
        
    @staticmethod
    def upload_from_str(to_json: str) -> SimpleJson:
        return SimpleJson(json.loads(to_json))
    
    def upload_to_dict(self) -> dict:
        return self.data
    
    def save_file(self, path: PathLike, mode="+w"):
        with open(path, mode) as json_file:
            json.dump(self.data, json_file)
            
    def get_dict(self):
        return self.data