import json
from files import PathLike
from .interfaces import _IJsonLikeObj

class SimpleJson(_IJsonLikeObj):
    "Implement interface"
    
    @staticmethod
    def load_from_dict(to_json: dict) -> "SimpleJson":
        return SimpleJson(to_json)
    
    @staticmethod
    def upload_from_file(to_json: PathLike) -> "SimpleJson":
        with open(to_json) as json_file:
            return SimpleJson(json.loads(json_file.read()))
    
    def upload_to_dict(self) -> dict:
        return self.data
    
    def save_file(self, path: PathLike, mode="w+"):
        with open(path, mode) as json_file:
            json.dump(self.data, json_file)