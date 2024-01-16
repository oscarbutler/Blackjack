import random


cards = ['2', '3', '4', '5', '6', '7', '8', '9',
         '10', 'ace', 'king', 'queen', 'jack',
         '2', '3', '4', '5', '6', '7', '8', '9',
         '10', 'ace', 'king', 'queen', 'jack',
         '2', '3', '4', '5', '6', '7', '8', '9',
         '10', 'ace', 'king', 'queen', 'jack',
         '2', '3', '4', '5', '6', '7', '8', '9',
         '10', 'ace', 'king', 'queen', 'jack']

ace = 1
king = 10
queen = 10
jack = 10

def user_turn():
    print("Your Turn:")
    randomised_card = random.choice(cards)
    print("randomised_card for a user: ", randomised_card)
    return randomised_card

def opponent_turn():
    print("Opponents Turn:")
    randomised_card = random.choice(cards)
    print("randomised_card for the opponent: ", randomised_card)
    return randomised_card

#def stop_recieving_card():
 #   return 17 <= 

#def opponent_first_turn():
   # opponent_turn = random.choice(cards)
   # return opponent_turn

def main_game_logic():
    """
    This will give the user and the opponent their first card
    and will give the user the chance to get another card or
    stay with what they have.
    """

    user_total = 0
    opponent_total_score = 0
    user_result_one = user_turn()

    while True:
        intro = input("Hit or Stick:\n")
        print("Opponents Turn...\n")
        randomised_two = random.choice(cards)
        print("randomised_two for a comp", randomised_two)
        opponent_score = randomised_two
        opponent_total_score += value(opponent_score)
        print(f"Opponents total score is: {opponent_total_score}")

        if opponent_total_score > 21:
           print("You have won. Well done!")
           return user_total, opponent_total_score
    
        if intro.lower().strip().endswith('hit'):
            user_result_two = user_turn()
            user_total += value(user_result_two)
            print(f"Your total score is: {user_total}")            
            
            if user_total > 21:
                print("You've lost, better luck next time!")
                return user_total
        
        elif intro.lower().strip().endswith("stick"):
            randomised_two = random.choice(cards)
            #print("Opponents Turn...\n")
            #if user_total > 21:
            #   print("You've lost, better luck next time!")
            #  return
        
        else:
            print("Invalid input. Please enter 'Hit' or 'Stick'.")

    return user_total, opponent_total_score

def value(card):
    if card.isdigit():
        return int(card)
    elif card.lower() == 'ace':
        return ace
    else:
        return 10

#def opponent():
    """
    The score for the opponent which will be automised.
    """
    #print("Opponents Turn...\n")
    #randomised_two = random.choice(cards)
    #print(randomised_two)

def game_summarising():
    """
    Adds all the functions that will be displayed into one function
    """
    user_score, opponent_score = main_game_logic()
    print(f"User's Total Score: {user_score}")
    print(f"Opponent's Total Score: {opponent_score}")

def print_menu():
    print("""[1] Play The Game!
[2] How to Play
[3] Credits"
[0] Exit the programn.""")


def main():
    print_menu()
    answer = int(input("Enter your option: "))

    while answer != 0:
        if answer == 1:
            print("Option 1 has been chosen.")
            game_summarising()
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

        print_menu()
        print()
        answer = int(input("Enter your option: "))

if __name__ == "__main__":
    main()