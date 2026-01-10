# WAP to check list contain unique element
def is_unique(list):
    return len(list) == len(set(list))


number_list = [1, 2, 3, 4, 5]
print(is_unique(number_list))

number_list2 = [1, 2, 2, 3, 4, 5, 3]
print(is_unique(number_list2))
