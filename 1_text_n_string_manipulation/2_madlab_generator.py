# =========================================
# Mad Libs Generator in Simpler way
# =========================================

# print("Welcome to the Mad Libs Generator! Game!!")
# print("Please provide the following words:")
# nounn1 = input("Enter a noun: ")
# verb1 = input("Enter a verb: ")
# adjective1 = input("Enter an adjective: ")
# emotion1 = input("Enter an emotion: ")
# place1 = input("Enter a place: ")

# madlib_story = f"""
# Once upon a time in a {adjective1} land called {place1},
# there lived a {nounn1} who loved to {verb1}.
# Every day, the {nounn1} would feel very {emotion1} about its adventures.
# """

# print("Here is your Mad Libs story:")
# print(madlib_story)


# ====================================================
# Using List and Dictionary to make it more scalable
# ====================================================

print("Welcome to the Mad Libs Generator! Game!!")
placeholders = [
    "adjective1",
    "adjective2",
    "adjective3",
    "adjective4",
    "noun1",
    "noun2",
    "noun3",
    "noun4",
    "verb1",
    "verb2",
    "verb3",
    "verb4",
    "emotion1",
    "emotion2",
    "place1",
    "place2",
    "animal1",
    "animal2",
    "food1",
    "food2",
    "person1",
    "person2",
]

word_dict = {}
for placeholder in placeholders:
    word_dict[placeholder] = input(
        f""" Enter a {placeholder.replace('1', '').replace('2', '')
                                 .replace('3', '').replace('4', '')}:
        """
    )

# Step 3: Build the story using triple quotes and f-strings

story = f"""
Once upon a time, a {word_dict['adjective1']} {word_dict['noun1']}
decided to {word_dict['verb1']} to {word_dict['place1']}.
There, they met {word_dict['person1']}, who had a {word_dict['adjective2']}
{word_dict['noun2']}. Together, they decided to {word_dict['verb2']}
with a {word_dict['animal1']} while eating {word_dict['food1']}. Suddenly,
a {word_dict['adjective3']} {word_dict['noun3']} appeared
and {word_dict['verb3']} towards them. Everyone felt {word_dict['emotion1']},
but {word_dict['person2']} quickly {word_dict['verb4']} the situation.
In the end, the {word_dict['animal2']} and all the friends celebrated
at {word_dict['place2']} with {word_dict['food2']}.
It was a truly {word_dict['adjective4']} adventure!
And they all lived {word_dict['emotion2']} ever after.
"""

print("Here is your Mad Libs story:")
print(story)
