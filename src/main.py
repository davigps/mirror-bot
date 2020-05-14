from time import sleep
from pathlib import Path
from pydub import AudioSegment, playback
from threading import Thread

from controllers.keyboard import KeyboardController
from controllers.mouse import MouseController
from recorders.keyboard import KeyboardRecorder
from recorders.mouse import MouseRecorder


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
    print('STARTED!')

def main():
    print(INITIAL_MESSAGE)
    res = input('-> ').lower()

    if res == 'r':
        name = input("Record's name: ")
        prepare_start()

        try:
            record_k = open(ROOT.joinpath('src', 'mimics', f'{name}.kmimic'), 'a')
            record_m = open(ROOT.joinpath('src', 'mimics', f'{name}.mmimic'), 'a')
        except:
            print("Cannot create record's files.")
            raise
        
        k_recorder = KeyboardRecorder(record_k)
        k_thread = Thread(target=k_recorder.start)

        m_recorder = MouseRecorder(record_m, k_thread.is_alive)
        m_thread = Thread(target=m_recorder.start)

        k_thread.start()
        m_thread.start()

    elif res == 'p':
        name = input("Record's name: ")
        prepare_start()

        try:
            record_k = open(ROOT.joinpath('src', 'mimics', f'{name}.kmimic'), 'r')
            record_m = open(ROOT.joinpath('src', 'mimics', f'{name}.mmimic'), 'r')
        except:
            print("Cannot open record's files.")
            raise 
        
        k_controller = KeyboardController(record_k)
        m_controller = MouseController(record_m)

        Thread(target=k_controller.start).start()
        Thread(target=m_controller.start).start()

    else: quit()

if __name__ == "__main__":
    main()