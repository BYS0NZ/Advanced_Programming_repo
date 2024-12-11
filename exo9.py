# Exercise 9: FizzBuzz Exercise

number = int(input("Type in an Integer: "))

is_div_by3 = number % 3 == 0
is_div_by5 = number % 5 == 0

if is_div_by3 and not is_div_by5:
    print("Fizz")
elif not is_div_by3 and is_div_by5:
    print("Buzz")
elif is_div_by3 and is_div_by5:
    print("FizzBuzz")
