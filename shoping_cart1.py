shopping_cart = {}

def add_item():
    item = input("Enter the item you want to add: ")
    shopping_cart[item] = quantity
    print(shopping_cart)

    quantity = int(input("Enter the quantity: "))
    if item in shopping_cart:
        shopping_cart[item]+=quantity
    else:
        shopping_cart[item]=quantity
    print(f"{quantity} {item} (s) added to the shopping cart.")

def remove_item():
    item = input("Enter the item you to remove: ")
    if item in shopping_cart:
        quantity = int(input("Enter the quantity to remove: "))
        if quantity >= shopping_cart[item]:
            del shopping_cart[item]
            print(f"All {item} remove from the shopping cart.")
        else:
            shopping_cart[item] -= quantity
            print(f"{quantity} {item} (s) removed from the shopping list.")
    else:
        print(f"{item} is not in the shopping cart.")
    
    def show_list():
        print("shopping_cart:")
        for item, quantity in shopping_cart.items():
            print(f"{item}: {quantity}")

    while True:
        print("option:")
        print("1: Add an item")
        print("2: Remove an item")
        print("3: Show the shoppin list")
        print("4: Quit")

        user_choice = input("Enter your choice: ")

        if user_choice == "1":
            add_item()

        if user_choice == "2":
            add_item()
        
        if user_choice == "3":
            add_item()

        if user_choice == "4":
            print("Your final shopping list:")
            show_list()
            break

        else:
            print("Invalid option. Please choose a valid option (1, 2, 3, or 4).")
        
        print("Thank you for shopping!")