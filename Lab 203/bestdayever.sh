#!/bin/bash

name=$1
complimnet=$2

user=$(whoami)
date=$(date)
whereami=$(pwd)

echo "Good morning $name."
sleep 1
echo "You have the best $compliment."
sleep 1
echo "You are currently logged in at $user on $whereami. Today is $date."

