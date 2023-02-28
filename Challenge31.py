#!/usr/bin/env python3

# Script:                        Ops 401 Challenge 31
# Author:                        Jose Cardozo
# Date of latest revision:       02/27/2023
# Purpose:                       Ops Challenge: Signature-based Malware Detection Part 1 of 3


# Open Command Prompt. View manual to dir using:
dir /?

# Note that /B uses bare format, and /S recursively displays files and directories.

# Search a specific file in this directory using this syntax.
dir /b/s *.file_extension

# Example: dir /b/s *.png would search for all png files recursively

# Alternatively, we can search for a file by name
dir "\search term*" /s

# Example: dir *picture*.jpg /s

# We can search for folders recursively as well.
dir "Name of folder to search" /AD /b /s

# Example: dir Images /AD /b /s

# If you only know the partial name of the folder you're looking for, try:
dir /s/b /A:D "D:*partial-name-of-folder*"

# Example: dir /s/b /A:D "D:*Stea*" would help you find folders with the word "steam" in their names