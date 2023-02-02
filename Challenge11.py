#!/usr/bin/env python3

# Script:                        Ops 401 Challenge 11
# Author:                        Jose Cardozo
# Date of latest revision:       01/31/2023
# Purpose:                       Network Security Tool with Scapy Part 1 of 3 (Creating a network scanning tool)


# Import from Scapy library
from scapy.all import *
import random


# Define end host and TCP port range
host = "www.facebook.com"
portRange = [22,23,80,443,3389]

# Define port ranges on a specific set of ports to scan
# Test each port in the specified range using a for loop
# If flag 0x12 is received, send an rst packet to graciously close the open connection. notify the user the port is open
# If flag 0x14 is received, notify the user the port is closed
# If no flag received, notify the user the port is filtered and silently dropped 

for dstPort in portRange:
	srcPort = random.randint(1025,65534)
	resp = sr1(IP(dst=host)/TCP(sport=srcPort,dport=dstPort,flags="S"),timeout=1,verbose=0)
	if (str(type(resp)) == "<type 'NoneType'>"):
		print(host + ":" + str(dstPort) + " is filtered (silently dropped).")
	# elif(resp.haslayer(TCP)):
	
    if(resp.getlayer(TCP).flags == 0x12):
		send_rst = sr(IP(dst=host)/TCP(sport=srcPort,dport=dstPort,flags="R"),timeout=1,verbose=0)
		print(host + ":" + str(dstPort) + " is open.")
	elif (resp.getlayer(TCP).flags == 0x14):
		print(host + ":" + str(dstPort) + " is closed.")
	# elif(resp.haslayer(ICMP)):
	if(int(resp.getlayer(ICMP).type)==3 and int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
		print host + ":" + str(dstPort) + " is filtered (silently dropped)."

