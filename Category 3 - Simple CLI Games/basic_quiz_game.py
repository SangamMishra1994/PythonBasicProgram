# Basic Quiz Game
# Concept: Displays a question, asks for an answer,
# checks if it's correct, and keeps a score.
# Skills: Dictionaries (to store questions/answers) or Lists,
# and incrementing variables (counters).
from random import choice


print("Welcome to Quiz Game!!")
question_bank = {
    "What is the capital of india?": "Delhi",
    "What is the natioal flower of India?": "Lotus",
    "National game of India?": "Hockey",
    "Prime Minister of India?": "Sri Narendar Modi",
    "Full form of ISRO?": "Indian space Reasearch Organization",
}

is_correct = True
score = 0
name_of_player = input("Enter your name:- ")
print(f"Welcome {name_of_player} to Hot seat!!")

while is_correct:
    question = choice(list(question_bank.keys()))
    print(question)

    player_answer = input("Answer:- ")

    if player_answer.strip().lower() == question_bank[question].lower():
        print("Correct !!")
        score += 1
     
        del question_bank[question]
    else:
        print("Ohh !! Wrong answer, Better luck next time.")
        is_correct = False
        break
print(f"Final score is {score}")
