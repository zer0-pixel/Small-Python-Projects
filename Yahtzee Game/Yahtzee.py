'''
Author: Thomas Johnson, Linh Dong
Date: 3/6/2025
Project: Program allows user to play a Yahtzee(dice game)
'''

#Imports player file from player.py
import player


def take_turn():
    print("-Yahtzee-")
    #Creates a player object that stays till the player ends the game
    p1 = player.Player()

    while True:
        #Rolls players dice and displays results
        p1.roll_dice()
        print("Rolled dice: ", p1)

        #Checks for different conditions
        if p1.has_three_of_a_kind():
            print("You got 3 of a kind! +3 Points")

        elif p1.has_pair():
            print("You got a pair! +1 Points")

        elif p1.has_series():
            print("You got a series of 3! +2 Points")

        else:
            print("Yikes! Too Bad...")
        #Displays players points
        print("Total points: ", p1.points())

        #Asks the player to play again
        while True:
            play_again = input("Play Again? Y/N: ").strip().lower()
            if play_again in ["n","no"]:
                print("Thanks for Playing!")
                print("Final Points: ", p1.points())
                return
            elif play_again in ["y", "yes"]:
                break
            else:
                print("Invalid input. Please enter Y or N.")

take_turn()