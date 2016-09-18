# splunk_alert_bmcpatrol
Splunk modular alert to BMC Patrol

Splunk modular alert to BMC Patrol will send alerts leveraging the msend command. 
#https://docs.bmc.com/docs/display/public/btsim96/mposter+and+msend+syntax
The msend binary would be required on the splunk server running the alert action. 

TO DO:

SAMPLE ALERTS
-will use DMC alerts as the intial test alert searches

SCRIPTED ALERT ACTION
-design and complete python scipt to parse json payload from splunk and trigger msend

UI
-complete setup.xml to allow setting of the msend destination address & port
-complete alert action user inputs



