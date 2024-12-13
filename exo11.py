# Exercise11: Palindrome Checker

word = input("Type in a word: ")
word.lower()

is_palindrome = True
i = 0
j = len(word)-1

while i < j:
    if word[i] != word[j]:
        is_palindrome = False
        break
    i += 1
    j -= 1

if is_palindrome:
    print(f"Yes, {word} is palindrome.")
else:
    print(f"No, {word} is Not palindrome.")
