# Exercise 22: List Statistics

numbers = [1, 2, 3, 4, 5]

print(f"Length: {len(numbers)}")

if len(numbers) > 0:
    mean = sum(numbers) / len(numbers)
    print(f"Mean: {mean}")
else:
    print("Can't calculate Mean (empty list)")

if len(numbers) > 0:
    range_list = max(numbers) - min(numbers)
    print(f"Range: {range_list}")
else:
    print("Can't calculate Range (empty list)")
