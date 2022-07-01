import argparse

import mirror_bot.cli.commands as commands

DESCRIPTION = '''
    This bot will record every button you press and when you release, on a file
    with type .mirror, then, to reproduce your mirror file, it just interpret and
    follow its statements.
    '''

class Bridge:
    commands_args = {
        'list': commands.list_mirrors,
        'play': commands.play_mirror,
        'record': commands.record_mirror,
        'delete': commands.delete_mirror
    }

    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(description=DESCRIPTION)

        self._create_args()
        self.args = self.parser.parse_args()

    def _create_args(self):
        self.parser.add_argument(
            '-l', '--list', action='store_true', help='list all saved mirrors'
        )
        self.parser.add_argument('-p', '--play', help='specify mirror to play')
        self.parser.add_argument('-r', '--record', help='specify mirror name to be recorded')
        self.parser.add_argument('-d', '--delete', help='specify mirror to be deleted')
    
    def process(self):
        for command, value in self.args.__dict__.items():
            if value:
                self.commands_args[command](value)
                return
        
        self.parser.print_help()
