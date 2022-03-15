#!/usr/bin/env python3
#Script Name: file.py
#Author: Gina Hobbs
#Date of last revision: 15 March 2022
#Description of purpose: Create and remove a file in a directory
#Declaration of variables: file
#Declaration of functions (if used): 
#Main

import os

# Create a file if one doesn't exist
file = open("text.txt","w")
file.close()

# Open file for appending lines 
file = open("text.txt","a")

# Append lines
lines = ["line 1 \n","line 2 \n", "line 3 \n"]
file.writelines(lines)
file.close()

# Print file line 1
file = open("text.txt","r")
print(file.read(6))

# Remove text.txt
os.remove("text.txt")

#End