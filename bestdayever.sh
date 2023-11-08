#!/bin/bash

name=$1
compliment=$2

user=$(whoami)
date=(date)
whereami=$(pwd)


echo "Good morning $name."
sleep 1
echo "At least you woke up today, $name."
sleep 2
echo "You have the best $compliment I've ever seen $name!"
sleep 2
echo "You are currently logged in as $user at $date on $whereami."

