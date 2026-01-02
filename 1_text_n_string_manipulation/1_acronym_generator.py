# Acronym Generator

phrase = input("Enter a phrase to generate its acronym: ")
words = phrase.split()
acronym = ""
for word in words:
    acronym += word[0].upper()
print(f"The acronym for '{phrase}' is: {acronym}")
