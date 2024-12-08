# Exercise 4: Discount Calculation

amount = float(input("Amount : "))
nb_items = int(input("How many items :"))
day = input("sorry, remind me of the day please: ")

if day == "Saturday" or day == "Sunday":
    amount -= amount*0.2
else:
    amount -= amount*0.1
if nb_items >5:
    amount -= amount * 0.05

print(f"That would be {amount}$ please.")
