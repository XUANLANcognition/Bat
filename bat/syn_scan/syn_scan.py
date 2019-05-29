#!/usr/bin/env python
# -*- coning : utf-8 -*-

' help '

from scapy.all import *

from bat.report import report

def main(argv):
    dst = '127.0.0.1'
    dport = 80
    if len(argv) == 4:
        dst = argv[2]
        dport = int(argv[3])
    r = sr1(IP(dst=dst)/TCP(dport=dport, flags='S'), timeout=1)
    if r:
        re = report.Report('SYN', r.show(dump=True))
    else:
        re = report.Report('SYN', 'No response.')
    re.create()

if __name__ == '__main__':
    main()
