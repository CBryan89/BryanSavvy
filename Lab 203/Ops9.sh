#!/bin/bash

user=y

while [ $user = y ]
do
echo "Pick a number to do one of the following."
echo Enter 1 for a special note.
echo Enter 2 to ping youself.
echo Enter 3 to show your network configuration.

read input

sleep 2

if [ $input = 1 ]
    then echo "Hello World."
elif [ $input = 2 ]
    then ping -c 3 192.168.12.207
elif [ $input = 3 ]
    then ifconfig
else
    echo "Invalid Entry."

fi 

echo "Do you want to choose another option? y/n?"
read user
done