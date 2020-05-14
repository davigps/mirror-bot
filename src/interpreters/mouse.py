from _io import TextIOWrapper
from typing import List
from interpreters.setence import Setence


class MouseInterpreter:
    def __init__(self, record: TextIOWrapper):
        self.record = record.read()
        self.setences: List[Setence] = []
        self.read_record()
    
    def read_record(self):
        for string in self.record.split(';'):
            if not string: continue
            setence = Setence(string, 'm')
            self.setences.append(setence)
    
    def get_stream(self) -> List[Setence]:
        return self.setences