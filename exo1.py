# Exercise 1: Calculating Taxi Rides

nb_persons = int(input("How many people want to travel ?"))
taxi_fit = int(input("How many people can fit in those cars ?"))

nb_cars = nb_persons // taxi_fit

if nb_persons % taxi_fit != 0:
    nb_cars += 1

print(f"You'll need {nb_cars} for them")
