def input_validation(question):
    while True:
        try:
            user_answer = int(input(question))
            return user_answer
        except ValueError:
            print("Please enter an integer not only spaces, nothing or text. Try again.")

def string_validation(question, is_lower = True):
    while True:
        user_answer = input(question).strip()
        if user_answer == "":
            print("Please enter some text.")
            continue
        
        if is_lower:
            return user_answer.lower() # for most input validation
        
        else:
            return user_answer.capitalize() # for names

def email_validation(question):
    while True:
        user_answer = input(question).strip()

        if user_answer == "":
            print("Please enter a valid email adress.")
            continue

        if "@" in user_answer and user_answer[-1].isalpha(): # If @ present in email adress and last character is a letter considered valid email
            return user_answer
        else:
            print("Please enter a valid email adress.")

def phone_validation(question):
    LONGEST_NUMBER = 11 # So length can be changes easily in the future if regulations change
    SHORTEST_NUMBER = 9
    
    while True:
        user_answer = string_validation(question) # Regular validation
        try:
            user_answer = int(user_answer) # Attemps to convert to string
            
            if user_answer >= SHORTEST_NUMBER and user_answer <= LONGEST_NUMBER: # Checks for valid lenth (in NZ)
                return f"+64{user_answer}"
            
            else: # If outside valid range
                print("Phone numbers must be between 7 and 9 digits long.")
        
        except ValueError: # If not 100% integers
            print("Please enter a valid phone number will integers only.")




# Collects user informaiton
def user_information(user_dictionary):
    user_dictionary["Name"] = string_validation("Name: ")
    user_dictionary["Email"] = email_validation("Email: ")
    user_dictionary["Number"] = phone_validation("Phone Number: +64") # Doesn't like the numbers starting with 0, change to start with "64"
    return user_dictionary

def print_food_menu(menu):
    number = 1
    for item in menu: # Extracts food items from meun_items (eg, "Dalh with Rice", "Risoto" etc.)
        
        options = ""
        for option in menu[item]: # Extracts the next option in the values lists  (eg, "V", "VE", etc.)
            options =  options + ", " + option # Added all previously extracted options, a ", " and the new options
        
        print(f"    {number}. {item} ({options[2:]})") # String splice removes extra ", " for the start of the options string
        number += 1
    
    print(f"Or:\n   {number}. Save & Continue")

    return number

def print_food_options(menu, key):
    number = 1
    for option in menu[key]:
        print(f"    {number}. {option}")
        number += 1
    
    print(f"Or:\n   {number}. To Main Menu")

    return number

def index_to_key(items, user_answer):
    list_of_items = list(items.keys()) # Converts the number to the key associated with it
    return list_of_items[user_answer - 1]

# Collects order
def ordering_information(user_dictionary):
    menu_items = {
        "Dalh with rice" : ["M", "V", "VE", "GF", "DF"],
        "Risoto" : ["M", "V", "GF"],
        "Tagine" : ["M", "V", "VE", "GF", "DF"],
        "Lasagna" : ["M", "V"]
    }

    for item in menu_items:
        user_dictionary[item] = {}

    while True:

        print("Food items avalibles:")

        continue_number = print_food_menu(menu_items) # prints all food items, returns the number associated with the "Save & Continue" option
        user_answer = int(input("> "))

        if user_answer > 0 and user_answer < continue_number: # View a food item
            
            item = index_to_key(menu_items.key(), user_answer) # Convert index to key (for later use)

            while True:
                back_number = print_food_options(menu_items, item) # Print food options
                user_answer = int(input("> "))

                if user_answer > 0 and user_answer < back_number: # View the options
                    
                    option = index_to_key(menu_items[item], user_answer) # Converts answer to option veiwed

                    option_amount = int(input("Amount: ")) # Collects amount of the food type

                    if len(user_dictionary[item][option]) == 0:
                        user_dictionary[item][option] = option_amount # Adds it to the dictionary
                    else:
                        print(f"This will overwrite the previous order of {user_dictionary[item][option]}. Would you like to continue? \n a. Yes, override and save \n b. No, go back")
                        user_answer = input("> ")
                        if user_answer == "a":
                            user_dictionary[item][option] = option_amount # Add it to the dictionary

                if user_answer == back_number:
                    break

                else:
                    print("That wasn't an option")
        
        if user_answer == continue_number:

            return user_dictionary

        else:
            print(f"Please enter a number between 1 and {continue_number}.")

# Devlivery/pick up information
def delivery_infromation(user_dictionary):
    print("Would you like to: n\ 1. Pick Up \n 2. Delivered")
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

        if isinstance(item, dict):
            print(item)
            for option in item:
                print(f"{option} : {item[option]}")
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
        1 : order_number
    }

    while True:
        order_number = 1

        temp_dict = {}

        print("Welcome to Mountain Meals!" \
        "Here you can easily order tasty food.")

        print("1. Personal Information")
        temp_dict = user_information(temp_dict)

        print("2. Pick your food")
        temp_dict = ordering_information(temp_dict)

        print("3. Delivery/Pick Up Information")
        temp_dict = delivery_infromation(temp_dict)

        print("4. Confirm Order")
        print_recipt(temp_dict)
        if order_confirmed():
            number += 1 # Gets next order number
            all_orders[number] = temp_dict

            print("Thanks for coming to Mountain Meals! We hope you enjoy your food.")
        else:
            print("Your order has been cancalled! We hope you come to Mountain Meals in the future.")

main_menu()