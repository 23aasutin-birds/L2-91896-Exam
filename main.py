def int_validation(question):
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
        user_answer = user_answer.replace(" ", "")
        try:
            int(user_answer) # Attemps to convert to string
            
            if len(user_answer) >= SHORTEST_NUMBER and len(user_answer) <= LONGEST_NUMBER: # Checks for valid lenth (in NZ)
                return f"+64{int(user_answer)}"
             
            else: # If outside valid range
                print(f"Phone numbers must be between {SHORTEST_NUMBER} and {LONGEST_NUMBER} digits long.")
        
        except ValueError: # If not 100% integers
            print("Please enter a valid phone number will integers only.")




# Collects user informaiton
def user_information(user_dictionary):
    user_dictionary["Name"] = string_validation("Name: ")
    user_dictionary["Email"] = email_validation("Email: ")
    user_dictionary["Number"] = phone_validation("Phone Number: +64") # Removed 0 from start of phone numbers, will be recored as string
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

def index_to_key(dictionary, user_answer):
    try:
        list_of_items = list(dictionary.keys()) # Converts the number to the key associated with it (in dictionaries)
    except AttributeError:
        list_of_items = dictionary # Converts the number to the key associated with it (in lists)
    
    return list_of_items[user_answer - 1]

def collects_order(menu_items, main_dictionary, user_answer):
    item = index_to_key(menu_items, user_answer) # Convert index to key (for later use)
    while True:
        print(item)
        back_number = print_food_options(menu_items, item) # Print food options
        user_answer = int_validation("> ")

        if user_answer > 0 and user_answer < back_number: # View the options
            option = index_to_key(menu_items[item], user_answer) # Converts answer to option veiwed to use as key latter
            
            while True:
                option_amount = int(input("Amount: ")) # Collects amount of the food option
                if user_answer < 0:
                    print("You can't have negative orders. Entre 0 if you would like to reset that order.")
                else:
                    break

            if main_dictionary[item].get(option, None) == None: # If nothing under that option yet
                main_dictionary[item][option] = option_amount # Adds it to the dictionary
            
            else: # If order already under that option
                print(f"This will overwrite the previous order of {option}, {item}. Would you like to continue? \n a. Yes, override and save \n b. No, go back")
                user_answer = string_validation("> ")
                
                if user_answer == "a":
                    main_dictionary[item][option] = option_amount # Adds it to the dictionary

        elif user_answer == back_number:
            return main_dictionary # Returns updated dictionary

        else:
            print("That wasn't an option")

# Collects order (should make sure users have ordered stuff)
def ordering_information(user_dictionary):
    menu_items = {
        "Dalh with rice" : ["M", "V", "VE", "GF", "DF"],
        "Risoto" : ["M", "V", "GF"],
        "Tagine" : ["M", "V", "VE", "GF", "DF"],
        "Lasagna" : ["M", "V"]
    }

    for item in menu_items:
        user_dictionary[item] = {} # Added nested item: {} pairs in preperation for order (probably possible in other ways but this is the simplest)

    while True:

        print("Food items avalibles:")
        continue_number = print_food_menu(menu_items) # prints all food items, returns the number associated with the "Save & Continue" option
        user_answer = int_validation("> ")

        if user_answer > 0 and user_answer < continue_number: # Views a food item
            user_dictionary = collects_order(menu_items, user_dictionary, user_answer) # Orders and saves
        
        elif user_answer == continue_number: # Finishes ordering
            for item in menu_items:
                if user_dictionary.get(item) == {}: # Removes unnessisary item : {} pairs before returning
                    user_dictionary.pop(item)
            
            return user_dictionary

        else: # Catchs invalid inputs
            print(f"Please enter a number between 1 and {continue_number}.")

# Devlivery/pick up information
def delivery_infromation(user_dictionary):
    print("Would you like to: \n 1. Pick Up \n 2. Delivered")
    user_answer = int_validation("> ")

    if user_answer == 1:
        user_dictionary["Delivery"] = False

    if user_answer == 2:
        user_dictionary["Delivery"] = True
        user_dictionary["Adress"] = string_validation("Delivery Address: ")

    else:
        print("Please enter either '1' or '2'.")
    
    return user_dictionary

# Recipt
def print_recipt(user_dictionary):
    for item in user_dictionary:
        if isinstance(user_dictionary[item], dict): # If value is a dictionary
            print(f"{item}:")
            for option in user_dictionary[item]: # Prints options individually
                print(f"    {option} : {user_dictionary[item][option]}")
        else:
            print(f"{item}: {user_dictionary[item]}") # Else print normally

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