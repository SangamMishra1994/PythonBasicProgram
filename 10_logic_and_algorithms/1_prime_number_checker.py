# WAP to chcek whether nunber is Prime or not

def prime_number_checker(number):
    is_prime = True
    if number < 0:
        return False
    for i in range(2, number // 2):
        if number % i == 0:
            is_prime = False
            break
    return is_prime


number = int(input("Enter a number:- "))
result = prime_number_checker(number)
print(f"Is number {number} is prime = {result}")
