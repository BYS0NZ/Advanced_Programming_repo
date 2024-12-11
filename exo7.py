# Exercise 7: Separating Dinars and Centimes

price = float(input("Type in a price: "))

int_price = int(price)
dec_price = int(float(price - int_price)*100)

print(f"Dinars: {int_price}")
print(f"Centimes: {dec_price}")
