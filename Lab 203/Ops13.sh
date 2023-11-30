#!/bin/bash

read -p "Enter a number 2 through 5: " number1

if [ $number1 -gt 2 -a $number1 -lt 5];
then echo "Valid Number. Your number is $number1."