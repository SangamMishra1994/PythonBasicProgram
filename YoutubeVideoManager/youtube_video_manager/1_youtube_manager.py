import json


def load_data():
    try:
        with open("youtube.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)


def list_all_videos(videos):
    pass


def add_video(videos):
    pass


def update_video(videos):
    pass


def delete_video(videos):
    pass


def main():
    while True:
        videos = load_data()
        print("\n Youtube Manager | choose an option")
        print("1. List all the youtube videos")
        print("2. Add a new youtube video")
        print("3. Update the youtube video details")
        print("4. Delete the youtube video")
        print("5. Exit the app")
        choice = input("Enter a choice:- ")
        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Wrong choice try again!!")


if __name__ == "__main__":
    main()
