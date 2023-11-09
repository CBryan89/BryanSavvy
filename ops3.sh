echo -n "Enter Number: "
read VAR
echo Your number is $VAR
if [ $VAR -gt 5 ]
then
echo "'It's greater than 5."
elif [ $VAR -lt 5 ]
then
echo "It's less than 5."
else 
echo "It's exactly 5."
fi
echo Bye.
