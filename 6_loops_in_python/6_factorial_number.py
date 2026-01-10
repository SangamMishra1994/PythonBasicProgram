# WAP to find the factorial number
number = int(input("Enter the number:- "))
factorial_value = 1
if number < 0:
    print("Factorial of a negative number is not possible!")
    exit()
for i in range(1, number + 1):
    factorial_value *= i
print(factorial_value)
