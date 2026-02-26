# Fixed number that the user has to guess
fixed_number = 10

# To count how many attempts the user makes
total_attempts = 0

while True:    # This loop will run until the correct number is guessed
    guess = int(input("guess the number:"))   # take user input to guess the number
    total_attempts += 1  # increase the count by one everytime the user guess a number
    
    if guess == fixed_number:
        print(f"Congratulations!!! You have guessed correct. You took {total_attempts} attempts" )
        break  # stops the loop when guessed correct and execution is stopped