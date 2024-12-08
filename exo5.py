# Exercise 5: Determine the Oldest Age

f_person = int(input("First person's age: "))
s_person = int(input("Second person's age: "))

if f_person > s_person:
    print("The first person's older.")
elif f_person < s_person:
    print("The second person's older.")
else:
    print("They are the same age.")
