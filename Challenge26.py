#!/usr/bin/env python3

# Script:                        Ops 401 Challenge 26
# Author:                        Jose Cardozo
# Date of latest revision:       02/20/2023
# Purpose:                       Ops Challenge: Event Logging Tool Part 1 of 3

import logging
import os
import time
from datetime import datetime
import smtplib
from decouple import config

# I AM APPLYING CHALLENGE 26 INTO CHALLENGE 2!!!

def send_email():
    today = datetime.today()
    if current_ping == 0:
        message1 = "Your host is responding", str(today)
    else:
        message1 = "Your host is not responding", str(today)
    # Sending the mail
    email.sendmail(username, username, message1)

# Create and configure the logger
logging.basicConfig(filename="test.log", filemode='w')

# Create an object
logger = logging.getLogger()

# Set the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

# Test messages - These get worse as you go down the list
logger.debug("Harmless debug message")
logger.info("Just informantion")
logger.warning("This is a warning")
logger.error("This is an error")
logger.critical("This is critical")

        
email = smtplib.SMTP('smtp.gmail.com', 587)

email.starttls()
username = config("username", default='')
password = config("password", default='')
email.login(username, password)

current_ping = os.system("ping -c1 127.0.0.1")

while True:
    last_ping = current_ping
    logger.debug("System attempting to ping.")
    current_ping = os.system("ping -c1 127.0.0.1")
    time.sleep(2)
    today = datetime.today()
    print(today)

    if current_ping == 0:
        logger.info("This is an information that your ping was successful")
        print(str(today) + " This ping was successful to: 127.0.0.1")
    else:
        logger.error("This is an error, the ping did not go through.")
        print(str(today) +" This ping to: 127.0.0.1 was a failure!")
    if current_ping != last_ping:
        send_email()
        if current_ping != 0:
            logger.critical("The host is no longer reachable")