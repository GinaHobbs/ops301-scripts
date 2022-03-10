#!/usr/bin/env python3
#Script Name: directory.py
#Author: Gina Hobbs
#Date of last revision: 10 March 2022
#Description of purpose: Print directroy contents
#Declaration of variables: file_path
#Declaration of functions (if used): walk()

# Import libraries

import os

# Declaration of variables

### Read user input here into a variable
file_path = input('Please enter a file path.')

# Declaration of functions

### Declare a function here
def walk(file_path):
    for (root, dirs, files) in os.walk(file_path):
        ### Add a print command here to print ==root==
        print(root)
        ### Add a print command here to print ==dirs==
        print(dirs)
        ### Add a print command here to print ==files==
        print(files)

# Main

### Pass the variable into the function here
walk(file_path)

# End