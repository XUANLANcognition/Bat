#!/usr/bin/env python
# -*- coning : utf-8 -*-

' help '

from scapy.all import *

from bat.report import report
from bat.core.scan import scan

class SynScanner(scan.Scanner):

    def p1(self):
        print("Please wait...")
        ans, unans = sr(IP(dst=self.dnetwork)/TCP(dport=(1, 1000), flags='S'), timeout=3, verbose=0)
        print("Bat report for " + self.dnetwork + '\n')
        print(str(len(ans[ICMP])) +  " flitered ports")
        print("port\t\tstatus")
        ans.summary( lfilter =  lambda r: r[1].sprintf("%TCP.flags%") == 'SA', prn = lambda r: r[1].sprintf("%TCP.sport%\topen"))
        ans.summary( lfilter =  lambda r: r[1].sprintf("%TCP.flags%") == 'RA', prn = lambda r: r[1].sprintf("%TCP.sport%\tclose"))

    def p2(self):
        ans, unans = sr(IP(dst=self.dnetwork)/TCP(dport=int(self.dport), flags='S'), timeout=5, verbose=0)
        ans.show()

    def p3(self):
        print("p3")

if __name__ == '__main__':
    scanner = SynScanner(argv)
