#!/usr/bin/env python3

# Script: Ops 401 Challenge 07
# Author: Jose Cardozo
# Date of latest version:  01/25/2023
# Purpose: File Encryption Script Part 3 of 3

# Libraries

import ipaddress
from scapy.all import ICMP, IP, sr1, TCP
import sys
import os
from socket import *
import time

# User menu prompting choice between TCP Port Range Scanner mode and ICMP Ping Sweep mode, with the former leading to yesterday’s feature set
def ask_user():
    mode = input("\nWhat would you like to do? \n1 - TCP Port Range Scanner mode \n2 - ICMP Ping Sweep mode")

    if (mode == "1"):
        print()
    elif (mode == "2"):
        print()
    else:
        print("Wrong Choice! Choose again.")
ask_user()

#  ICMP Ping Sweep tool
IP = input("[+] Enter the Host IP Address:\t")
print("[+] Starting Ping Sweeper on " + IP)
dot = IP.rfind(".")
IP = IP[0:dot + 1]
    
for i in range(1, 255):
     host = IP + str(i)
     response = os.system("ping -c 1 -w 1 " + host + " >/dev/null")

     if response == 0:
        print(host + " is up")
else:
        print(host + " is down")


startTime = time.time()

if __name__ == '__main__':
   target = input('Enter the host to be scanned: ')
   t_IP = gethostbyname(target)
   print ('Starting scan on host: ', t_IP)
   
   for i in range(50, 500):
      s = socket(AF_INET, SOCK_STREAM)
      
      conn = s.connect_ex((t_IP, i))
      if(conn == 0) :
         print ('Port %d: OPEN' % (i,))
      s.close()
print('Time taken:', time.time() - startTime)

# Prompt user for network address including CIDR block, for example “10.10.0.0/24”
# Careful not to populate the host bits!

# Create a list of all addresses in the given network
# Ping all addresses on the given network except for network address and broadcast address
# If no response, inform the user that the host is down or unresponsive.
# If ICMP type is 3 and ICMP code is either 1, 2, 3, 9, 10, or 13 then inform the user that the host is actively blocking ICMP traffic.
# Otherwise, inform the user that the host is responding.
# Count how many hosts are online and inform the user.



# Define the end host and IP

network = "10.0.2.0/24"
ip_list = ipaddress.ip_network(network)
host_count = 0

for host in ip_list:
    print("Pinging", host )