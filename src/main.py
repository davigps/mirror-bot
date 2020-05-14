from threading import Thread
from utils import ROOT, prepare_start

from recorders.keyboard import KeyboardRecorder
from recorders.mouse import MouseRecorder
from interpreters.keyboard import KeyboardInterpreter
from interpreters.mouse import MouseInterpreter
from controllers.keyboard import KeyboardController
from controllers.mouse import MouseController



INITIAL_MESSAGE = '''
---------- WELCOME ----------
Type "R" to record your keyboard and mouse.
Type "P" to play your already saved record.
'''

def main():
    print(INITIAL_MESSAGE)
    res = input('-> ').lower()

    if res == 'r':
        name = input("Record's name: ")

        try:
            record_k = open(ROOT.joinpath('src', 'mimics', f'{name}.kmimic'), 'a')
            record_m = open(ROOT.joinpath('src', 'mimics', f'{name}.mmimic'), 'a')
        except:
            print("---! Cannot create record's files.")
            raise

        k_recorder = KeyboardRecorder(record_k)
        k_thread = Thread(target=k_recorder.start)

        m_recorder = MouseRecorder(record_m, k_thread.is_alive)
        m_thread = Thread(target=m_recorder.start)

        prepare_start()
        k_thread.start()
        m_thread.start()

    elif res == 'p':
        name = input("Record's name: ")

        try:
            record_k = open(ROOT.joinpath('src', 'mimics', f'{name}.kmimic'), 'r')
            record_m = open(ROOT.joinpath('src', 'mimics', f'{name}.mmimic'), 'r')
        except:
            print("---! Cannot open record's files.")
            raise 
        
        k_stream = KeyboardInterpreter(record_k).get_stream()
        m_stream = MouseInterpreter(record_m).get_stream()

        prepare_start()
        Thread(
            target=KeyboardController(k_stream).start
            ).start()
        Thread(
            target=MouseController(m_stream).start
            ).start()

    else: quit()

if __name__ == "__main__":
    main()