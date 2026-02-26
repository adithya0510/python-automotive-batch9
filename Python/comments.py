products = ["Shoes", "Bag", "Watch", "T-Shirt", "Jeans", "Perfume"]
prices = [1200, 800, 500, 300, 900, 450]

cart = []
cart_prices = []

print("Available Products:")
for i in range(len(products)):
    print(i, "-", products[i], "₹", prices[i])

while True:
    choice = input("Enter product number to add or 'done' to stop: ")

    if choice.lower() == "done":
        break

    choice = int(choice)
    cart.append(products[choice])
    cart_prices.append(prices[choice])

    print(products[choice], "added to cart")


while True:
    print("Your cart items:")
    for i in range(len(cart)):
        print(i, "-", cart[i], "₹", cart_prices[i])

    remove_item = input("Do you want to remove any item? (yes/no): ")

    if remove_item.lower() == "yes":
        remove_index = int(input("Enter item number to remove: "))
        cart.pop(remove_index)
        cart_prices.pop(remove_index)
        print("Item removed")
        continue

    proceed = input("Do you want to proceed with bill? (yes/no): ")

    if proceed.lower() == "yes":
        print("Final Cart Items:")
        for item in cart:
            print(item)
        break
    else:
        print("Back to cart modification")


total = sum(cart_prices)
print("Total Amount =", total)

if total > 500:
    discount = total * 0.10
    total = total - discount
    print("Discount Applied")
    print("Pay =", total)
else:
    print("No discount applied")
    print("Pay =", total)

print("Thank you for visiting!")