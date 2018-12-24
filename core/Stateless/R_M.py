#!/usr/bin/env python
# -*- coning : utf-8 -*-

' help '

from scapy.all import *
import netaddr

def prn(pkt):
    if pkt[IP].src in IPDict:
        if pkt[TCP].flags == 'SA':
            print(pkt[IP].src + ':' + str(pkt[TCP].sport) + ' Open')
        elif pkt[TCP].flags == 'RA':
            print(pkt[IP].src + ' Close')

def rM(iface, IPDict):
    userIP = get_if_addr(str(iface))
    f = 'tcp and dst %s'%userIP
    sniff(iface = iface, filter = f, prn = prn)
    

if __name__ == '__main__':
    ip = '192.168.16.0/24'
    port = [53, 80, 443]
    iface = 'eth0'

    IPList = [str(i) for i in netaddr.IPSet(netaddr.IPNetwork(ip))]
    IPDict = {str(i): None for i in IPList}
    rM(iface, IPDict)
