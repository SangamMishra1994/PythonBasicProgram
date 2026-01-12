import datetime
import time


def digital_clock():
    print("Digital clock (Press ctrl+c) to stop")
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Clock :- {current_time}", end="\r", flush=True)
        time.sleep(1)


digital_clock()
