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

def infobloxAdd():
    x = object_manager.InfobloxManager()
    while True:
        primary_input = input("[Primary Input]> ")
        if primary_input == "":
            raise sys.exit()
        elif validators.ipv4(primary_input):
            # A record
            secondary_input = input("[Record Name]> ")
            for network in umd_ips:
                if primary_input.startswith(network):
                    # search and display existing/add corresponding PTR
                    x.delete_ptr_record(ip=primary_input)
                    x.create_ptr_record(ip=primary_input,
                                        name=secondary_input)
            x.create_record(primary=primary_input,
                              secondary=secondary_input,
                              primary_type="ipv4addr",
                              secondary_type="name",
                              wapi_id="record:a")
        else:
            secondary_input = input("[Secondary Input]> ")
            y = re.search(r"\.([a-z])+$", secondary_input)
            if y:
                # should be CNAME record as it ends with ".xyz"
                x.create_record(primary=primary_input,
                                secondary=secondary_input,
                                primary_type="name",
                                secondary_type="canonical",
                                wapi_id="record:cname")
            else:
                # should be TXT record
                x.create_record(primary=primary_input,
                                secondary=secondary_input,
                                primary_type="name",
                                secondary_type="text",
                                wapi_id="record:txt")
        print("DONE")

requests.packages.urllib3.disable_warnings()
# supress irrelevant messages to enduser

infobloxAdd()

