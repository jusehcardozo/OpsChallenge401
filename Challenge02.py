#!/usr/bin/env python3

# Script: Ops 401 Challenge 02
# Author: Jose Cardozo
# Date of latest version:  01/18/2023
# Purpose: Uptime Sensor Tool Part 2 of 2

# Transmit a single ICMP (ping) packet to a specific IP every two seconds.
# Evaluate the response as either success or failure.
# Assign success or failure to a status variable.
# For every ICMP transmission attempted, print the status variable along with a comprehensive timestamp and destination IP tested.
# Example output: 2020-10-05 17:57:57.510261 Network Active to 8.8.8.8

# Ask the user for an email address and password to use for sending notifications.
# Send an email to the administrator if a host status changes (from “up” to “down” or “down” to “up”).
# Clearly indicate in the message which host status changed, the status before and after, and a timestamp of the event.

import os
import time
from datetime import datetime
import smtplib
from decouple import config

def send_email():
    today = datetime.today()
    if current_ping == 0:
        message1 = "Your host is responding", str(today)
    else:
        message1 = "Your host is not responding", str(today)
    # Sending the mail
    email.sendmail(username, username, message1)
        
email = smtplib.SMTP('smtp.gmail.com', 587)

email.starttls()
username = config("username", default='')
password = config("password", default='')
email.login(username, password)

current_ping = os.system("ping -c1 127.0.0.1")

while True:
    last_ping = current_ping
    current_ping = os.system("ping -c1 127.0.0.1")
    time.sleep(2)
    today = datetime.today()
    print(today)

    if current_ping == 0:
        print(str(today) + " This ping was successful to: 127.0.0.1")
    else:
        print(str(today) +" This ping to: 127.0.0.1 was a failure!")
    if current_ping != last_ping:
        send_email()
