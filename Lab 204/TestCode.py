# Your challenge tonight is to write a basic adventure game using some of the  
#code provide below and using if/elif statments
import time

yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]
 
# Introduction
name = input("What is your name, adventurer?\n")
print("Greetings, " + name + ". Let us go on a quest!")
print("You find yourself on the edge of a dark forest.")
print("Can you find your way through?\n")
 
# Start of game
response = ""
while response not in yes_no:
    response = input("Would you like to step into the forest?\nyes/no\n")
    if response == "yes":
        print("You head into the forest. You hear crows cawwing in the distance.\n")
    elif response == "no":
        print("You are not ready for this quest. Goodbye, " + name + ".")
        quit()
    else: 
        print("I didn't understand that.\n")
 
print("There is something smelly up ahead by the crows")
time.sleep(1)
print("To the left is Sharknadoes")
time.sleep(1)
print("To the right is lava\n")
time.sleep(1)
while True:
    response = input("what direction will you go?\nleft/right\n")
    # Start you Code below this line use and if/elif statment to take you an adventure in all directions
    if response == "left":
        print("The sharks and the tornadoes are overwhelming!")
        ride = input("Do you ride a shark y/n\n")
        if  ride == "y":
            print("The shark has flown you to saftey and has befriended your family.")
        else: print("The Shark smacks your face with his tail and you die!")
        
    elif response == "right":
        print("You get closer to the lava and notice two ways to get across.\n")
        print("To the left is a rickety old bridge, to the right is a childs swingset...")
        lava = input("Do you go left or right?\n")
        if lava == "left":
            print("The bridge breaks and you fall into the lava and die.")
        
        else: print("The child swing was inadequate for velocity and you die.\n")
        
    else:
        print("I didn't understand that.\n")
        #Write you code above this line
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
    