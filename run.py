import random
import os

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
    """
    Chooses a random card out of the cards variablefor the user to have."""
    print("Your Turn:")
    randomised_card = random.choice(cards)
    print("Users card: ", randomised_card)
    return randomised_card


def opponent_turn(opponent_total_score):
    """
    Chooses a random card out of the cards variable for the opponent to have.
    If the opponent's total score is between 17 and 21, the opponent
    will stick.
    """
    print("Opponents Turn:")
    if 17 <= opponent_total_score <= 21:
        print("Opponent chooses to stick.")
        return 'stick'
    else:
        randomised_card = random.choice(cards)
        print("Opponents card: ", randomised_card)
        return randomised_card


def main_game_logic():
    """
    This will give the user and the opponent their first card
    and will give the user the chance to get another card or
    stay with what they have.
    """

    user_total = 0
    opponent_total_score = 0
    user_result_one = user_turn()
    opponent_result_one = opponent_turn(opponent_total_score)

    user_total += value(user_result_one)
    opponent_total_score += value(opponent_result_one)

    user_stays = False

    while True:
        intro = input("Hit or Stick:\n").lower().strip()

        if intro not in ['hit', 'stick']:
            print("Invalid input. Please enter 'Hit' or 'Stick'.\n")
            continue

        print("Opponents Turn...\n")
        opponent_score = opponent_turn(opponent_total_score)

        if opponent_score == 'stick':
            print(f"Opponents total score is: {opponent_total_score}\n")
        else:
            opponent_total_score += value(opponent_score)
            print(f"Opponents total score is: {opponent_total_score}\n")

            if opponent_total_score > 21:
                print("You have won. Well done!\n")
                return user_total, opponent_total_score

        if intro.lower().strip().endswith('hit') and not user_stays:
            user_result_two = user_turn()
            user_total += value(user_result_two)
            print(f"Your total score is: {user_total}\n")

            if user_total > 21:
                print("You've lost, better luck next time!")
                return user_total, opponent_total_score

        elif intro.lower().strip().endswith("stick") and not user_stays:
            print("You have chosen to stick")
            user_stays = True

        if user_stays:
            while 17 <= opponent_total_score <= 21:
                print("Opponents Turn...\n")
                opponent_score = opponent_turn(opponent_total_score)

                if opponent_score == 'stick':
                    print(f"Opponents total score is: {opponent_total_score}")
                    break
                else:
                    opponent_total_score += value(opponent_score)
                    print("Invalid input. Please enter 'Hit' or 'Stick'.\n")

            print("Opponents sticks")
            break

    return user_total, opponent_total_score

def get_the_winner(user_score, opponent_score):
    if user_score > 21:
        print("You've lost, better luck next time!")
    elif opponent_score > 21:
        print("You have won. Well done!")
    elif user_score > opponent_score:
        print("You have won. Well done!")
    elif user_score < opponent_score:
        print("You've lost, better luck next time!")
    else:
        print("It is a draw!") 

def value(card):
    """
    Create the value for ace
    """
    if card.isdigit():
        return int(card)
    elif card.lower() == 'ace':
        return ace
    else:
        return 10


def game_summarising():
    """
    Adds all the functions that will be displayed into one function
    """
    user_score, opponent_score = main_game_logic()
    print(f"User's Total Score: {user_score}")
    print(f"Opponent's Total Score: {opponent_score}")
    get_the_winner(user_score, opponent_score)
    print_menu()


def print_menu():
    """This will show the menu when the programme starts"""
    print("""[1] Play The Game!
[2] How to Play
[3] Credits
[0] Exit the programn.""")
    while True:
        try:
            answer = input("Enter your option: ")
            if not answer.isnumeric():
                print(
                    f"""
{answer} is not the option that is required. Please use numbers 0 - 3
"""
                )
            else:
                answer = int(answer)
            # answer = int(input("Enter your option: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if answer == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Option 1 has been chosen.")
            game_summarising()
        elif answer == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""Option 2 has been chosen.\n
              Welcome to a game of 21, you will
              have to get the closest to 21 as possible\n
              Your opponent is also trying to get as close to 21 but if
              they reach 17 or higher they can not get another card.
              In this version the opponent is allowed to stick whenever
              so be careful!\n
              If the user or opponent goes over 21 then they will lose!\n""")
        elif answer == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("""Option 3 has been chosen.\n
                https://github.com/oscarbutler""")
        elif answer == 0:
            print("Programme stopping")
            exit()
        else:
            print("Invalid Option. The number should be between 0-3")

        print_menu()
        print()


def main():
    """This is what is going to be shown when
    choosing each option in the menu"""
    print_menu()


if __name__ == "__main__":
    main()
