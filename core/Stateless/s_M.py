from scapy.all import *
import netaddr

ip = '192.168.16.0/24'
port = [80, 8080]

IPList = [str(i) for i in netaddr.IPSet(netaddr.IPNetwork(ip))]

for i in IPList:
    for j in port:
        send(IP(dst = i)/TCP(dport = j, flags = 2), verbose = False)
        print(str(i) + ' : ' + str(j))
