# List of the available products and their prices
products = ["Shoes", "Bag", "Watch", "T-Shirt", "Jeans", "Perfume"]
prices = [1200, 800, 500, 300, 900, 450]

# The empty lists to store cart items and their prices
cart = []
cart_prices = []

# Display available products with index and price
print("Available Products:")
for i in range(len(products)):
    print(i, "-", products[i], "₹", prices[i])

# Loop to add products to cart
while True:
    choice = input("Enter product number to add or 'done' to stop: ")

    if choice.lower() == "done":
        break

    # Converting input to integer 
    choice = int(choice)

    # Adding selected product and its price to cart
    cart.append(products[choice])
    cart_prices.append(prices[choice])

    print(products[choice], "added to cart")

# Loop to view and modify the cart
while True:
    remove_item = input("Do you want to remove any item? (yes/no): ")
                        
    if remove_item.lower()   == "no":                 
         print("Final cart items:") 
         for item in cart:
             print(item)             
         break 
                 
    print("Your cart items:")
    for i in range(len(cart)):
        print(i, "-", cart[i], "₹", cart_prices[i])

    # Asking if the user wants to remove an item
    remove_item = input("Do you want to remove any item? (yes/no): ")

    if remove_item.lower() == "yes":
       remove_index = int(input("Enter item number to remove: "))

    # Remove the item and its price from cart
    cart.pop(remove_index)
    cart_prices.pop(remove_index)
    print("Item removed")
    continue

    # Ask the user if they want to proceed with billing
    proceed = input("Do you want to proceed with bill? (yes/no): ")

    if proceed.lower() == "yes":
        print("Final Cart Items:")
        
        # Displaying final items
        for item in cart:
            print(item)
        break
    else:
     print("Back to cart modification")

# Calculating total bill amount
total = sum(cart_prices)
print("Total Amount =", total)

# Applying 10% discount if total is more than 500
if total > 500:
    discount = total * 0.10
    total = total - discount
    print("Discount Applied")
    print("Pay =", total)
else:
    print("No discount applied")
    print("Pay =", total)

# Displays the polite message at the end
print("Thank you for visiting!")