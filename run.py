import random

print("Welcome to a game of 21, you will have to get the closest to 21 as possible\n")
print("Your opponent is also trying to get as close to 21 but if they reach 17 or higher they can not get another card.\n")


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
    user_result_one = user_turn()
    user_total = [user_result_one]
    intro = input("Hit or Stick:\n")
    if intro.lower().strip().endswith('Hit'):
        print(randomised)
        print("Opponents Turn...\n")
    if intro.lower().strip().endswith("Stick"):
        print("Opponents Turn...\n")
        if user_total > 21:
            print("You've lost, better luck next time!")
            return
    if intro.endswith('Hit'):
        print(user_result_two)
    else:
        print("Invalid input. Please enter 'Hit' or 'Stick'.")
        user()

def opponent():
    """
    The score for the opponent which will be automised.
    """
    print("Opponents Turn...\n")
    randomised_two = random.choice(cards)
    print(randomised_two)

def main():
    opponent_score = opponent()
    user_score = user()