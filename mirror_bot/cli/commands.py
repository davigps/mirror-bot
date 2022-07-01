from mirror_bot import MirrorBot
from mirror_bot.utils import delete_mirror_file, get_mirror_files


def list_mirrors():
    mirror_files = get_mirror_files()
    for file in mirror_files: print(file)

def delete_mirror(mirror_name: str):
    mirror_files = get_mirror_files()

    if mirror_name not in mirror_files:
        raise Exception(f'"{mirror_name}" mirror does not exist!')
    
    delete_mirror_file(mirror_name)
    print(f'"{mirror_name}" mirror successfully deleted!')

def play_mirror(mirror_name: str):
    MirrorBot.play_mirror(mirror_name)

def record_mirror(mirror_name: str):
    MirrorBot.record_mirror(mirror_name)
