# Exercise 13: Rectangle of hashes

width = int(input("Enter the width of the hash rectangle: "))
height = int(input("Enter the height of the hash rectangle: "))
h = "#"
for i in range(height):
    print(h * width)
