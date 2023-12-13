# Objectives
# Create if statements using these logical conditionals below. Each statement should print information to the screen depending on if the condition is met.

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# Create an if statement using a logical conditional of your choice and include elif keyword that executes when other conditions are not met.
print("Enter two numbers.")
a = input ("Enter a number for a ")
b = input ("Enter a number for b ")

if (a == b) and (b == a):
    print ("a is equal to b")
elif (a < b) and (a <= b):
    print ("a is less than b")
else:
    print ("a is greater than b")
# Create an if statement that includes both elif and else to execute when both if and elif are not met.

# Stretch Goals (Optional Objectives)
# Pursue stretch goals if you are a more advanced user or have remaining lab time.

# Create an if statement with two conditions by using and between conditions.

# Create an if statement with two conditions by using or between conditions.

# Create a nested if statement.

x = 11
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20.")
    else:
        print("but not above 20.")
# Create an if statement that includes pass to avoid errors.

# if b > a:
#   pass
