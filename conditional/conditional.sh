#/bin/bash
#Script Name: conditional.sh
#Author: Gina Hobbs
#Date of last revision: 08 March 2022
#Description of purpose: To create a meny system that fulfills varioous options
#Declaration of variables: user_input
#Declaration of functions (if used):
#Main

while [ $user_input != 4 ]

echo 'Please select an option:'
echo '1: Print Hello World'
echo '2: Ping self'
echo '3: IP info'
echo '4: Exit'
read user_input

do
    case $user_input in

    1)
        echo 'Hello World'
        ;;

    2)
        ping -c1 `hostname` 
        ;;

    3)
        ifconfig
        ;;

    4) 
        ;;
    esac
done

#End