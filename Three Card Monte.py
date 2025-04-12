# Thomas
# Date: 1/28/2025
# User plays Three Card Monte
from operator import truediv

import check_input
import random
#Title of the game is presented
print("Three Card Monte")
print("Enter amount to bet")

def main():
    user = 100

    play = True
    #User gets prompted to input an amount to bet
    while play :
        start = check_input.get_int_range("Amount 1 - 100: ", 1, 100 )
        print("Playing...")
        print("...Shuffling Cards...")
        print("Guess Where The Queen is (choose numbers 1-3)")
        print("+-----+ +-----+ +-----+")
        print("|     | |     | |     |")
        print("|  1  | |  2  | |  3  |")
        print("|     | |     | |     |")
        print("+-----+ +-----+ +-----+")

        # User gets prompt to guess a card and the Queen card randomizes
        card = check_input.get_int_range("Your Guess: ", 1, 3)
        queen = random.randint(1, 3)
        print("Flipping Cards")
        if  queen == 1:
            print("+-----+ +-----+ +-----+")
            print("|     | |     | |     |")
            print("|  Q  | |  K  | |  K  |")
            print("|     | |     | |     |")
            print("+-----+ +-----+ +-----+")

        elif queen == 2:
            print("+-----+ +-----+ +-----+")
            print("|     | |     | |     |")
            print("|  K  | |  Q  | |  k  |")
            print("|     | |     | |     |")
            print("+-----+ +-----+ +-----+")

        else:
            print("+-----+ +-----+ +-----+")
            print("|     | |     | |     |")
            print("|  K  | |  K  | |  Q  |")
            print("|     | |     | |     |")
            print("+-----+ +-----+ +-----+")
        #User either win when they choose the same card as the queen
        #OR lose when they don't get the same card as the queen

        if queen == card:
            print("This Card...IS the Queen! YOU WIN!")
            print("The Queen was, " + str(queen))
            print("Your Amount: $" + str(user + start))
            user += start
        else:
            print("This Card...was NOT the Queen! YOU LOSE!")
            print("The Queen was, " + str(queen))
            print("Your Amount: $" + str(user - start))
            user -= start

        #If the user has $0 or less, the game automatically ends
        if user <= 0:
            print("...YOU ARE BROKE! GET OUTTA HERE!")
            print("...Ending...")
            play = False

        #User gets prompted to play or again or not
        else:
            val = False
            print("Would you like to play again?")
            val = check_input.get_yes_no("Press Y to play again / N to quit: ")
            if val == "Yes" or val == "Y":
                play = True
            #Problem: The 'no' doesn't render for some reason
            elif val == "No" or val == "N":
                print("ending...")
                play = False
                
main()