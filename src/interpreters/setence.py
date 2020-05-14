class Setence:
    def __init__(self, string: str, mode: str):
        self.separator = '|&|' if mode == 'k' else '&'
        self.read_string(string)

    def read_string(self, string):
        parts = string.split(self.separator)
        self.pause: float = float(parts[0])
        self.action: str = parts[1]
        self.metadata: str = parts[2]
