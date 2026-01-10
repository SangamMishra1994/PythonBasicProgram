# WAP to check whether number is prime or not
number = int(input("Enter the number:- "))
is_prime = True
for i in range(2, number // 2):
    if number % i == 0:
        is_prime = False
        break
if is_prime:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
