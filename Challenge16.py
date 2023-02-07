#!/usr/bin/env python3

# Script:                        Ops 401 Challenge 16
# Author:                        Jose Cardozo
# Date of latest revision:       02/06/2023
# Purpose:                       Automated Brute Force Wordlist Attack Tool Part 1 of 3

import time, getpass

# Offensive
def iterator():
    path=input("Enter dictionary file path:\n")
    doc=open(path)
    contents=doc.readline()
    print()

    # Loop
    while contents:
        print(contents.rstrip())
        contents=doc.readline()
        time.sleep(1)

iterator()

# Defensive
def defender():
    string=getpass.getpass("Enter a password to query:\n")
    path=input("Enter dictionary file path:\n")
    doc=open(path)
    contents=doc.readline()
    answer=False 

    # Loop
    while contents:
        contents.rstrip()
        contents=doc.readline()

        if contents.rstrip == string:
            answer=True
            break

if answer:
    print("File contained entered string")

else:
    print("File did not contained the entered string")

defender()
