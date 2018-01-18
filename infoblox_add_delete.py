#! /usr/bin/env python3.6
import logging
import requests
import urllib3
import validators
import re
from infoblox_auto import object_manager

umd_ips = ["x.x, y.y"]


# have user choose from options of which record they are manipulating
# set variable of record_type to either CNAME or ARecordBase etc.

def infobloxAdd():
    x = object_manager.InfobloxManager()
    while True:
        primary_input = input("[Primary Input]> ")
        if validators.ipv4(primary_input):
            # A record
            secondary_input = input("[Record Name]> ")
            for network in umd_ips:
                if primary_input.startswith(network):
                    # search and display existing/add corresponding PTR
                    x.delete_ptr_record(ip=primary_input)
                    x.create_ptr_record(ip=primary_input,
                                        name=secondary_input)
                    print("DONE")
                x.create_a_record(ip=primary_input,
                                  name=secondary_input)
        else:
            # CNAME/TXT record
            if primary_input.endswith(zone):
                # if user inputs a umd.edu url
                secondary_input = input("[Alias]> ")
                y = re.search(r"\.([a-z])+$", secondary_input)
                if y:
                    # should be CNAME record as it ends with ".xyz"
                    x.create_cname_record(name=primary_input,
                                          canonical=secondary_input)
                    print("DONE")
            else:
                # should be TXT record
                secondary_input = input("[Text]> ")
                x.create_txt_record(name=primary_input,
                                    text=secondary_input)
                print("DONE")

requests.packages.urllib3.disable_warnings() # supress irrelevant messages to enduser

infobloxAdd()

