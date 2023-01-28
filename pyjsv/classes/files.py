from os.path import join, exists
from os import PathLike

def save_file(path: PathLike, data: str, mode="+w"):
    with open(path, mode) as file:
        file.write(data)