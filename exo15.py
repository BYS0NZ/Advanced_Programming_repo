# Exercise 15: Framed word

word = input("Type in a word to see the magic happen: ")
star = "*"
padding = (28 - len(word))/2

print(star * 30)
print("*" + " "*int(padding) + word + " "*int(padding) + "*")
print(star * 30)
