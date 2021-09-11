#!/usr/bin/python3
print("Use Sudo")
#Packet sniffer script using scapy
from datetime import datetime 
import sys
import subprocess #Create another processs
from scapy.all import *

#net_iface = input("Enter interface name: ")
net_iface = sys.argv[1]

#promisceous mode transfer the interface data packets to cpu to processs and you capture from there
subprocess.call(["ifconfig",net_iface,"promisc"]) #creating another process to run command

#num_of_pkt = int(input("Enter the packet count you want to capture"))
num_of_pkt =int(sys.argv[2])

#time_sec =int(input("Enter the time how long(in sec) run to capture"))
time_sec =int(sys.argv[3])

#proto = input("Enter the protocol(arp | icmp |all)")
proto=sys.argv[4]

#sniff function call it and pass every packet in byte format
def logs(packet):
	print(f"SRC_MAC: {str(packet[0].src)} DEST_MAC: {str(packet[0].dst)}")


if proto == "all":
	sniff(iface = net_iface ,count = num_of_pkt, timeout = time_sec, prn=logs ) #sniffing packet
elif proto == "arp" or proto == "icmp":
	sniff(iface = net_iface, count = num_of_pkt,timout = time_sec , prn = logs , filter = proto) #sniffing packet
else:
	print("Wrong protocol")

