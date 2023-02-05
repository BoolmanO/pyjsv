from typing import Type
from os.path import join, exists
from os import PathLike


OpenTextMode = Type[str]

def save_file(path: PathLike, data: str, mode: OpenTextMode) -> None:
    with open(path, mode) as file:
        file.write(data)