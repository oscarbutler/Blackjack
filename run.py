import random


cards = ['2', '3', '4', '5', '6', '7', '8', '9',
         '10', 'ace', 'king', 'queen', 'jack',
         '2', '3', '4', '5', '6', '7', '8', '9',
         '10', 'ace', 'king', 'queen', 'jack',
         '2', '3', '4', '5', '6', '7', '8', '9',
         '10', 'ace', 'king', 'queen', 'jack',
         '2', '3', '4', '5', '6', '7', '8', '9',
         '10', 'ace', 'king', 'queen', 'jack']

ace = 1 or 10
king = 10
queen = 10
jack = 10

def user_turn():
    print("Your Turn:")
    randomised = random.choice(cards)
    print(randomised)

def user():
    """
    This will give the user and the opponent their first card
    and will give the user the chance to get another card or
    stay with what they have.
    """

    user_total = 0
    user_result_one = user_turn()

    while True:
        intro = input("Hit or Stick:\n")

        print("Opponents Turn...\n")
        randomised_two = random.choice(cards)
        print(randomised_two)
        opponent_score = randomised_two
        if opponent_score > 21:
            print("You have won. Well done!")

    
        if intro.lower().strip().endswith('Hit'):
            user_result_two = user_turn()
        
        if intro.lower().strip().endswith("Stick"):
            print("Opponents Turn...\n")
            if user_total > 21:
                print("You've lost, better luck next time!")
                return
        
        if intro.endswith('Hit'):
            print(user_result_two)

        else:
            print("Invalid input. Please enter 'Hit' or 'Stick'.")

def value(card):
    if card.isdigit():
        return int(card)
    elif card.lower() == 'ace':
        return ace
    else:
        return 10

def opponent():
    """
    The score for the opponent which will be automised.
    """
    print("Opponents Turn...\n")
    randomised_two = random.choice(cards)
    print(randomised_two)

def main():
    """
    Adds all the functions that will be displayed into one function
    """
    opponent_score = opponent()
    user_score = user()

def menu():
    print("""[1] Play The Game!
    [2] How to Play
    [3] Credits"
    [0] Exit the programn.""")

menu()
answer = int(input("Enter your option: "))

while answer != 0:
    if answer == 1:
        print("Option 1 has been chosen.")
        main()
    elif answer == 2:
        print(f"""Option 2 has been chosen.\n
              Welcome to a game of 21, you will
              have to get the closest to 21 as possible\n
              Your opponent is also trying to get as close to 21 but if
              they reach 17 or higher they can not get another card.\n""")
    elif answer == 3:
        print("""Option 3 has been chosen.\n#
              https://github.com/oscarbutler""")
    else:
        print("Invalid Option.")

    menu()
    print()
    answer = int(input("Enter your option: "))