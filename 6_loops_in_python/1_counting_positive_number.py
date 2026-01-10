# WAP to count the positive number in the given list
number_list = [1, 2, 3, -1, -5, 12, -9, 15, 28]
count = 0
for i in number_list:
    if i > 0:
        count += 1
print(f"toatl positive number:- {count}")
