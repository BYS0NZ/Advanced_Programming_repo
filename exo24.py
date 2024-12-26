# Exercise 24: From negative to positive

try:
    N = int(input("Enter a positive integer: "))

    if N <= 0:
        print("Please enter a positive integer.")
    else:
        for i in range(-N, N + 1):
            if i != 0:
                print(i)
except ValueError:
    print("Invalid input. Please enter an integer.")
