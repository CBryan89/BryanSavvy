#!/bin/bash
#scipt ops 201 class Ops Challenge Solutions
#Nov 09 2023
#purpose: Understanding Functions
#Variables
Variables= $Num1
Variables= $Num2
Variables= $Sum
Variables= $Prod
Variables= $Divan
Variables= $Diff

function addition (){
    sum=$(($Num1 + $Num2))
}
function subtraction () {  
    Diff=$(($Num1 - $Num2))
}
function multiplication () {
    Prod=$(($Num1 * $Num2))
}
function division () {
        Divan=$(($Num1 / $Num2))
}
echo "Please enter your first number to add, subtract, multiply and divide."
read Num1
echo "Thank You."
sleep 2
echo "Please enter your second number to add, subtract, multiply and divide."
read Num2
echo "Thank You. Please wait..."
sleep 3
addition
echo "The sum of your numbers is $Sum."
sleep 2
subtraction
echo "The remainder of your numbers is $Diff."
sleep 2
multiplication
echo "The product of your two numbers is $Prod."
sleep 2
division
echo "The dividend of your numbers is $Divan."
sleep 2
echo "Have a nice day."