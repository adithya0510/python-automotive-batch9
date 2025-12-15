# Stores product names as keys and their prices as values
products = {
    "Clock": 350,
    "Lamp": 470,
    "Bag": 600,
    "Bottle": 150
}

# Here we make an empty List used to store items
cart = []

# It Runs continuously to show menu until the user exits
while True:
    print("\n--- Product List ---")

    # Display all the available products along with prices
    for item, price in products.items():
        print(item, ":", price)

    # selecting an options by the user
    print("\n1. Add item")
    print("2. Remove item")
    print("3. View cart & total")
    print("4. Exit")

    # user should make a choice in the available products to add to cart
    choice = int(input("Enter your choice: "))

    # Adding selected item to cart
    if choice == 1:
        item = input("Enter item name to add: ")
        if item in products:
            cart.append(item)
            print(item, "added to cart")
        else:
            print("Item not found")

    # Removing item from cart if it exists
    elif choice == 2:
        item = input("Enter item name to remove: ")
        if item in cart:
            cart.remove(item)
            print(item, "removed from cart")
        else:
            print("Item not in cart")

    # Displaying cart items, calculating total, and applies discount
    elif choice == 3:
        total = 0
        print("\nItems in cart:")

        # Calculates total price of all items in the cart
        for item in cart:
            print(item, "-", products[item])
            total += products[item]

        print("Total amount:", total)

        # Applies 10% discount if total amount exceeds 500
        if total > 500:
            discount = total * 0.10
            total -= discount
            print("Discount applied: 10%")
            print("Amount after discount:", total)

    # Exits the program when user chooses exit option
    elif choice == 4:
        print("Thank you for shopping!")
        break

    # Handles invalid menu inputs
    else:
        print("Invalid choice")