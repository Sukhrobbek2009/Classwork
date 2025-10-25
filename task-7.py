groceries =["milk", "bread", "eggs", "chees"]

try:
    product = input("Which product would you like to buy? ").strip().lower

    if product in groceries:
        groceries.remove(product)
        product(f"User bought {product}")
    else:
        print('Not in the list.')

    print("Upate list:", groceries)

except Exception as e:
    print('An error occurred:', e)