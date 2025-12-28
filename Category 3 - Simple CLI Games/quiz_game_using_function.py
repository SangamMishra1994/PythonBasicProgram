import random
import time

# ---------------- QUESTION BANK ----------------
quiz_data = {
    "Easy": {
        "What is the capital of India?": "Delhi",
        "National flower of India?": "Lotus",
        "National game of India?": "Hockey",
        "Prime Minister of India?": "Narendra Modi",
        "Full form of ISRO?": "Indian Space Research Organization",
    },
    "Medium": {
        "Who is the founder of Microsoft?": "Bill Gates",
        "What is the capital of Japan?": "Tokyo",
        "Which planet is known as Red Planet?": "Mars",
        "What is H2O?": "Water",
        "Fastest land animal?": "Cheetah",
    },
    "Hard": {
        "Who developed Python?": "Guido van Rossum",
        "What does OOP stand for?": "Object Oriented Programming",
        "Binary of 10?": "1010",
        "What is CPU?": "Central Processing Unit",
        "HTTP full form?": "HyperText Transfer Protocol",
    },
}


# ---------------- FUNCTION TO ASK QUESTION ----------------
def ask_question(question, correct_answer, time_limit):
    print("\n" + question)
    start_time = time.time()
    answer = input("Answer: ")
    end_time = time.time()

    if end_time - start_time > time_limit:
        print("⏰ Time's up!")
        return False

    if answer.strip().lower() == correct_answer.lower():
        print("✅ Correct!")
        return True
    else:
        print("❌ Wrong answer!")
        return False


# ---------------- FUNCTION TO PLAY LEVEL ----------------
def play_level(level_name, questions, time_limit):
    print(f"\n--- {level_name} Level Started ---")
    score = 0

    question_list = list(questions.items())
    random.shuffle(question_list)

    for question, answer in question_list:
        if ask_question(question, answer, time_limit):
            score += 1
        else:
            print("Game Over!")
            break

    return score


# ---------------- MAIN QUIZ FUNCTION ----------------
def start_quiz():
    print("🎮 Welcome to Quiz Game 🎮")
    player_name = input("Enter your name: ")
    print(f"\nWelcome {player_name}! Let’s start the game.")

    total_score = 0

    levels = [("Easy", 10), ("Medium", 7), ("Hard", 5)]

    for level_name, time_limit in levels:
        score = play_level(level_name, quiz_data[level_name], time_limit)
        total_score += score

        if score < 3:
            print(f"\n❌ You failed the {level_name} level.")
            break
        else:
            print(f"🎉 You cleared {level_name} level!")

    print(f"\n🏆 Final Score of {player_name}: {total_score}")


# ---------------- RUN PROGRAM ----------------
start_quiz()
