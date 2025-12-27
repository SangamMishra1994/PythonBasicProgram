# ================
# import math
# ================


def add(first_num, second_num):
    return first_num + second_num


def subtract(first_num, second_num):
    return first_num - second_num


def multiply(first_num, second_num):
    return first_num * second_num


def division(first_num, second_num):
    if second_num == 0:
        return "Error: Division by zero is not allowed."
    return first_num / second_num


print("For now only input Integer values")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

is_true = True

while is_true:
    print(
        """
    Select operation:
    1. Add
    2. Substract
    3. Multiply
    4. Division
    5. Exit
    """
    )
    result = 0
    choice = input("Enter choice: ")
    if choice == "1":
        result = add(num1, num2)
        print(f"The sum of {num1} and {num2} is: {result}")
    elif choice == "2":
        result = subtract(num1, num2)
        print(f"The difference of {num1} and {num2} is: {result}")
    elif choice == "3":
        result = multiply(num1, num2)
        print(f"The product of {num1} and {num2} is: {result}")
    elif choice == "4":
        result = division(num1, num2)
        print(f"The division of {num1} by {num2} is: {result}")
    elif choice == "5":
        print("Exiting the calculator. Goodbye!")
        is_true = False
print("Thank you for using the calculator.")
