# WAP to calcualte the factorial of a number


def calculate_factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result


number = int(input("Enter the number:- "))
print(f"Factorial of {number} is :- ", calculate_factorial(number))
