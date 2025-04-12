"""
Author: Thomas Johnson, Linh Dong
Date: 3/19/2025
Program: Mimic of Pokemon turn based battle. Allows user to battle with CPU Pokemon.
"""
import pokemon
from pokemon import Pokemon
from waterpoke import Water
from firepoke import Fire
from grasspoke import Grass
import random

def main():
    print("Pokemon Champions")
    print(f"~~Defeat all of your opponents pokemon~~")
    opponent = "Stew Pickles"
    # Opponent Object
    Opp_pokeball = [Fire(name="Flareon", poke_type="Fire"), Water(name="Blastoise", poke_type="Water"), Grass(name="Exeggutor", poke_type="Grass/Psychic")]
    # Player Object
    player_pokeball = [Fire("Charizard"), Water("Lapras"), Grass("Ivysaur")]

    while True:
        # Creates opponents and players pokemon list
        print(f"\n{opponent}(Opponent) Pokemon:")
        for i, pokemon in enumerate(Opp_pokeball, start=1):
            print(f"{i}. {pokemon}")

        print("\nYour Pokemon:")
        for i, pokemon in enumerate(player_pokeball, start=1):
            print(f"{i}. {pokemon}")
        p1 = int(input("Choose your Pokemon to battle with: "))

        # Checks players pokemon choices
        try:
            if 1 <= p1 <= len(player_pokeball):
                player_pokemon = player_pokeball[p1 - 1]
                print(f"\nYou: I CHOOSE YOU {player_pokemon._name}!")
            else:
                print("Invalid Input! Choose a valid Pokemon.")
                continue
        except ValueError:
            print("Invalid Input! Please Enter a number.")
            continue
        opp_pokemon = random.choice(Opp_pokeball)
        print(f"{opponent}:Lets GO {opp_pokemon._name}!\n")
        print("--Pokemon Championship--")

        # Loops game until opponents three pokemon or players pokemon faints
        while True:
            try:
                print(f"{opponent}: Ha, you can't defeat me!\n"
                      f"{opp_pokemon}\n")
                print(player_pokemon)
                print("Choose an Attack Type:")
                print("1. Normal")
                print("2. Special")
                p1 = int(input("Your Selection: "))
                if p1 not in [1, 2]:
                    print("Invalid Input! Choose 1 - 2.")
                    continue
                # Checks normal menu for player pokemon
                if p1 == 1:
                    normal_menu = player_pokemon.get_normal_menus()
                    print(normal_menu)
                    while True:
                        try:
                            p1 = int(input("Choose a Move: "))
                            if p1 == 1:
                                print(player_pokemon._slam(opp_pokemon))
                                break
                            elif p1 == 2:
                                print(player_pokemon._tackle(opp_pokemon))
                                break
                            else:
                                print("Invalid Input! Choose 1 or 2.")
                        except ValueError:
                            print("Invalid input! Please enter a number!")
                # Checks the special menu for players pokemon
                elif p1 == 2:
                    special_menu = player_pokemon.get_special_menu()
                    print(special_menu)
                    while True:
                        try:
                            p1 = int(input("Choose a Move: "))
                            if p1 == 1:
                                print(player_pokemon._special_move(opp_pokemon, player_pokemon._special_1))
                                break
                            elif p1 == 2:
                                print(player_pokemon._special_move(opp_pokemon, player_pokemon._special_2))
                                break
                            else:
                                print("Invalid Move! Choose 1 - 2.")
                        except ValueError:
                                print("Invalid Input! Choose 1 - 2. ")
            except ValueError:
                print("Invalid input! Please enter a number.")
            # Checks if opposing pokemon have fainted
            if opp_pokemon.hp <= 0:
                print(f"{opp_pokemon._name} has fainted!")
                Opp_pokeball = [p for p in Opp_pokeball if p.hp > 0]
                if not Opp_pokeball:
                    print(f"You defeated all of {opponent}'s Pokemon!\n")
                    break
                else:
                    opp_pokemon = random.choice(Opp_pokeball)
                    print(f"{opponent}:Come on {opp_pokemon._name} FIGHT1!\n")
            # Opponent will attack player, attacks are randomized through normal and special attacks
            move = random.choice([opp_pokemon._opp_special_1, opp_pokemon._opp_special_2, "Body Slam", "Bite"])
            if move == "Body Slam":
                print(opp_pokemon._opp_Body_slam(player_pokemon, move))
            elif move == "Bite":
                print(opp_pokemon._opp_Bite(player_pokemon, move))
            else:
                print(opp_pokemon.opponent(player_pokemon, move))
            # Game will end if players' pokemon faint
            if player_pokemon.hp <= 0:
                print(f"{player_pokemon._name} has fainted!")
                print(f"{opponent}: Heh, come back when you could put up a fight, DWEEB!")
                print("--Game Over--")
                return

if __name__ == '__main__':
    main()