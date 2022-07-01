from os import listdir
from os.path import isfile, join

from mirror_bot import MirrorBot
from mirror_bot.utils import MIRRORS


def is_mirror_file(filename: str):
    return isfile(join(MIRRORS, filename)) and filename.endswith('.mirror')

def list_mirrors():
    mirror_files = [file.replace('.mirror', '') for file in listdir(MIRRORS) if is_mirror_file(file)]
    for file in mirror_files: print(file)

def play_mirror(mirror_name: str):
    MirrorBot.play_mirror(mirror_name)

def record_mirror(mirror_name: str):
    MirrorBot.record_mirror(mirror_name)