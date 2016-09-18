#!/usr/bin/python
# -*- coding: utf-8 -*-

#Splunk Custom Alert Action for BMC Patrol
#Send dynamic alerts via the MSEND command
#https://docs.bmc.com/docs/display/public/btsim96/mposter+and+msend+syntax
#Matthew Modestino 09.2016
#Please feel free to leave it better than you found it, I know just enough to be dangerous!
#https://github.com/n00badmin/splunk_alert_bmcpatrol

import sys
import re
import subprocess
import json
import csv
import gzip


def bmcPatrol():
    try:
        #get json ouptut from splunk modular alert - See alert_actions.conf
        payload = json.loads(sys.stdin.read())
        config = payload.get('configuration', dict())
        host = payload.get('host') 
        splunkServer = payload.get('server_host')
        splunkURI = payload.get('server_uri')
        splunkApp = payload.get('app')
        splunkSearch = payload.get('search_name')
        resultsLink = payload.get('results_link')
        bmcPatrolTarget = config.get('serverip')
        port = str(config.get('port'))
        message = config.get('message')
        severity = config.get('severity')
        team = config.get('team')

#Thanks Manny! outfile.write( json.dumps(body))
#json,dumps({'a': "b", 'c': "d"}, indent=4) 
#sort_keys=true for adding more cpu usage to your script too

#use contents of body to dynamically populate, then execute the MSEND CLI command

#msend -n @bmcPatrolTarget:port#mc -a EVENT –r severity -m message -b "mc_host=host; mc_tool_class=SPLUNK-ENTERPRISE; mc_object=source; mc_object_owner=team; mc_tool=splunksearch; mc_tool_uri=splunkSearch"
 
 
#Check args
if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] != "--execute":
         print >> sys.stderr, "FATAL Unsupported execution mode (expected --execute flag)"
         sys.exit(1)
    bmcPatrol() 
