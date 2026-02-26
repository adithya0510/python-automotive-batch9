numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 0

# while loop
while i < len(numbers):
    num = numbers[i]
    i += 1

    # if condition
    if num == 3:
        print("Skipping 3")
        continue      # skips rest of loop for this iteration

    # elif condition
    elif num == 7:
        print("Breaking at 7")
        break         # exits the loop completely

    # else condition
    else:
        print("Processing", num)

# for loop
for n in numbers:
    if n % 2 == 0:
        print(n, "is even")
    else:
        print(n, "is odd")
