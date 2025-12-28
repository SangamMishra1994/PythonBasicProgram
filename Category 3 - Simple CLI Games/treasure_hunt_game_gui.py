import tkinter as tk


# Main game window
window = tk.Tk()
window.title("🏴‍☠️ Treasure Hunt Adventure")
window.geometry("600x400")
window.resizable(False, False)

# Global variable to track game state
current_scene = "start"

# Story text label
story_label = tk.Label(
    window, text="", font=("Arial", 14), wraplength=550, justify="center"
)
story_label.pack(pady=40)

# Button frame
button_frame = tk.Frame(window)
button_frame.pack(pady=20)

# Buttons
button1 = tk.Button(button_frame, width=20, font=("Arial", 12))
button2 = tk.Button(button_frame, width=20, font=("Arial", 12))
button1.grid(row=0, column=0, padx=10)
button2.grid(row=0, column=1, padx=10)


# Function to update story and buttons
def update_scene(scene):
    global current_scene
    current_scene = scene

    if scene == "start":
        story_label.config(
            text="🏝️ You arrive at the mysterious Crimson Isle.\n\n"
            "Legend says a great treasure is hidden here.\n"
            "Two paths lie ahead. What will you do?"
        )
        button1.config(text="Go Left (Jungle) \
            ", command=lambda: update_scene("jungle"))
        button2.config(text="Go Right (Beach) \
            ", command=lambda: update_scene("beach"))

    elif scene == "jungle":
        story_label.config(
            text="🌲 You enter the dark jungle.\n\n" " \
                A wild river blocks your path."
        )
        button1.config(
            text="Walk Along River \
            ",
            command=lambda: update_scene("temple"),
        )
        button2.config(
            text="Swim Across \
            ",
            command=lambda: update_scene("river_death"),
        )

    elif scene == "beach":
        story_label.config(text="You walk along beach and find an old boat.")
        button1.config(
            text="Take the Boat \
            ",
            command=lambda: update_scene("boat_death"),
        )
        button2.config(
            text="Ignore & Walk \
            ",
            command=lambda: update_scene("escape"),
        )

    elif scene == "temple":
        story_label.config(
            text="🏛️ You discover an ancient temple.\n\n"
            " \
                Two doors stand before you."
        )
        button1.config(
            text="Gold Door \
            ",
            command=lambda: update_scene("treasure"),
        )
        button2.config(text="Stone Door", command=lambda: update_scene("trap"))

    elif scene == "treasure":
        story_label.config(
            text="💰 CONGRATULATIONS!\n\n"
            "You found the Lost Treasure of the Crimson Isle!"
        )
        button1.config(
            text="Play Again \
            ",
            command=lambda: update_scene("start"),
        )
        button2.config(text="Exit", command=window.quit)

    elif scene == "trap":
        story_label.config(
            text="☠️ A trap is triggered!\n\n" "\
                The temple collapses. Game Over."
        )
        button1.config(text="Try Again", command=lambda: update_scene("start"))
        button2.config(text="Exit", command=window.quit)

    elif scene == "river_death":
        story_label.config(
            text="🐊 The river is full of crocodiles.\n\n"
            "You did not survive. Game Over."
        )
        button1.config(text="Try Again", command=lambda: update_scene("start"))
        button2.config(text="Exit", command=window.quit)

    elif scene == "boat_death":
        story_label.config(
            text="🌊 The boat has a leak.\n\n"
            "\
                You sink into the ocean. Game Over."
        )
        button1.config(text="Try Again", command=lambda: update_scene("start"))
        button2.config(text="Exit", command=window.quit)

    elif scene == "escape":
        story_label.config(
            text="🚣 You meet a fisherman who helps you escape.\n\n"
            "You survive, but never find the treasure."
        )
        button1.config(
            text="Play Again \
            ",
            command=lambda: update_scene("start"),
        )
        button2.config(text="Exit", command=window.quit)


# Start game
update_scene("start")

# Run the application
window.mainloop()
