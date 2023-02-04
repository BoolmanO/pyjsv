from __future__ import annotations
import json
from .files import PathLike
from .interfaces import _IJsonLikeObj


class SimpleJson(_IJsonLikeObj):
    @staticmethod
    def upload_from_dict(to_json: dict) -> SimpleJson:
        return SimpleJson(to_json)
    
    @staticmethod
    def upload_from_str(to_json: str) -> SimpleJson:
        return SimpleJson(json.loads(to_json))

    @staticmethod
    def upload_from_file(path: PathLike) -> SimpleJson:
        with open(path, "r") as json_file:
            return SimpleJson(json.loads(json_file.read()))
    
    def save_file(self, path: PathLike, mode="+w"):
        with open(path, mode) as json_file:
            json.dump(self.data, json_file)
            
    def get_dict(self) -> dict:
        return self.data