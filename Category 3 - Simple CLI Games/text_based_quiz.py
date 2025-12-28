# 10. Text-Based Adventure
# Concept: A "Choose Your Own Adventure" story. The user makes choices
# (e.g., "Go left or right?") that lead to different endings.
# Skills: Nested if/else statements and storytelling logic.

print("Welcome to the Text-based Adventure Game!!")
print("Your mission is to reach Accenture Office in Kormangla")

current_location = "Tara-Colive PG"
is_correct_path = True
while is_correct_path:
    print(f"You are currently at {current_location}.")
    choice1 = input(
        "Do you want to go 'left' towards sarjapura or 'right' \
towards Bellandur City Light Appartments?"
    ).lower()
    if choice1 == "left":
        current_location = "Sarjapura Road"
        choice2 = input(
            "You reached Sarjapura Road. Do you want to go \
'straight' towards Wipro or  \
'right' towards Kormangla?"
        ).lower()
        if choice2 == "straight":
            print(
                "You did wrong choice. You reached Wipro and stuck in \
\traffic, Do you want to choose again?"
            )
            decision = input(
                "Type 'yes' to choose again or 'no' \
        to exit."
            ).lower()
            if decision == "yes":
                continue
            else:
                is_correct_path = False
                print("Thank you for playing. Goodbye!")

        elif choice2 == "right":
            current_location = "Bellandur bus stop"
            choice3 = input(
                "You reached bellandur bus stop, \
do you want BMTC bus, auto, or rapido?"
            ).lower()
            if choice3 == "auto" or choice3 == "rapido":
                current_location = "Accenture Office Kormangla"
                print(
                    f"Congratulations! You have reached your destination: \
                {current_location}."
                )
                is_correct_path = False
            elif choice3 == "bmtc bus":
                print(
                    "Bus dropped at checkpost and from there. \
            you need to cross over brodge. Take 'left' or 'right'?"
                )
                choice4 = input().lower()
                if choice4 == "left":
                    current_location = "Accenture Office Kormangla"
                    print(
                        f"Congratulations! You have reached your destination: \
                {current_location}."
                    )
                    is_correct_path = False
                elif choice4 == "right":
                    print(
                        "You reached a dead end and couldn't find a way \
                to your destination. Do you want to choose again?"
                    )
                    decision = input(
                        "Type 'yes' to choose again or 'no' to exit."
                    ).lower()
                    if decision == "yes":
                        continue
                    else:
                        is_correct_path = False
                        print("Thank you for playing. Goodbye!")
    elif choice1 == "right":
        print(
            "You reached Bellandur City Light Appartments and \
    got stuck in traffic. Do you want to choose again?"
        )
        decision = input("Type 'yes' to choose again or 'no' to exit.").lower()
        if decision == "yes":
            continue
        else:
            is_correct_path = False
            print("Thank you for playing. Goodbye!")
print("Game Over.")
