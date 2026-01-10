# WAP to find the sum of even numbers
number_list = [1, 2, 3, 4, 12, 13, 15, 20, 23, 28]
sum = 0
for i in number_list:
    sum += i if i % 2 == 0 else 0
    print(f"{i}", end=", ")
print(f"\nSum of numbers:- {sum}")
