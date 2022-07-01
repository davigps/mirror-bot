from threading import Thread

from mirror_bot.controllers.main import Controller
from mirror_bot.interpreters.main import Interpreter
from mirror_bot.recorders.keyboard import KeyboardRecorder
from mirror_bot.recorders.mouse import MouseRecorder
from mirror_bot.utils import get_mirror_path


class MirrorBot:
    @classmethod
    def list_mirrors() -> list[str]:
        return ['bomdia']

    @classmethod
    def record_mirror(cls, mirror_name: str):
        record = open(get_mirror_path(mirror_name), "a")
        delay_information = [None]

        k_recorder = KeyboardRecorder(record, delay_information)
        k_thread = Thread(target=k_recorder.start)

        m_recorder = MouseRecorder(record, delay_information, k_thread.is_alive)
        m_thread = Thread(target=m_recorder.start)

        k_thread.start()
        m_thread.start()

    @classmethod
    def play_mirror(cls, mirror_name: str):
        record = open(get_mirror_path(mirror_name), "r")

        stream = Interpreter(record).get_stream()

        Controller(stream).start()
