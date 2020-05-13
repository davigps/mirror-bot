from time import sleep
from pathlib import Path
from pydub import AudioSegment, playback

ROOT = Path('.').cwd()
BIP = ROOT.joinpath('src', 'audios', 'btn.mp3').as_posix()
BEGIN = ROOT.joinpath('src', 'audios', 'begin.wav').as_posix()
INITIAL_MESSAGE = '''
---------- WELCOME ----------
Type "R" to record your keyboard and mouse.
Type "P" to play your already saved record.
'''

def play_effect(path: str):
    type_file = path.split('.')[-1]
    effect = None
    if type_file == 'mp3':
        effect = AudioSegment.from_mp3(path)
    else:
        effect = AudioSegment.from_wav(path)
    playback.play(effect)

def prepare_start():
    play_effect(BIP)
    sleep(1)
    play_effect(BIP)
    sleep(1)
    play_effect(BIP)
    sleep(1)
    play_effect(BEGIN)
    sleep(1)

def main():
    print(INITIAL_MESSAGE)
    res = input('-> ').lower()
    prepare_start()

if __name__ == "__main__":
    main()