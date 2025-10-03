menu = {
    'Pizza' : 40,
    'Pasta' : 50,
    'Burger' : 60,
    'Salad' : 70,
    'Coffee' : 80,
}

# Display a welcome message and show the menu to the user
print("Welcome to Akram's Restaurant")
print("Menu:")
for item, price in menu.items():
    print(f"- {item} : Rs{price}")

# Initialize total bill and list to store ordered items
order_total = 0
ordered_items = []

while True:
    item = input("\nEnter the name of the item you want to order (or type 'exit' to finish): ").strip()
    
    if item.lower() == 'exit':
        break  # Exit the loop and proceed to order summary
    
    # Check if the entered item is available in the menu
    elif item in menu:
        order_total += menu[item]           # Add item price to total
        ordered_items.append(item)          # Add item to the list of ordered items
        print(f"Your item '{item}' has been added to your order.")
    
    # If item is not found in the menu, show an error message
    else:
        print(f"Sorry, '{item}' is not available on the menu.")

# Display the final order summary after exiting the loop
print("\nOrder Summary:")
if ordered_items:
    print("Items ordered:", ", ".join(ordered_items))  # Show all ordered items
    print(f"Total amount to pay: Rs{order_total}")     # Show total bill
else:
    print("No items were ordered.")  # Inform user if nothing was ordered