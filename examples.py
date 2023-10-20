cart = {}

item = input("What would you like to add? ")
print(item)
quantity = int(input("How many would you like to add?"))
print(quantity)

cart[item] = quantity
print(cart)

while True: #this is going to run until i give it a break condition
    item = input("What would you like to add? (Yes/No)")
    print(item)
    quantity = int(input("How many would you like to add?"))
    print(quantity)
    
    cart[item] = quantity
    print(cart)

while True: #this is going to run until i give it a break condition
    item = input("What would you like to add? ")
    print(item)
    quantity = int(input("How many would you like to add?"))
    print(quantity)
    
    if item not in cart:
        cart[item] = quantity
    else:
        cart[item] += quantity
    print(cart)
    