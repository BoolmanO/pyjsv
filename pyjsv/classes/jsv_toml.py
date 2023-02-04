from __future__ import annotations
import tomlkit
from .files import PathLike, save_file
from .interfaces import _IJsonLikeObj


class SimpleToml(_IJsonLikeObj):
    def __init__(self, data: dict) -> None:
        self.data = data

    @staticmethod
    def upload_from_dict(to_toml: dict) -> SimpleToml:
        return SimpleToml(data=to_toml)

    @staticmethod
    def upload_from_str(toml: str) -> SimpleToml:
        return SimpleToml(data=dict(tomlkit.parse(toml)))

    @staticmethod
    def upload_from_file(path: PathLike) -> SimpleToml:
        with open(path, "r") as xml_file:
            data = tomlkit.parse(xml_file.read())
            return SimpleToml(data)

    def get_toml(self) -> str:
        return tomlkit.dumps(self.data)

    def save_file(self, path: PathLike) -> None:
        save_file(path,self.get_toml())

    def get_dict(self) -> dict:
        return self.data