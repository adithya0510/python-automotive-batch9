try:
    # Read the length of the list as input (string)
    num = input()
    
    # Check whether the input for n is numeric
    if not num.lstrip('-').isdigit():
        # If n is not numeric, print error and terminate
        print("Error: You must enter a numeric value.")
        exit()

    # Convert n from string to integer
    num = int(num)

    # Check if the length of the list is non-negative
    if num < 0:
        # Negative length is not allowed
        print("Error: The length of the list must be a non-negative integer.")
        exit()

    # Initialize an empty list to store integers
    integer_list = []

    # Read each element of the list
    for i in range(num):
        input_list = input()
        
        # Check if the element is numeric
        # lstrip('-') allows negative integers (e.g., -10)
        if not input_list.lstrip('-').isdigit():
            # If a non-numeric value is entered, print error and exit
            print("Error: You must enter a numeric value.")
            exit()
        
        # Convert the valid input to integer and add to the list
        integer_list.append(int(input_list))

    # Calculate the average of the list
    if num == 0:
        # If the list is empty, set average to 0.00
        average = 0.00
    else:
        # Calculate average normally
        average = sum(integer_list) / num

    # Print the average rounded to two decimal places
    print(f"{average:.2f}")

except Exception:
    # Handle any unexpected runtime errors
    print("Error: You must enter a numeric value.")
