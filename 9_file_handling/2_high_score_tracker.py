# 5. High Score Tracker

# Concept: Ask the user for a game score. Check a file named highscore.txt.
# If the new score is higher than the one in the file, overwrite it;
# otherwise, tell the user they didn't beat the record.
# Key Skill: Reading files ('r'), type conversion (string to int),
# and conditional writing.

# Not a good Coding approach

# try:
#     with open("highscore.txt", "r") as file:
#         content = file.readline().strip()
#         new_game_score = content.split("=")
#         if content == "":
#             print(f"High score is {game_score}")
#         elif game_score > int(new_game_score[1]):
#             with open("highscore.txt", "w") as fe:
#                 fe.write(f"Updated high score = {game_score}")
#                 print("File Updated successfully!!")
#         else:
#             print(
#                 f"Current user score {game_score} is lower than "
#                 f"previous score, Hence no changes made.\n"
#             )
# except FileNotFoundError:
#     print(f"\nFile does not exit, High score is {game_score}")


# Better approach

import re
from pathlib import Path

FILE_NAME = "highscore.txt"


def extract_score(text: str) -> int:
    match = re.search(r"\d+", text)
    return int(match.group()) if match else 0


def high_score_checker(game_score: int):
    current_score = 0

    if Path(FILE_NAME).exists():
        with open(FILE_NAME, "r") as file:
            content = file.read().strip()
            current_score = extract_score(content)

    if game_score > current_score:
        with open(FILE_NAME, "w") as file:
            file.write(f"High Score = {game_score}")
            print("🎉 New high score saved!")
    else:
        print(
            f"Current score {game_score} did not beat "
            f"the high score {current_score}"
        )


def main():
    while True:
        choice = input("\nDo you want to beat the current score (Y/N)?").lower()
        if choice != "y":
            break
        try:
            game_score = int(input("What is the score of the game?:- "))
            if game_score < 0:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a positive number.")
            continue
        high_score_checker(game_score)


if __name__ == "__main__":
    main()
