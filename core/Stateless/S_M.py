#!/usr/bin/env python
# -*- coning : utf-8 -*-

' help '

from scapy.all import *
import netaddr

def sM(IPList):
    for i in IPList:
        for j in port:
            send(IP(dst = i)/TCP(dport = j, flags = 'S'), verbose = False)
            print(str(i) + ' : ' + str(j))

if __name__ == '__main__':
    ip = '192.168.16.0/24'
    port = [53, 80, 443]
    iface = 'eth0'

    IPList = [str(i) for i in netaddr.IPSet(netaddr.IPNetwork(ip))]
    IPDict = {str(i): None for i in IPList}
    sM(IPList)
