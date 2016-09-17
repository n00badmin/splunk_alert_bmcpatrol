#!/usr/bin/python
# -*- coding: utf-8 -*-

#Splunk Custom Alert Action for BMC Patrol
#Send dynamic alerts via the MSEND command
#https://docs.bmc.com/docs/display/public/btsim96/mposter+and+msend+syntax

import sys
import re
import subprocess
import json
import csv
import gzip
from collections import OrderedDict

#Check args
if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] != "--execute":
         print >> sys.stderr, "FATAL Unsupported execution mode (expected --execute flag)"
         sys.exit(1) 
    
    try:
        settings = json.loads(sys.stdin.read())
        body = OrderedDict(
            sid=settings.get('sid'),
            search_name=settings.get('search_name'),
            app=settings.get('app'),
            owner=settings.get('owner'),
            results_link=settings.get('results_link'),
            result=settings.get('result')
        )

#use contents of body to dynamically populate, then execute the MSEND CLI command

#msend -n @msend.host.com:1830#mc -a EVENT –r CRITICAL -m “Message passed by user in gui” -b "mc_host=$host; mc_tool_class=SPLUNK-ENTERPRISE; mc_object=$source; mc_object_owner=$team; mc_tool=$SearchName; mc_tool_uri=$UriOfSplunkReportIfAvailableORRESULTS"
 
 
#-a Class                                 Sends an object of class Class
#-r Severity                           Sets the event severity value to the Severity specified
#-b SlotSetValue Adds SlotSetValue settings (format: "slot=value;...")
#-m Message                       Sets event message to the specified Message text
 
