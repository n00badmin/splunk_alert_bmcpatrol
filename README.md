# splunk_alert_bmcpatrol
Splunk modular alert to BMC Patrol

Splunk modular alert to BMC Patrol will send alerts leveraging the msend command. 

The msend binary would be required on the splunk server running the alert action. 

TO DO:

design the type of searches best used to pass to msend

design and complete python scipt to parse json payload from splunk and trigger msend

complete setup.xml to allow setting of the msend destination address 
