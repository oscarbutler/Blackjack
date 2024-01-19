import random
import os
os.system('cls' if os.name == 'nt' else 'clear')


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
    print("Users card: ", randomised_card)
    return randomised_card


def opponent_turn(opponent_total_score):
    print("Opponents Turn:")
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
                return user_total

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

        while opponent_total_score <= 21:
            if opponent_total_score > user_total:
                print("You lose, better luck next time!")
                break

    return user_total, opponent_total_score


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


def print_menu():
    print("""[1] Play The Game!
[2] How to Play
[3] Credits
[0] Exit the programn.""")


def main():
    print_menu()

    while True:
        try:
            answer = int(input("Enter your option: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if answer == 1:
            print("Option 1 has been chosen.")
            game_summarising()
        elif answer == 2:
            print(f"""Option 2 has been chosen.\n
              Welcome to a game of 21, you will
              have to get the closest to 21 as possible\n
              Your opponent is also trying to get as close to 21 but if
              they reach 17 or higher they can not get another card.
              In this version the opponent is allowed to stick whenever
              so be careful!\n""")
        elif answer == 3:
            print("""Option 3 has been chosen.\n
                https://github.com/oscarbutler""")
        elif answer == 0:
            print("Programme stopping")
            break
        else:
            print("Invalid Option.")

        print_menu()
        print()
        answer = int(input("Enter your option: "))


if __name__ == "__main__":
    main()
