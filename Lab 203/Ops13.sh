#!/bin/bash

echo "Enter a number." 
read number

if (( number >= 2 && number <= 5 )); then
    echo "Valid Number."
    echo "Your number is $number."
else 
    echo "Not Valid."
fi