#/bin/bash
#Script Name: datetime.sh
#Author: Gina Hobbs
#Date of last revision: 08 March 2022
#Description of purpose: 
#Declaration of variables: 
#Declaration of functions (if used):
#Main

cp -R /var/log/syslog ./syslog_`date +%d%b%Y`

#End