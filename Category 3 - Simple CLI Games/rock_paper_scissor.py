# Concept: Play a round against the computer. The computer chooses randomly,
# and you compare the results to declare a winner.
# Skills: random.choice(), boolean logic (and/or), and
# while loops for "play again" functionality.

from random import choice


def rock_paper_scissor():
    choices = ["rock", "paper", "scissor"]
    user_score = 0
    computer_score = 0
    rounds = int(input("Enter the number of rounds want to play: "))
    for round in range(rounds):
        user_choice = input("Enter your choice: ").lower()
        if user_choice not in choices:
            print("Invalid choice! Please choose rock, paper, or scissor.")
            continue
        computer_choice = choice(choices)
        print(f"Computer chose: {computer_choice}")
        if user_choice == computer_choice:
            print("It's a tie!!")
        elif (
            (user_choice == "rock" and computer_choice == "scissor")
            or (user_choice == "paper" and computer_choice == "rock")
            or (user_choice == "scissor" and computer_choice == "paper")
        ):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Final Scores - You: {user_score}, Computer: {computer_score}")
        if user_score > computer_score:
            print("Congratulations! You won the game!")

        elif computer_score > user_score:
            print("Computer won the game! Better luck next time.")


rock_paper_scissor()
