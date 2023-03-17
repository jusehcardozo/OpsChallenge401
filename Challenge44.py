#!/usr/bin/env python3

# Script:                        Ops 401 Challenge 44
# Author:                        Jose Cardozo
# Date of latest revision:       03/16/2023
# Purpose:                       Ops Challenge: Create a Port Scanner


#!/usr/bin/python3

import socket

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = 5
sockmod.settimeout(timeout)

hostip = input("Provide the IP Address: ")
portno = int(input("Provide port number: "))

def portScanner(portno):
    if sockmod.connect_ex((hostip, portno)) == 1:
        print("Port closed")
    else:
        print("Port open")

portScanner(portno)