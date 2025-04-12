"""
Author: Thomas Johnson, Linh Dong
Date: 3/11/2025
Project: Program allows user to be a hero and fight three different dragons
"""

from entity import Entity
from hero import Hero
from dragon import Dragon
from fire import FireDragon
from flying import FlyingDragon
import random
import time

def main():
    # User inputs their name
    user = input("What is your name?\n")
    # Hero object | Connected to entity
    hero = Hero(user, 50)
    # Dragon object | Connected to entity
    dragons = [Dragon("Bad Dragon", 10), FireDragon("Flamin' Hot Dragon", 15 ), FlyingDragon("Soar Dragon", 20)]
    print(f"Welcome to the\n  ~GAUNLET~\n{user}")
    print("...You have to defeat 3 powerful dragons...\n")
    # Starts the game
    while len(dragons) > 0 and hero.get_hp() > 0:
        # Prints Hero stats
        print(hero)
        # Prints Dragons stats
        for i, dragon in enumerate(dragons, start=1):
            print(f"{i}. {dragon}")
        try:
            drgn = int(input("Choose a Dragon to Attack: "))
            if 1 <= drgn <= len(dragons):
                dragon = dragons[drgn - 1]
            else:
                print("Invalid Input! Choose 1 - 3")
                continue
        except ValueError:
            print("Invalid Input! Choose 1 - 3")
            continue

            # Checks which weapon the Hero has chosen
        try:
            weapon = int(input("\n--Weapons--\n"
                                f"1. Sword (6 ~ ATK)\n"
                                f"2. Bow (12 ~ ATK)\n"
                                f"Your Choice of Weapon: "))

            if weapon == 1:
                print(f"-You've Swung Your Blade Towards {dragon.get_name()}-")
                hero.sword_attack(dragon)
            elif weapon == 2:
                print(f"-You've Shot an Arrow At {dragon.get_name()}-")
                hero.arrow_attack(dragon)
            else:
                print("Invalid Input ~ Choose 1 or 2")
                continue

        except ValueError:
            print("Invalid Input ~ Choose 1 or 2")
            continue

        # Randomizes the dragons and their attacks
        # Fire and Flying dragons will use special attacks first
        heart = [d for d in dragons if d.get_hp() > 0]
        if heart:
            random_drgn = random.choice(heart)
            print(f"{random_drgn.get_name()} is preparing to attack...")
            random_drgn.special_attack(hero)

        # Checks if any of the dragons have died
        if dragon.get_hp() <= 0:
            print(f"{dragon.get_name()} has been defeated!")

        # Checks if Hero killed all dragons
        if all(dragon.get_hp() <= 0 for dragon in dragons):
            print("------------------------")
            time.sleep(2)
            print(f"You've Done It {hero.get_name()} 🥹, You've Saved the World!")
            break

    # Checks if Hero has died
    if hero.get_hp() <= 0:
        print(f"~~{hero.get_name()} screams in pain~~")
        print("You've Died!")
        print("------------------------")
        time.sleep(2)
        print("--Aftermath--")
        time.sleep(2)
        print("Without You, 70% of Humanity is Dead\n...That Number Will Keep Going Up...")
        time.sleep(2)
        print("--Game Over--")

if __name__ == "__main__":
    main()

