# ==========================
# Palindrome Checker
# ==========================

palindrome_string = input("Enter a string: ").lower()
for i in range(len(palindrome_string) // 2):
    if palindrome_string[i] != \
            palindrome_string[len(palindrome_string) - 1 - i]:
        print(f'"{palindrome_string}" is not a palindrome.')
        break
    else:
        print(f'"{palindrome_string}" is a palindrome.')
        break

# Alternative approach

if palindrome_string == palindrome_string[::-1]:
    print(f'"{palindrome_string}" is a palindrome.')
else:
    print(f'"{palindrome_string}" is not a palindrome.')

# Using two pointers
left, right = 0, len(palindrome_string) - 1
is_palindorme = True
while left < right:
    if palindrome_string[left] != palindrome_string[right]:
        is_palindorme = False
        break
    left += 1
    right -= 1
if is_palindorme:
    print(f'"{palindrome_string}" is a palindrome.')
