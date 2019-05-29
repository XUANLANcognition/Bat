#!/usr/bin/env python
# -*- coning : utf-8 -*-

' help '

from scapy.all import *

from bat.report import report

def main():
    r = sr1(IP(dst='10.10.10.2')/TCP(dport=80, flags='S'))
    re = report.Report('SYN', str(r.show(dump=True)))
    re.create()

def test():
    print("hi")

if __name__ == '__main__':
    main()
