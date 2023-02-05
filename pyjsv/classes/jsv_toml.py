from __future__ import annotations
import tomlkit
from .files import PathLike, save_file, OpenTextMode
from .interfaces import _IJsonLikeObj


class SimpleToml(_IJsonLikeObj):
    def __init__(self, data: dict):
        self.data = data

    @staticmethod
    def from_dict(to_toml: dict) -> SimpleToml:
        return SimpleToml(data=to_toml)

    @staticmethod
    def from_string(toml: str) -> SimpleToml:
        return SimpleToml(data=dict(tomlkit.parse(toml)))

    @staticmethod
    def from_file(path: PathLike) -> SimpleToml:
        with open(path, "r") as toml_file:
            data = tomlkit.parse(toml_file.read())
            return SimpleToml(data)

    def get_toml(self) -> str:
        "Returns the `toml` string representation of the data stored in the class."
        return tomlkit.dumps(self.data)

    def get_dict(self) -> dict:
        "Returns the dictionary representation of the data stored in the class."
        return self.data

    def save_file(self, path: PathLike, mode: OpenTextMode="+w") -> None:
        "Saves the data (in `toml` format) stored in the class to a file."
        save_file(path, self.get_toml(), mode)