#!/usr/bin/env python3

# Script:                        Ops 401 Challenge 27
# Author:                        Jose Cardozo
# Date of latest revision:       02/21/2023
# Purpose:                       Ops Challenge: Event Logging Tool Part 2 of 3

import logging
import time

from logging.handlers import RotatingFileHandler

#----------------------------------------------------------------------
def create_rotating_log(path):
    """
    Creates a rotating log
    """
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)
    
    # add a rotating handler
    handler = RotatingFileHandler(path, maxBytes=20,
                                  backupCount=5)
    logger.addHandler(handler)
    
    for i in range(10):
        logger.info("This is test log line %s" % i)
        time.sleep(1.5)
        
#----------------------------------------------------------------------
if __name__ == "__main__":
    log_file = "test.log"
    create_rotating_log(log_file)



import logging
import time

from logging.handlers import TimedRotatingFileHandler

#----------------------------------------------------------------------
def create_timed_rotating_log(path):
    """"""
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)
    
    handler = TimedRotatingFileHandler(path,
                                       when="m",
                                       interval=1,
                                       backupCount=5)
    logger.addHandler(handler)
    
    for i in range(6):
        logger.info("This is a test!")
        time.sleep(75)

#----------------------------------------------------------------------
if __name__ == "__main__":
    log_file = "timed_test.log"
    create_timed_rotating_log(log_file)