#/bin/python3
#Script Name: hardware.py
#Author: Gina Hobbs
#Date of last revision: 08 March 2022
#Description of purpose: to grab hardware config
#Declaration of variables: 
#Declaration of functions (if used):
#Main

import os

os.system('whoami')

os.system('ip a')

os.system('lshw -short')

#End