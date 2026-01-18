import time

my_dict = {
    "sangam123@gmail.com": "Hello123@",
    "devender@zohomail.in": "Byebye123@",
    "Mohan@yahoo.com": "Hehe@123",
}


def login_to_system(username, password):
    return my_dict.get(username) == password


def logout_to_system():
    print("Logged out successfully.")


while True:  # entire application loop
    counter = 3
    login_success = False

    while counter > 0:
        user = input("Enter the username: ")
        password = input("Enter the password: ")

        if login_to_system(user, password):
            print("Login Successful!")
            login_success = True

            try:
                with open("secret_file.txt", "r") as file:
                    print(file.read())
            except FileNotFoundError:
                print("File not found")

            while True:
                choice = input("Do you want to logout? (Y/N): ").lower()
                if choice == "y":
                    logout_to_system()
                    break
                elif choice == "n":
                    print("Session active...")
                else:
                    print("Invalid choice")

            break  # exit attempt loop ONLY

        else:
            counter -= 1
            print(f"Invalid credentials. Attempts left: {counter}")

    # 🔒 cooldown only if login NEVER succeeded
    if not login_success and counter == 0:
        print("Too many failed attempts. Please wait 10 seconds...")
        time.sleep(10)

        retry = input("Do you want to login again? (Y/N): ").lower()
        if retry != "y":
            print("Exiting program.")
            break

    # 🔄 after successful logout
    if login_success:
        retry = input("Do you want to login again? (Y/N): ").lower()
        if retry != "y":
            print("Exiting program.")
            break
