# Exercise 19: Interactive List Operations

numbers = [1, 2, 3, 4, 5]

print(f"The list : {numbers}")
print("Menu:")
print("[ 1 ] Append")
print("[ 2 ] Insert")
print("[ 3 ] Pop")
print("[ 4 ] Remove")
print("[ 5 ] Quit")

option = int(input("Choose an option: "))
want_to_quit = False

if 0 < option <= 5:
    while option != 5 and not want_to_quit:
        if option == 1:
            value = int(input("Enter a value to append: "))
            numbers.append(value)
            print(numbers)
        elif option == 2:
            value = int(input("Enter a value to insert: "))
            index = int(input("Enter a valid position to insert: "))
            numbers.insert(index,value)
            print(numbers)
        elif option == 3:
            numbers.pop()
            print(numbers)
        elif option == 4:
            value = int(input("Enter a value to remove: "))
            numbers.remove(value)
            print(numbers)
        elif option == 5:
            print(numbers)
            print("Quitting ..")
            want_to_quit = True
        else:
            print("Invalid option, try again")

        option = int(input("Choose an option: "))
else:
    print("Invalid option, try again")

print("You've quit.")
