# WAP to find the first non-repeating character in the string
str = "sangamsmng"
char_count = {}
for ch in str:
    char_count[ch] = char_count.get(ch, 0) + 1

for ch in str:
    if char_count[ch] == 1:
        print(f"first non-repeating char:- {ch}")
        break
    else:
        print("No non-repeating number")
        break
