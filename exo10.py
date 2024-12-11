# Exercise 9: Name Length Kingdom

cities_pop = {}
city_name = ""

while city_name != "stop":
    city_name = input("Type a city name: ")
    if city_name == "stop":
        break
    cities_pop.update({city_name: len(city_name) * 1000000})

print(cities_pop)
print(sorted(cities_pop.items(), key=lambda population: population[1], reverse=True))
