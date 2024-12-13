# Exercise 16: Does it contain vowels

word = input("Type in a word: ")

vowel_a = word.count("a") > 0
vowel_o = word.count("o") > 0
vowel_e = word.count("e") > 0

if vowel_a:
    print("a found.")
else:
    print("a not found.")

if vowel_o:
    print("o found.")
else:
    print("o not found.")

if vowel_e:
    print("e found.")
else:
    print("e not found.")
