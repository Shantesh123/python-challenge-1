# Menu dictionary
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
place_order = True
menu_dashes = "-" * 5
orders_list=[]
orders_dashes = "-" * 42
# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to view different sections of the menu, so let's create a 
# continuous loop
# while True:
#     # Ask the customer which menu category they want to view
#     print("Which menu would you like to view? ")

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

    # # Get the customer's input
    # menu_category = input("Enter menu number to : ")

    # Exit the loop if user typed 'q'

    # Check if the customer's input is a number
    # if menu_category.isdigit():
    #     # Check if the customer's input is a valid option
    #     if int(menu_category) in menu_items.keys():
    #         # Save the menu category name to a variable
    #         menu_category_name = menu_items[int(menu_category)]
    #         # Print out the menu category name they selected
    #         print(f"You selected {menu_category_name}")

    #         # Display the heading for the sub-menu
    #         print(menu_dashes)
    #         print(f"This is the {menu_category_name} menu.")
    #         print(menu_dashes)
    #         print("Item # | Item name                | Price")
    #         print("-------|--------------------------|-------")

            # Initialize a menu item counter
item_counter = 1
            # Print out the menu options from the menu_category_name
for key, value in menu.items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    # Iterate through the dictionary items
                    for key2, value2 in value.items():
                        # Print the menu item
                        if type(value2) is dict:
                             for key3, value3 in value2.items():  
                                num_item_spaces = 24 - len(key + key2 + key3) - 3
                                item_spaces = " " * num_item_spaces
                                print(f"{item_counter}      | "
                                    + f"{key} - {key2}-{key3}{item_spaces} | "
                                    + f"${value3}")
                                orders_list.append({
                                "Item number" : item_counter,
                                "Item name": key2 + "-" + key3,
                                "Price": value3,
                                })
                                item_counter += 1
                        else:
                            num_item_spaces = 24 - len(key + key2) - 3
                            item_spaces = " " * num_item_spaces
                            print(f"{item_counter}      | "
                                    + f"{key} - {key2}{item_spaces} | "
                                    + f"${value2}")
                        # Add 1 to the item_counter
                            orders_list.append({
                                        "Item number" : item_counter,
                                        "Item name": key2,
                                        "Price": value2,
                                            })
                        item_counter += 1
                else:
                    # Print the menu item
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{item_counter}      | "
                          + f"{key}{item_spaces} | ${value}")
                    # Add 1 to the item_counter
                    item_counter += 1
                    orders_list.append({
                        "Item number": item_counter,   
                        "Item name": key,
                        "Price": value,
                        })
                    


customer_order_list=[]
price_list=[]

for items in orders_list:
     print(items)

customer_menu_input = input("select item # from the menu :" )
customer_quantity = int(input('Enter the quanity: ') or 1)
customer_quantity = customer_quantity if customer_quantity != 0 else None 
print(customer_quantity)



for item_orders in orders_list:

     # 3. Check if the customer typed a number
   
    if isinstance(int(customer_menu_input), int):
                # Convert the menu selection to an integer
        # print(customer_menu_input)
        customer_menu_input=int(customer_menu_input)
        customer_ticker = item_orders["Item number"]
        customer_item_name = item_orders["Item name"]
        # print(customer_item_name)
        # print(customer_ticker)
        customer_price = item_orders["Price"] 
        # print(customer_price)
                    #Store the item name as a variable
        if int(customer_menu_input) is int(customer_ticker):
            customer_order_list.append({   
                        "Item name": customer_item_name,
                        "Price": customer_price,
                        "Quantity" : customer_quantity,
                        })
            price_list.append(customer_price)
            item_counter += 1
        else:
        
            # print(f"{customer_menu_input} was not part of menu")  
            item_counter += 1
        #Ask the customer for the quantity of the menu item
    else:
        print(f"{customer_menu_input} was not a appropriate number") 

        
while place_order:

    # while True:
        # Ask the customer if they would like to order anything else
     
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")
        customer_menu_input = input("select item # from the menu :" )
        customer_quantity = int(input('Enter the quanity: ') or 1)
        customer_quantity = customer_quantity if customer_quantity != 0 else None 
        match keep_ordering.lower():
            # Customer chose yes
            case 'y':
                    for item_orders in orders_list:
     # 3. Check if the customer typed a number
                        if isinstance(int(customer_menu_input), int):
                # Convert the menu selection to an integer
        # print(customer_menu_input)
                            customer_menu_input=int(customer_menu_input)
                            customer_ticker = item_orders["Item number"]
                            customer_item_name = item_orders["Item name"]
        # print(customer_item_name)
        # print(customer_ticker)
                            customer_price = item_orders["Price"] 
        # print(customer_price)
                    #Store the item name as a variable
                            if int(customer_menu_input) is int(customer_ticker):
                                    customer_order_list.append({   
                                    "Item name": customer_item_name,
                                    "Price": customer_price,
                                    "Quantity" : customer_quantity,
                                    })
                                    price_list.append(customer_price)
                                    item_counter += 1
                            else:       
                            # print(f"{customer_menu_input} was not part of menu")  
                                item_counter += 1
        #Ask the customer for the quantity of the menu item
                        else:
                            print(f"{customer_menu_input} was not a appropriate number") 
                # Exit the keep ordering question loop
                    #place_order = True
            # Customer chose no
            case 'n':
                # Complete the order
                    place_order = False
                # Since the customer decided to stop ordering, thank them for their order
                    print("Thank you for your order.")
                # Exit the keep ordering question loop
                    break
            # Customer typed an invalid input
            case _:
                # Tell the customer to try again
                print("I didn't understand your response. Please try again.")
                    

# # Print out the customer's order
print("This is what we are preparing for you.\n")
for customers_orders in customer_order_list:
    print (customers_orders)
# # Uncomment the following line to check the structure of the order

# print(orders_list)
i=1 
# menu_items = {}
print("Item name                       | Price  | Quantity")
print("--------------------------------|--------|--------")
# 6. Loop through the items in the customer's order
for customers_orders in customer_order_list:
                        
                        cust_item_name = customers_orders["Item name"]
                        cust_item_price = customers_orders["Price"]
                        cust_item_quant = customers_orders["Quantity"]
                        num_item_spaces = 32 - len(cust_item_name)
                        price_spaces = 12 -len(cust_item_name)
                        price_spaces_list= " " * price_spaces
                        item_spaces = " " * num_item_spaces
 # 9. Create space strings
                        print(f"{cust_item_name}{item_spaces}|{cust_item_price}    |{cust_item_quant}")

    # 10. Print the item name, price, and quantity


# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
tuple_cust = [(customer_order_list["Price"] * customer_order_list["Quantity"]) for customer_order_list in customer_order_list]

print(f"here are the individual total prices for items {tuple_cust}\n")

# Use a list comprehension to calculate the total number of adult guests
total_cust_bill = sum([tuple_cust for tuple_cust in tuple_cust])

print(f"Total bill for you today is : {total_cust_bill}")
