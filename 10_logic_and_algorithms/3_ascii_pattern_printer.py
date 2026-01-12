def print_pattern(number):
    for i in range(1, number + 1):
        space = number - i
        star = 2 * i - 1
        print(" " * space + "*" * star)


number = int(input("Enter the number:- "))
print_pattern(number)
