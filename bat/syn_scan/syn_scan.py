#!/usr/bin/env python
# -*- coning : utf-8 -*-

' help '

from scapy.all import *

from bat.report import report
from bat.scan import scan

class SynScanner(scan.Scanner):

    def p1(self):
        print("Please wait...")
        ans, unans = sr(IP(dst=self.dnetwork)/TCP(dport=(1, 100), flags='S'), timeout=5, verbose=0)
        print("port\tstatus")
        print("********************")
        ans.summary( lfilter =  lambda r: r[1].sprintf("%TCP.flags%") == 'SA', prn = lambda r: r[1].sprintf("%TCP.sport%\topen"))

    def p2(self):
        ans, unans = sr(IP(dst=self.dnetwork)/TCP(dport=int(self.dport), flags='S'), timeout=5, verbose=0)
        ans.show()

    def p3(self):
        print("p3")

if __name__ == '__main__':
    scanner = SynScanner(argv)
