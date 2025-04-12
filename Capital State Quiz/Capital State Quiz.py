'''
Thomas Johnson, Linh Dong
Date: 2/18/2025
Project: A State Capital Quiz is Given To The User When Running the Code
'''

import random

#Program reads all file lines and strips the keys and values into an empty dictionary
def read_file_to_dict():
    with open("C:\\Users\\hamst\\OneDrive\\Desktop\\HomeWork\\statecapitals.txt", 'r') as file:
        states = file.readlines()

    statecapitals = {}
    for state in states:
        key, value = state.split(',')
        statecapitals[key.strip()] = value.strip()

    return statecapitals

#The dictionary is converted into a list and randomizes the keys(states) only
def get_random_state(statecapitals):
    state = random.choice(list(statecapitals.keys()))
    return state, statecapitals[state]

#The dictionary is converted to a list again, but only takes the values(Capitals) instead then randomizes just three of the values.
def get_random_choices(statecapitals, correct_capital):
    capitals = list(statecapitals.values())
    capitals.remove(correct_capital)
    incorrect_cap = random.sample(capitals, 3)
    choices = incorrect_cap + [correct_capital]
    random.shuffle(choices)
    return choices

#ask_question constructs the quiz, and prompts the user.
def ask_question(state, correct_capital, choices):
#Calling the dictionary in the print elements
    print(f"What is the capital of {state}?")
    options = ['A', 'B', 'C', 'D']
    for i, choice in enumerate(choices):
        print(f"{options[i]}. {choice}")
#Passes in correct_capital parameter
    user = input("Enter selection | (A/B/C/D): ").strip().upper()
    if user in options:
        if choices[options.index(user)] == correct_capital:
            print("Correct!")
            return True
        else:
            print(f"Incorrect. The correct answer is {correct_capital}.")
            return False
    else:
        print("Invalid input. Input choices A-D")
        return ask_question(state, correct_capital, choices)

#Prompts the title, ties in every parameter and function, and counts the correct answers
def main():
    print("- State Capitals Quiz -")
    statecapitals = read_file_to_dict()
    correct_answers = 0
    for _ in range(10):
        state, correct_capital = get_random_state(statecapitals)
        choices = get_random_choices(statecapitals, correct_capital)
        if ask_question(state, correct_capital, choices):
            correct_answers += 1
    print(f"You got {correct_answers} correct!")

if __name__ == "__main__":
    main()