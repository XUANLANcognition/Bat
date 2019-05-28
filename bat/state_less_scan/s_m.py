#!/usr/bin/env python
# -*- coning : utf-8 -*-

' help '

from scapy.all import *
import netaddr

ip = '10.10.10.0/24'
port = [8000]
iface = 'eth0'

def sM(IPList):
    for i in IPList:
        for j in port:
            send(IP(dst=i)/TCP(dport=j, flags='S'), verbose=0)
            print(str(i) + ' : ' + str(j))

def main():
    IPList = [str(i) for i in netaddr.IPSet(netaddr.IPNetwork(ip))]
    IPDict = {str(i): None for i in IPList}
    sM(IPList)

if __name__ == '__main__':
    main()
