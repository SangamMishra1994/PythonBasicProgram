def caesar_cipher_encryption(message, shift):
    encrypted_text = ""

    for char in message:
        if char.isalpha():
            start = ord("A") if char.isupper() else ord("a")

            new_char = chr((ord(char) - start + shift) % 26 + start)
            encrypted_text += new_char

        else:
            encrypted_text += char
    return encrypted_text


message = input("Enter the message:- ")
result = caesar_cipher_encryption(message, 2)
print(f"Original messgae = {message} --> encrypted message = {result}")
