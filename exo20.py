# Exercise 20: Unique Word Counter

unique_words = {""}
duplicate = False
unique_words.remove("")

while not duplicate:
    word = input("Type in a word: ")

    if word in unique_words:
        duplicate = True
    else:
        unique_words.add(word)

print(f"You typed {len(unique_words)} unique words.")
