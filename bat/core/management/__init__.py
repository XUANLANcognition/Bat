import sys
import ipaddress

from netaddr import *
from scapy.all import *

import bat.core.management.commands as commands

class ManagementUtility:
    """
    Encapsulate the logic of manage.py utilityes.
    """

    METHODS = ['syn', 'ack', 'fin']

    FUNC = ['-h', '-p', '-a', 'help']

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

    def port_scan(self):
        if self.argv[2] in self.METHODS:
            if self.argv[2] == 'syn':
                commands.syn_scan.go(self.argv[3:])
            elif self.argv[2] == 'ack':
                pass
        else:
            commands.syn_scan.go(self.argv[2:])

    def host_scan(self):
        ans, unans = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=self.argv[2]), timeout=2, verbose=0)
        ans.summary(lambda r: r[1].sprintf('%Ether.src% | %ARP.psrc% is up'))

    def script_attack(self):
        pass

    def help(self):
        print('HELP')

    def execute(self):
        if self.argv[1] in self.FUNC:
            if self.argv[1] == '-p':
                self.port_scan()
            elif self.argv[1] == '-h':
                self.host_scan()
            elif self.argv[1] == '-a':
                self.script_attack()
            else:
                self.help()
        else:
            self.help()


def execute_from_command_line(argv=None):
    utility = ManagementUtility(argv)
    utility.execute()
