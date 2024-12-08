# Exercise 6: Determine the Faster Runner

r1 = input("Runner 1 name: ")
r2 = input("Runner 2 name: ")
t1 = float(input(f"{r1}'s time: "))
t2 = float(input(f"{r2}'s time: "))

if t1 < t2:
    print(f"{r1} is champ !")
elif t1 > t2:
    print(f"{r2} is champ !")
else:
    print("They both did great.")
