from os import path, remove
import sys
import time

from classes import SimpleJson, SimpleXml


path_to_samples = path.join("pyjsv", "tests", "samples")
path_to_temp = path.join("pyjsv", "tests", "temp")

def unique_filename() -> str:
    return str(round(time.time() * 10000))