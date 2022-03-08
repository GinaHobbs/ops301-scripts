#/bin/bash
#Script Name: chmod.sh
#Author: Gina Hobbs
#Date of last revision: 08 March 2022
#Description of purpose: To change the permissions for a file
#Declaration of variables: file_input, chmod_input
#Declaration of functions (if used):
#Main

echo 'Please enter the path to the file you wih to change permissions to:'
read file_input

echo 'Please enter the 3 digit number of the permissions you wish to change:'
read chmod_input

cd $file_input
chmod -R $chmod_input ./

echo ./

#End