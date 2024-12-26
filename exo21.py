# Exercise 21: Sorted List Builder

user_list = []
while True:
    try:
        number = int(input("Enter a number (0 to stop): "))

        if number == 0:
            print("Exiting the program. Goodbye!")
            break

        user_list.append(number)
        print(f"Current List: {user_list}")
        print(f"Sorted List: {sorted(user_list)}")

    except ValueError:
        print("Please enter an integer.")
