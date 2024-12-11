# Exercise11: Palindrome Checker

word = input("Type in a word: ")

is_palindrome = True

for i in range(0, len(word)):
    if word[i] != word[-i]:
        is_palindrome = False
        break

if is_palindrome:
    print(f"Yes, {word} is palindrome.")
else:
    print(f"No, {word} is Not palindrome.")

