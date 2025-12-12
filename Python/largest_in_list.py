numbers = [12, 45, 7, 81, 23, 56]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("The largest number in the list is", largest)

