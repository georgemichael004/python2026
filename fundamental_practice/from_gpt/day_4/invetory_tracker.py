# Task: Track inventory items, stock changes, and totals.
inventory = {'apples': 10, 'bananas': 5}

while True:
    print("\nInvetory Menu:")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        print("\nCurrent Stock")
        for item, quantity in inventory.items():
            print(f"-{item.capitalize()}: {quantity}")
    
    if choice == '2':
        item = input("Enter item name: ").lower()
        try:
            quantity = int(input("Enter quantity for {item}: "))
            if quantity > 0:
                inventory[item] = quantity
                print(f"Updated {item} quantity to {quantity}.")
            elif quantity == 0:
                if item in inventory:
                    del inventory[item]
                    print(f"Removed {item} from inventory.")
                else:
                    print("Item not found to remove.")
        except ValueError:
            print("Invalid quantity entered. Please use a whole number.")

    elif choice == '3':
        print("Exiting invetory Tracker.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

