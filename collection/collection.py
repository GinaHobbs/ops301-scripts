#!/usr/bin/env python3
#Script Name: directory.py
#Author: Gina Hobbs
#Date of last revision: 10 March 2022
#Description of purpose: Print directroy contents
#Declaration of variables: collection
#Declaration of functions (if used): 
#Main

collection = ["One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten"]

print(collection[3])

for i in range(6, len(collection)):
        print(collection[i])

collection[7] = "onion"
print(collection[7])

#End