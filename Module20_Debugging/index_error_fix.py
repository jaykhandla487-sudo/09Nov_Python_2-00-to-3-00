numbers = [10, 20, 30]

try:
    print(numbers[2])
except IndexError:
    print("Index out of range")