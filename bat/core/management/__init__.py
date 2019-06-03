import sys
import ipaddress

from netaddr import *

import bat.core.management.commands as commands

class ManagementUtility:
    """
    Encapsulate the logic of manage.py utilityes.
    """

    METHODS = ['syn', 'ack', 'fin']

    IPNetwork = None
    PORT = None

    def __init__(self, argv=None):
        self.argv = argv or sys.argv[:]

    def check_ip_valid(self):
        try:
            ipaddress.IPv4Network(self.IPNetwork)
            return True
        except ValueError:
            return False

    def execute(self):
        if self.argv[1] in self.METHODS:
            if self.argv[1] == 'syn':
                commands.syn_scan.go(self.argv[2:])
            elif self.argv[1] == 'ack':
                pass
        else:
            commands.syn_scan.go(self.argv[1:])


def execute_from_command_line(argv=None):
    utility = ManagementUtility(argv)
    utility.execute()
