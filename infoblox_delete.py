#! /usr/bin/env python3.6
import logging
import requests
import urllib3
import validators
import re
import sys
from infoblox_auto import object_manager

# below empty list should be a list of IP NETWORKS owned/managed by user
user_networks = ["1.1.", "1.2."]

# have user choose from options of which record they are manipulating
# set variable of record_type to either CNAME or ARecordBase etc.

def infobloxDelete():
    x = object_manager.InfobloxManager()
    while True:
        primary_input = input("[Primary Input]> ")
        if primary_input == "":
            raise sys.exit()
        else:
            x.pull_info(primary=primary_input)


requests.packages.urllib3.disable_warnings()
# supress irrelevant messages to enduser

infobloxDelete()

# 1. Ask user for primary ID should be one of the following:
#     A. ip address
#     B. canonical
#     C. domain name
# 2. Return query for associated info for ALL records tied to that primary ID
# 3. Display record type and pertinent information for each associated record
# 4. User picks number of record they want to delete
# 5. Confirm choice by displaying info
# 6. <ENTER> to confirm deletion
# 7. Deletion success message!