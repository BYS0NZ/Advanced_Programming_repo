# Exercise 17: Mutability in Lists

numbers = [1, 2, 3, 4, 5]
value = int(input("Enter a value: "))
index = int(input("Enter and index( -1 to quit ): "))

if index < len(numbers):
    while index != -1:
        numbers[index] = value
        print(numbers)
        print(len(numbers))

        value = int(input("Enter a value: "))
        index = int(input("Enter and index( -1 to quit ): "))
else:
    print("Your index is out of range")

print("Quit.")
