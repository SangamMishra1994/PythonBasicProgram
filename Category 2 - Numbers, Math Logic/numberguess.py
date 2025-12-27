# =========================================
# Number Guessing Game
# =========================================

import random


def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempt = 0
    max_attempt = 3
    print("welcome to number guessing sytem")
    while attempt < max_attempt:
        user_guess = int(input("Enter your guess between 1 to 100: "))
        if user_guess == number_to_guess:
            print("Congratulations! You guessed the correct number.")
            break
        else:
            attempt += 1
            if user_guess < number_to_guess:
                print("Your guess is too low.")
            else:
                print("Your guess is too high.")
            print(
                f"Wrong guess. You have {max_attempt - attempt} attempts \
left."
            )
            if attempt == max_attempt:
                print(
                    f"Sorry, you've used all attempts. The correct number \
was {number_to_guess}."
                )


number_guessing_game()
print("Thank you for playing the number guessing game.")
