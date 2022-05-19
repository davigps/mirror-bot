from threading import Thread

from controllers.main import Controller
from interpreters.main import Interpreter
from recorders.keyboard import KeyboardRecorder
from recorders.mouse import MouseRecorder
from utils import ROOT, prepare_start

INITIAL_MESSAGE = """
---------- WELCOME ----------
Type "R" to record your keyboard and mouse.
Type "P" to play your already saved record.
"""


def recordMirror():
    """Get the name of a file and record it."""
    name = input("Record's name: ")

    try:
        record = open(ROOT.joinpath("src", "mirrors", f"{name}.mirror"), "a")
        delay_information = [None]

        k_recorder = KeyboardRecorder(record, delay_information)
        k_thread = Thread(target=k_recorder.start)

        m_recorder = MouseRecorder(record, delay_information, k_thread.is_alive)
        m_thread = Thread(target=m_recorder.start)

        prepare_start()
        k_thread.start()
        m_thread.start()
    except:
        print("---! Cannot create record file.")


def playMirror():
    """Get the name of a file and play it."""
    name = input("Record's name: ")

    try:
        record = open(ROOT.joinpath("src", "mirrors", f"{name}.mirror"), "r")

        stream = Interpreter(record).get_stream()

        prepare_start()
        Controller(stream).start()
    except:
        print("---! Cannot open record file.")


def main():
    """Main Menu Function to play and record with the BOT."""
    print(INITIAL_MESSAGE)
    res = input("-> ").lower()

    if res == "r":
        recordMirror()
    elif res == "p":
        playMirror()
    else:
        quit()


if __name__ == "__main__":
    main()
