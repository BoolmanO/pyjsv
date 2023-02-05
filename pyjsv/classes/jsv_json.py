from __future__ import annotations
import json
from .files import PathLike, OpenTextMode
from .interfaces import _IJsonLikeObj


class SimpleJson(_IJsonLikeObj):
    @staticmethod
    def from_dict(to_json: dict) -> SimpleJson:
        return SimpleJson(to_json)
    
    @staticmethod
    def from_string(to_json: str) -> SimpleJson:
        return SimpleJson(json.loads(to_json))

    @staticmethod
    def from_file(path: PathLike) -> SimpleJson:
        with open(path, "r") as json_file:
            return SimpleJson(json.loads(json_file.read()))

    def get_json(self) -> str:
        "Returns the `toml` string representation of the data stored in the class."
        return json.dumps(self.data)

    def get_dict(self) -> dict:
        "Returns the dictionary representation of the data stored in the class."
        return self.data

    def save_file(self, path: PathLike, mode: OpenTextMode="+w") -> None:
        "Saves the data (in `json` format) stored in the class to a file."
        with open(path, mode) as json_file:
            json.dump(self.data, json_file, indent=4)