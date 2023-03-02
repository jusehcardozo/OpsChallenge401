#!/usr/bin/env python3

# Script:                        Ops 401 Challenge 33
# Author:                        Jose Cardozo
# Date of latest revision:       03/01/2023
# Purpose:                       Ops Challenge: Signature-based Malware Detection Part 3 of 3

import hashlib
import requests


# API Key for VirusTotal
API_KEY = 'API_KEY_VIRUSTOTAL YOU GET FROM THE WEBSITE'

# Function to calculate the MD5 hash of a file
def calculate_md5(filename):
    hash_md5 = hashlib.md5()
    with open(filename, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# Function to check if a file is malicious based on its MD5 hash using the VirusTotal API
def is_malicious(filename):
    file_signature = calculate_md5(filename)
    params = {'apikey': API_KEY, 'resource': file_signature}
    response = requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=params)
    if response.status_code == 200:
        json_response = response.json()
        if json_response['response_code'] == 1:
            positives = json_response['positives']
            if positives > 0:
                return True
    return False

# Example usage
filename = 'file.exe'
if is_malicious(filename):
    print(f'{filename} is malicious')
else:
    print(f'{filename} is clean')