

def add_item(shopping_cart, item):
    # adds an item to the shopping cart.

    # args:
        # shopping_cart: a dictionary representing the shopping cart.
        # item: item to add to the shopping cart.

    if item in shopping_cart:
        shopping_cart[item]+=1
    else:
        shopping_cart[item]=1 
    
def remove_item(shopping_cart, item):
    # removes an item to the shopping cart.

    # args:
        # shopping_cart: a dictionary representing the shopping cart.
        # item: item to remove to the shopping cart.
    if item in shopping_cart:
        if shopping_cart[item] == 1:
            del shopping_cart[item]
        else:
            shopping_cart[item]-=1

def print_shopping_cart(shopping_cart):
    # print the shopping cart.

    # args:
        # shopping_cart: a dictionary representing the shopping cart.
    print("Shopping_cart:" )
    for item, quantity in shopping_cart.items():
        print(f"{item}: {quantity}")

def main():
    shopping_cart = {}

    while True:
        choice = input("what would you like to do? (add, remove, view, quit): ")
    
        if choice == "add":
            item = input("what item would you like to add?: ")
            add_item(shopping_cart, item)
        elif choice == "remove":
            item = input("what item would you like to remove?: ")
            remove_item(shopping_cart, item)
        elif choice == "view":
            print_shopping_cart(shopping_cart)
        elif choice == "quit":
            break
main()


    




