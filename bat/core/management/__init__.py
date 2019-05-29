import sys

import bat.core.management.commands as commands

class ManagementUtility:
    """
    Encapsulate the logic of manage.py utilityes.
    """
    def __init__(self, argv=None):
        self.argv = argv or sys.argv[:]

    def execute(self):
        if self.argv[1] == 'syn':
            commands.syn_scan.go(self.argv)


def execute_from_command_line(argv=None):
    utility = ManagementUtility(argv)
    utility.execute()
