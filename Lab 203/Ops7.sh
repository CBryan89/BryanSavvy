#!/bin/bash

input="yes"
    echo "Enter the name of a file to change permissions:"
    ls
    read file

    if [ -e "$file" ]; then
        echo "Enter permission number 777 or 770."
        read Num
            chmod $Num "$file"
        echo "$file permissions have been changed."
        ls -l "$file"
    else
        echo "File not found: $file."
    fi
    echo "Would you like to change the permissions of another file? (yes or no)"
    read input
    
    echo "You typed $input."


