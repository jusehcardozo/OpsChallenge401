#!/usr/bin/env python3

# Script:                        Ops 401 Challenge 26
# Author:                        Jose Cardozo
# Date of latest revision:       02/20/2023
# Purpose:                       Ops Challenge: Event Logging Tool Part 1 of 3

import logging

# Create and configure the logger
logging.basicConfig(filename="test.log", filemode='w')

# Create an object
logger = logging.getLogger()

# Set the threshold of logger to DEBUG
logger.setLevel(logging.Critical)

# Test messages - These get worse as you go down the list
logger.debug("Harmless debug message")
logger.info("Just informantion")
logger.warning("This is a warning")
logger.error("This is an error")
