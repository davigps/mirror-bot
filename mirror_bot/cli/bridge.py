import argparse

import mirror_bot.cli.commands as commands

DESCRIPTION = '''
    This bot will record every button you press and when you release, on a file
    with type .mirror, then, to reproduce your mirror file, it just interpret and
    follow its statements.
    '''

class Bridge:
    

    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(description=DESCRIPTION)

        self._create_args()

        args, unknown = self.parser.parse_known_args()
        self.args = args
        self.unknown = unknown
    
    def _create_args(self):
        self.parser.add_argument(
            '-l', '--list', action='store_true', help='list all saved mirrors'
        )
        self.parser.add_argument('-p', '--play', help='specify mirror to play')
        self.parser.add_argument('-r', '--record', help='specify mirror name to be recorded')
        self.parser.add_argument('-d', '--delete', help='specify mirror to be deleted')
    
    def process(self):
        if self.args.list:
            commands.list_mirrors()
            return
        
        if self.args.play:
            commands.play_mirror(self.args.play)
            return
        
        if self.args.record:
            commands.record_mirror(self.args.record)
            return
        
        if self.args.delete:
            commands.delete_mirror(self.args.delete)
            return
        
        self.parser.print_help()
