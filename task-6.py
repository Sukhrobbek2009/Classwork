price = 5

age = int(input('Enter your age : '))

if age < 18:
    discount = 5 * 20 / 100
    price = 5 - discount
    print(f"The price to you discount {price}")
elif age > 60:
    discount = 5 * 50 / 100
    price = 5 - discount
    print(f'The price to you 50% discount is ${price}')
else:
    print(f"No discount.The price to you is ${price}")


      