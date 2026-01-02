# ==========================
# Word Counter
# ==========================

paragraph = input("Enter a paragraph of text: ")
words = paragraph.split()
word_count = 0
word_list = []
for word in words:
    word_count += 1
    word_list.append(word)
print(f"The total number of words in the paragraph is: {word_count}")
print("The words in the paragraph are: ", len(word_list))
