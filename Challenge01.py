#!/usr/bin/env python3

# Script: Ops 401 Challenge 02
# Author: Jose Cardozo
# Date of latest version:  01/17/2023
# Purpose: Uptime Sensor Tool Part 1 of 2

# Transmit a single ICMP (ping) packet to a specific IP every two seconds.
# Evaluate the response as either success or failure.
# Assign success or failure to a status variable.
# For every ICMP transmission attempted, print the status variable along with a comprehensive timestamp and destination IP tested.
# Example output: 2020-10-05 17:57:57.510261 Network Active to 8.8.8.8

import os
import time
from datetime import datetime

while True:
    egg = os.system("ping -c1 127.0.0.1")
    print(os.system("ping -c1 127.0.0.1"))
    time.sleep(2)
    today = datetime.today()
    print(today)

    if egg == 0:
        print(str(today) + " This ping was successful to: 127.0.0.1")
    else:
        print(str(today) +" This ping to: 127.0.0.1 was a failure!")

# End.

    
    



