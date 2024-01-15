import random

print("Welcome to a game of 21, you will have to get the closest to 21 as possible\n")
print("Your opponent is also trying to get as close to 21 but if they reach 17 or higher they can not get another card.\n")


cards = ['2', '3','4' ,'5' ,'6' ,'7' ,'8' ,'9' ,'10' , 'ace', 'king', 'queen' ,'jack',
    '2', '3','4' ,'5' ,'6' ,'7' ,'8' ,'9' ,'10' , 'ace', 'king', 'queen' ,'jack', 
    '2', '3','4' ,'5' ,'6' ,'7' ,'8' ,'9' ,'10' , 'ace', 'king', 'queen' ,'jack',
    '2', '3','4' ,'5' ,'6' ,'7' ,'8' ,'9' ,'10' , 'ace', 'king', 'queen' ,'jack']

ace = 1 or 10
king = 10
queen = 10
jack = 10

randomised = random.choice(cards)
user_result_one = print(randomised)
randomised_two = random.choice(cards)

def user():
    """
    This will give the user and the opponent their first card
    and will give the user the chance to get another card or
    stay with what they have.
    """
    intro = input("Hit or Stick:\n")
    if intro.endswith('Hit'):
        print(randomised)
        print("Opponents Turn...\n")
    if intro.endswith("Stick"):
        print("Opponents Turn...\n")#

    def opponent():
