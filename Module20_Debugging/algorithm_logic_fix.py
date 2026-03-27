# Find maximum number in list

numbers = [10, 25, 5, 40, 15]

max_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num

print("Maximum:", max_num)