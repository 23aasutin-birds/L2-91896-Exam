# Collects user informaiton
def user_information(user_dictionary):
    user_dictionary["Name"] = input("Name: ")
    user_dictionary["Email"] = input("Email: ")
    user_dictionary["Number"] = input("Phone Number: ") # Doesn't like the numbers starting with 0, change to start with "64"
    return user_dictionary

# Collects order
def ordering_information(user_dictionary):
    menu_items = {
        "Dalh with rice" : ["M", "V", "VE", "GF", "DF"],
        "Risoto" : ["M", "V", "GF"],
        "Tagine" : ["M", "V", "VE", "GF", "DF"],
        "Lasagna" : ["M", "V"]
    }

    while True:
        print("Food items avalibles:")
        
        number = 1
        for item in menu_items: # Extracts food items from meun_items (eg, "Dalh with Rice", "Risoto" etc.)
            options = ""
            for option in menu_items[item]: # Extracts the next option in the values lists  (eg, "V", "VE", etc.)
                options =  options + ", " + option # Added all previously extracted options, a ", " and the new options
            
            print(f"    {number}. {item} ({options[2:]})") # String splice removes extra ", " for the start of the options string
            number += 1
        
        print(f"Or:\n   {number}. Save & Continue")
        input("> ")


            



        break

# Devlivery/pick up information
def delivery_infromation(user_dictionary):
    print("Would you like to:" \
    "1. Pick Up" \
    "2. Delivered")
    user_answer = input("> ")

    if user_answer == "1":
        user_dictionary["Delivery"] = False
    if user_answer == "2":
        user_dictionary["Delivery"] = True
        user_dictionary["Adress"] = input("Delivery Address: ")
    else:
        print("Please enter either '1' or '2'.")
    
    return user_dictionary

# Recipt
def print_recipt(user_dictionary):
    for item in user_dictionary:
        print(f"{item}: {user_dictionary[item]}") # Check if value is a dictionary so that you can print it acordingingly

# Cancellation/confirmation
def order_confirmed():
    print("Confirm order:" \
    "a. Confirm" \
    "b. Cancal")
    user_answer = input("> ")
    if user_answer == "a":
        return True
    if user_answer == "b":
        return False
    else:
        print("Please enter either 'a' or 'b'.")

# Main menu
def main_menu():

    order_number = {
        "Name" : "Audrey Austin",
        "Email" : "audrey.c.austin@gmail.com",
        "Number" : 642040326799,
        "Tagine" : {
            "V" : 2,
            "M" : 1
            },
        "Pizza" : {
            "V" : 1,
            "M" : 1
            }
    }

    all_orders = {
        145 : order_number
    }

    while True:

        temp_dic = {}

        print("Welcome to Mountain Meals!" \
        "Here you can easily order tasty food.")

        print("1. Personal Information")
        temp_dic = user_information(temp_dic)

        print("2. Pick your food")
        ordering_information(temp_dic)

        print("3. Delivery/Pick Up Information")
        # temp_dic = delivery_infromation(temp_dic)

        print("4. Confirm Order")
        print_recipt(temp_dic)
        if order_confirmed():
            number = 1 # Generate random number
            all_orders[number] = temp_dic
            print("Thanks for coming to Mountain Meals! We hope you enjoy your food.")
        else:
            print("Your order has been cancalled! We hope you come to Mountain Meals in the future.")

main_menu()