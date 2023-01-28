from os import path, remove
import sys
import time

from classes import SimpleJson

path_to_temp = path.join("pyjsv", "tests", "temp")

def unique_filename() -> str:
    return str(round(time.time() * 10000))