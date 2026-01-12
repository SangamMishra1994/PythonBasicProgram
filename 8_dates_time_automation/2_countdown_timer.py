import time


def countdown_timer(seconds):
    print("Countdown Start!!")
    while seconds >= 0:
        # {seconds:02d} formats an integer to be at least two digits wide,
        # padding with leading zeros if necessary.
        print(f"Remaining: {seconds:02d} seconds", end="\r", flush=True)
        time.sleep(1)
        seconds -= 1
    print("Time's Up")


seconds = int(input("Enter the seconds:- "))
countdown_timer(seconds)
