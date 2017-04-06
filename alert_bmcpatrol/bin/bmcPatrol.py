#!/usr/bin/python
# -*- coding: utf-8 -*-
 
 
#Splunk Custom Alert Action for BMC Patrol
#Send dynamic alerts via the MSEND command
#https://docs.bmc.com/docs/display/public/btsim96/mposter+and+msend+syntax
#Jeff Weiderman cleaned up Matthew Modestino's crappy code 09.2016
#Shoutout to Sean Mullen for pushing it over the goal line! 01.2017
#https://github.com/n00badmin/splunk_alert_bmcpatrol
 
import sys
import re
import subprocess
import json
import csv
import gzip
 
#Check args
def main():
    
    #get json ouptut from splunk modular alert - See alert_actions.conf.spec
    
    payload = json.loads(sys.stdin.read())
    config = payload.get('configuration', dict())
    #host = payload.get('host')
    host = ""
    splunkServer = payload.get('server_host')
    splunkURI = payload.get('server_uri')
    splunkApp = payload.get('app')
    splunkSearch = payload.get('search_name')
    resultsLink = payload.get('results_link')
    bmcPatrolTargetURI = config.get('targetURI')
    message = config.get('message')
    severity = config.get('severity')
    team = config.get('team')
    #outfile.write( json.dumps(payload))
    
    #use contents of body to dynamically populate, then execute the MSEND CLI command
    msendcmd = 'msend -n @{0}#mc -a EVENT -r "{1}" -m "{2}" -b "mc_host={3};mc_tool_class=SPLUNK-ENTERPRISE;mc_object=;mc_object_owner={4};mc_tool={5};mc_tool_uri={6}"'
    msendcmd = msendcmd.format(bmcPatrolTargetURI, severity, message, host, team, splunkSearch, resultsLink)
    
    #ps = open("/tmp/bmc.out","w")
    #ps.write("msendcmd = " + msendcmd + "\n")
 
    try:
        msend = subprocess.check_output(msendcmd, shell=True)
                                        sys.stdout.write(msend);
    except:
        sys.stderr.write('[bmcPatrol] failed to run MSEND command\n')
