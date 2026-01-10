name = input("Enter the string:- ")
reverse_str = ""
length = len(name)
for i in range(0, length):
    reverse_str += name[length - i - 1]
print(f"Reverse String:- {reverse_str}")
