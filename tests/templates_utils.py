import time

def unique_filename() -> str:
    return str(round(time.time() * 10000))