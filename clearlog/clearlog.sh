#/bin/bash
#Script Name: clearlog.sh
#Author: Gina Hobbs
#Date of last revision: 08 March 2022
#Description of purpose: Clear log files
#Declaration of variables:
#Declaration of functions (if used):
#Main

cat /var/log/syslog
cat /var/log/wtmp

cat /dev/null > /var/log/syslog
cat /dev/null > /var/log/wtmp

cat /var/log/syslog
cat /var/log/wtmp

#End