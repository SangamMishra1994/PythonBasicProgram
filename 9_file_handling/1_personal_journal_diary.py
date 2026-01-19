from datetime import datetime


DIARY_FILE = "journal_diary.txt"


def write_journal_diary():
    print("\n Journal Diary")
    print("Type your entry below")
    print("Type 'EXIT' on a new line to stop writing.\n")

    user_entries = []

    while True:
        line = input()
        if line.strip().upper() == "EXIT":
            break
        user_entries.append(line)

        if not user_entries:
            print("No content entered. Nothing saved")
            return
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(DIARY_FILE, "a", encoding="utf-8") as file:
            file.write("\n" + "=" * 50 + "\n")
            file.write(f"Entry Date & Time: {timestamp}\n")
            file.write("=" * 50 + "\n")
            for entry in user_entries:
                file.write(entry + "\n")

        print("\nJournal entry saved successfully!!")


def main():
    while True:
        choice = input("Do you want to write a journal entry? (Y/N): ").lower()
        if choice == "y":
            write_journal_diary()
        elif choice == "n":
            print("Exiting Journal Diary. Have a great day!")
            break
        else:
            print("Invalid choice. Please enter Y or N.")


if __name__ == "__main__":
    main()
