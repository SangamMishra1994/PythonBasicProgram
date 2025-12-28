# Dice Rolling Simulator
# Concept: Simulates rolling one or more dice.
# You can add complexity by asking how many sides the die has (d6, d20).
# Skills: random.randint(), function definition, and loops.
import random


print("🎲 Welcome to Dice Roll Game!")

is_continue = True

while is_continue:
    no_of_dice = int(input("\nEnter the number of dice: "))

    dice_sides = []

    # Take input for each dice
    for i in range(no_of_dice):
        sides = int(input(f"Enter number of sides for dice {i + 1}: "))
        dice_sides.append(sides)

    # Roll each dice
    print("\nRolling the dice...")
    for i, sides in enumerate(dice_sides, start=1):
        result = random.randint(1, sides)
        print(f"Dice {i}: You rolled {result} on a {sides}-sided dice")

    # Ask to continue
    choice = input("\nDo you want to roll again? (yes/no): ").lower()
    if choice == "no":
        is_continue = False

print("\nThank you for playing the Dice Roll Simulator! 🎉")
