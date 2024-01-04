# Scenario
# A junior magician has picked a secret number. He has hidden it in a variable named secret_number.
#  He wants everyone who runs his program to play the Guess the secret number game,
#  and guess what number he has picked for them.
#  Those who don't guess the number will be stuck in an endless loop forever! Unfortunately, he does not know how to complete the code.
# Your task is to help the magician complete the code in the editor in such a way so that the code:
# will ask the user to enter an integer number;
# will use a while loop;
# will check whether the number entered by the user is the same as the number picked by the magician.
# If the number chosen by the user is different than the magician's secret number, the user should see
# the message "Ha ha! You're stuck in my loop!" and be prompted to enter a number again.
# If the number entered by the user matches the number picked by the magician, the number should be printed to the screen,
# and the magician should say the following words: "Well done, muggle! You are free now."
# The magician is counting on you! Don't disappoint him.
import random
def guess_number():
    print("I'm thinking of a magic number between 1 and 10.")
    number = random.randint(1, 10)
    tries = 0
    while tries < 100:
        guess = int(input("Enter your guess: "))
        if guess == number:
            print(f"{number} is correct! Well done muggle! You are free now.")
            return
        else:
            print("Ha ha! You're stuck in my loop! Enter your guess again!")
        tries += 0
guess_number()