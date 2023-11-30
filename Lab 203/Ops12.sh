#!/bin/bash

echo -n "How are you doing today?"
read response

echo -n "You are $response."

case $response in

    good)
    echo -n "I am glad for you."
    ;;

    bad)
    echo -n "I am sorry to hear that."
    ;;
    
    *)
    echo -n "I do not understand. Sorry."
esac

