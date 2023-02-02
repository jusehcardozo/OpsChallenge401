#!/usr/bin/env python3

# Script:                        Ops 401 Challenge 13
# Author:                        Jose Cardozo
# Date of latest revision:       02/01/2023
# Purpose:                       Network Security Tool with Scapy Part 3 of 3 (Creating a network scanning tool)


# Import Libraries
import ipaddress
from scapy.all import ICMP, IP, sr1, TCP
import sys
import socket

# In Python, combine the two modes (port and ping) of your network scanner script.
def is_port_open(host, port):
    
   # determine whether `host` has the `port` open

    # creates a new socket
    s = socket.socket()
    try:
        # tries to connect to host using that port
        s.connect((host, port))
        
    except:
        # cannot connect, port is closed
        # return false
        return False
    else:


# In Python, combine the two modes (port and ping) of your network scanner script.
# Eliminate the choice of mode selection.
# Continue to prompt the user for an IP address to target.
# Move port scan to its own function.
# Call the port scan function if the host is responsive to ICMP echo requests.
# Print the output to the screen.