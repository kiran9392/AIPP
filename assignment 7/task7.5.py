numbers = [10, 20, 30]

try:
    index = 4
    print("Accessing element at index", index, ":", numbers[index])
except IndexError:
    print(f"Error: Index {index} is out of range. The list has {len(numbers)} elements.")
