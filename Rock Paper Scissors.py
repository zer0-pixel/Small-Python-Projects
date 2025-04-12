'''
Name: Thomas Johnson, Linh Dong
Date: 2/3/2025
Project: Rock, Paper, Scissors game is programmed to play
'''
import random

# Player gets to choose which hand to input or back out of the game to the main menu
def weapons_Menu():
  p_options = ['R', 'P', 'S', 'B']
  player = input("Press"
            "\n 'R' to play Rock,"
            "\n 'P' to play Paper,"
            "\n 'S' to play Scissors" 
            "\n 'B' to go back to the main menu"
            "\n Player: ").upper()
  if player in p_options:
    print("Rock, Paper, Scissors, Shoot!")
    if player == 'R':
      print("Player: Rock!")

    elif player == 'P':
      print("You: Paper!")

    elif player == 'S':
      print("You: Scissors")

    elif player == 'B':
      return 'B'
    return player

  else:
    print("Invalid Input! Choose R, P, S, or, B")
    return weapons_Menu()

# Computers choices gets randomized and displayed against the player
def com_Weapon():
  com_options = ['Rock!', 'Paper!', 'Scissors!']
  com = random.choice(com_options)
  print("COM: " + com)
  return com

# R, P, S logic is used to determine the winner of R, P, S
def find_Winner(player, com):
  win_Options = {"win_1": "~Paper beats Rock~",
                 "win_2": "~Rock beats Scissors~",
                 "win_3": "~Scissors beats Paper~"}
  wins = {"p_W": "Player Wins! +1 Points",
          "c_W": "COM Wins +1 Points"}
  if (player == 'R' and com == 'Paper!'):
    print(win_Options["win_1"] + "\n" + wins["c_W"])
    return 'C'
  elif (player == 'S' and com == 'Rock!'):
    print(win_Options["win_2"] + "\n" + wins["c_W"])
    return 'C'
  elif (player == 'P' and com == 'Scissors!'):
    print(win_Options["win_3"] + "\n" + wins["c_W"])
    return 'C'
  elif (player == 'P' and com == 'Rock!'):
    print(win_Options["win_1"] + "\n" + wins["p_W"])
    return 'P'
  elif (player == 'R' and com == 'Scissors!'):
    print(win_Options["win_2"] + "\n" + wins["p_W"])
    return 'P'
  elif (player == 'S' and com == 'Paper!'):
    print(win_Options["win_3"] + "\n" + wins["p_W"])
    return 'P'
  else:
    print("Its a tie!")
    print("No Winners!")
    return 'T'

# Displays the Players and Computers score when inputting '2' at the main menu
def display_Scores(player_score, com_score):
  print("Player Score: " + str(player_score))
  print("COM Score: " + str(com_score))

# Rock, Paper, Scissors menu that the player will navigate to play the game, show scores, or quit
def main_Menu():
# Players and Computers score starts at 0
  player_score = 0
  com_score = 0

# Loops the main menu
  while True:
    print(" *****************************\n "
          "Rock, Paper, Scissors! | Menu\n "
          "*****************************")
    print("Press:")
    print("1 - Play Game")
    print("2 - Show Scores")
    print("3 - Quit")

# Players navigate the main menu
    try:
      val = int(input("Press '1' to Play \n"))
    except ValueError:
      print("Invalid input! Choose number 1-3")
      continue

    if val == 1:
      print("*******\nPlaying\n*******")
      while True:
        player = weapons_Menu()
        if player == 'B':
          break
        com = com_Weapon()
# Adds a point to the winners score, unless its a tie - no points.
        result = find_Winner(player, com)
        if (result == 'P'):
          player_score += 1
          print("---------------")
          print("Player Score: " + str(player_score))
          print("COM Score: " + str(com_score))
          print("---------------")
        elif (result == 'C'):
          com_score += 1
          print("---------------")
          print("Player Score: " + str(player_score))
          print("COM Score: " + str(com_score))
          print("---------------")
        else:
          player_score += 0
          com_score += 0
          print("---------------")
          print("Player Score: " + str(player_score))
          print("COM Score: " + str(com_score))
          print("---------------")
    elif val == 2:
      print("Showing scores")
      display_Scores(player_score, com_score)
    elif val == 3:
      print("Final Scores:")
      print("Player Score: " + str(player_score))
      print("COM Score: " + str(com_score))
      break
    else:
      print("Invalid input! Choose numbers 1-3")


main_Menu()