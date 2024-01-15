import random

print("Welcome to a game of 21, you will have to get the closest to 21 as possible\n")

cards = ['1', '2', '3','4' ,'5' ,'6' ,'7' ,'8' ,'9' ,'10' , 'ace', 'king', 'queen' ,'jack',
    '1', '2', '3','4' ,'5' ,'6' ,'7' ,'8' ,'9' ,'10' , 'ace', 'king', 'queen' ,'jack', 
    '1', '2', '3','4' ,'5' ,'6' ,'7' ,'8' ,'9' ,'10' , 'ace', 'king', 'queen' ,'jack',
    '1', '2', '3','4' ,'5' ,'6' ,'7' ,'8' ,'9' ,'10' , 'ace', 'king', 'queen' ,'jack']

randomised = random.choice(cards)

def user():
    """
    This will give the user and the opponent their first card
    and will give the user the chance to get another card or
    stay with what they have.
    """
    intro = input("Hit or Stick:\n")
