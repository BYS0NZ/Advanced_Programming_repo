# Exercise 8: Leap Year Exercise

year = int(input("Enter a year: "))

if year % 4 == 0:
    print(f"{year} is a leap year.")
elif year % 100 == 0 and year % 400 == 0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is NOT a leap year.")
