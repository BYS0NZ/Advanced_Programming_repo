# Exercise 14: Underline

word = input("Please type in a string: ")

while word != "":
    print("\x1B[4m" + word + "\x1B[0m")
    word = input("Please type in a string: ")
