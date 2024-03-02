# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
## Create an empty list. This list will later store a customer's order in dictionary format, as follows:
# Asked BCS learning assistant questions to get an idea of how to understand the workflow

order_list = []
print("order_list", order_list)

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.") 

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number to view or q to quit: ")
    #print(f"How many of the  {menu.menu_items} item would you like to order?")

    # Exit the loop if user typed 'q'
    if menu_category == 'q':
        break

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            menu_selection = input("Please enter the number of the menu item you would like to select:")


            # 3. Check if the customer typed a number
            if menu_selection.isdigit():
                            

                # Convert the menu selection to an integer
                menu_selection = int(menu_selection)


                # 4. Check if the menu selection is in the menu items
                if menu_selection in menu_items.keys():

                    # Store the item name as a variable
                    item_name = menu_items[menu_selection]["Item name"]


                    # Ask the customer for the quantity of the menu item
                    quantity = input(f"How many {item_name} would you like to order? (Default is 1): ")


                    # Check if the quantity is a number, default to 1 if not
                    if quantity.isdigit():
                        quantity = int(quantity)
                    else:
                        quantity = 1

                        # Tell the customer that their input isn't valid
                        print("Invalid quantity input. Defaulting to 1.")


                    # Add the item name, price, and quantity to the order list
                    order_list.append({
                        "Item name": item_name,
                        "Price": menu_items[menu_selection]["Price"], 
                        "Quantity": quantity})
                else:

                    # Tell the customer they didn't select a menu option
                    print("You didn't select a valid menu option.")
                             
            else:
                    # Tell the customer they didn't select a menu option
                    print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

       
    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input
        if keep_ordering.lower() == 'y':

            # Keep ordering
            break

        elif keep_ordering.lower() == 'n':                       
            # Complete the order
            print("Order completed.")

            # Since the customer decided to stop ordering, thank them for
            # their order
            print("Thank you for your order.")
            # Exit the keep ordering question loop
            place_order = False
            break
        
        else:     
            # Tell the customer to try again
            print("Please enter a valid input (Y for Yes, N for No).")

  
# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order_list)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Create a for loop to loop through the order list.
for item in order_list:
    
    # 7. Store the dictionary items as variables
    #for item in order_list:
    item_name = item['Item name']
    price = item['Price']
    quantity = item['Quantity']

    #print(order_list)

    # Perform operations using the stored variables
    #print(f"Item Name: {item_name}, Price: {price}, Quantity: {quantity}")

   
    # 8. Calculate the number of spaces for format
    # ted printing
    max_item_name_length = max(len(item['Item name']) for item in order_list)
    max_price_length = max(len(str(item['Price'])) for item in order_list)
    max_quantity_length = max(len(str(item['Quantity'])) for item in order_list)

    total_spaces = max(max_item_name_length, len("Item Name")) + max(max_price_length, len("Price")) + max(max_quantity_length, len("Quantity")) + 10

    #print(f"Total Spaces Required: {total_spaces}")
        
    # 9. Create space strings
    #space_string = " " * total_spaces
    space_string_item_name = " " * (max_item_name_length - len(item_name))
    space_string_price = " " * (max_price_length - len(str(price)))
    space_string_quantity = " " * (max_quantity_length - len(str(quantity)))

    #print(f"|{space_string}|")  # Print a line with the calculated spaces

    # 10. Print the item name, price, and quantity
    
    print(item_name, price, quantity)
    #print(item_name[max_item_name_length], price[max_price_length], quantity[max_quantity_length])

    #for item_name, price, quantity in order_list(item[item_name],item[price],item[quantity]"):
    #print(f"{item_name:{max_item_name_length}} {price:{max_price_length}.2f} {quantity:{max_quantity_length}}")

    # for item in order_list:
    #     item_name = item['Item name']
    #     price = item['Price']
    #     quantity = item['Quantity']
    #     print(f"{item_name:{max_item_name_length}} {price:{max_price_length}.2f} {quantity:{max_quantity_length}}")

    #print(f"Item Name: {item_name}{space_string_item_name}, Price: {price}{space_string_price}, Quantity: {quantity}{space_string_quantity}")
   

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
total_cost = sum(item['Price'] * item['Quantity'] for item in order_list)
print(f"Total Cost of the Order: ${total_cost:.2f}")