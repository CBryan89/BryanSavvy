#!/bin/bash

counter=0
until [ $counter -gt 10 ]
do
    echo "Count: $counter"
    sleep 1
    (( counter++ ))
done