# Build an real game for mind exercise
import random


# Create hangman class
class HangmanGame:
    def __init__(self, word_list, max_attempts=6):
        self.secret_word = random.choice(word_list).upper()
        self.display_word = ["_"] * len(self.secret_word)
        self.max_attempts = max_attempts
        self.attempts_left = max_attempts
        self.guessed_letters = set()

    # Display Current Game Status
    def display_status(self):
        print("\nWord:- ", " ".join(self.display_word))
        print("Guessed Letter:- ", ", ".join(self.guessed_letters))
        print("Attempts left:- ", self.attempts_left)

    # Handle the guess letter
    def guess_letter(self, letter):
        letter = letter.upper()

        if not letter.isalpha() or len(letter) != 1:
            print("Please enter a single alphabet at once")
            return

        if letter in self.guessed_letters:
            print("You already gussed this letter.")
            return

        self.guessed_letters.add(letter)

        if letter in self.secret_word:
            print("Correct guess !")
            for index, char in enumerate(self.secret_word):
                if char == letter:
                    self.display_word[index] = letter

        else:
            print("Wrong guess!")
            self.attempts_left -= 1

    def is_won(self):
        return "_" not in self.display_word

    def is_lost(self):
        return self.attempts_left == 0

    def play(self):
        print("Welcome to Hangman Game!!")

        while not self.is_won() and not self.is_lost():
            self.display_status()
            guess = input("Guess a letter: ")
            self.guess_letter(guess)

        if self.is_won():
            print("\n Congratulations! you guessed the word:", self.secret_word)
        else:
            print("\n Game Over! The correct word was: ", self.secret_word)


if __name__ == "__main__":
    words = ["python", "developer", "hangman", "programming"]
    game = HangmanGame(words)
    game.play()
