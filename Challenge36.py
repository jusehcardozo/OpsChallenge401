#!/usr/bin/env python3

# Script:                        Ops 401 Challenge 36
# Author:                        Jose Cardozo
# Date of latest revision:       03/06/2023
# Purpose:                       Ops Challenge: Web Application Fingerprinting Part 1 of 3


# We can use Netcat to perform banner grabbing from a Kali Linux box using nc IP PORT to see if there's a response. Here's this in action.

# kali@kali:~$ nc scanme.nmap.org 22
# SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13 ###BANNER
# Alternatively, we can use Telnet to perform similar banner grabbing with the syntax telnet IP PORT as depicted below.

# kali@kali:~$ telnet 10.0.2.24 22
# Trying 10.0.2.24...
# Connected to 10.0.2.24.
# Escape character is '^]'.
# SSH-2.0-OpenSSH_5.3p1 Debian-3ubuntu4  ###BANNER
# ^
# Protocol mismatch.
# Connection closed by foreign host.