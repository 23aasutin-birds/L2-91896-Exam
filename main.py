"""This file collects orders for Mountain Meals and stores them for use by the company."""
import os


def clear_screen():
    """Clear user's screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def int_validation(question):
    """Return the user's integer input, repromt user if anything else is entered."""
    while True:
        try:
            user_answer = int(input(question))
            return user_answer
        except ValueError:
            print("Please enter an integer not only spaces, nothing or text. Try again.")


def string_validation(question, is_lower=True):
    """Return the user's string input striped, lowered/titled and checked in case of no characters."""
    while True:
        user_answer = input(question).strip()
        if user_answer == "":
            print("Please enter some text.")
            continue

        if is_lower:
            return user_answer.lower()  # For most input validation

        else:
            return user_answer.title()  # For names


def email_validation(question):
    """Return the user's email that contains a @ and ends in a letter (there was only so much I could do)."""
    while True:
        user_answer = input(question).strip()

        if user_answer == "":
            print("Please enter a valid email adress.")
            continue

        if "@" in user_answer and user_answer[-1].isalpha():  # If @ present in email adress and last character is a letter considered valid email
            return user_answer
        else:
            print("Please enter a valid email adress.")


def phone_validation(question):
    """Return the user's NZ phone number thats all integers and between 9 & 11 digits long."""
    LONGEST_NUMBER = 11
    SHORTEST_NUMBER = 9

    while True:
        user_answer = string_validation(question)  # Regular validation
        user_answer = user_answer.replace(" ", "")
        try:
            int(user_answer)  # Attemps to convert to string

            if len(user_answer) >= SHORTEST_NUMBER and len(user_answer) <= LONGEST_NUMBER:  # Checks for valid lenth (in NZ)
                return f"+64{int(user_answer)}"

            else:  # If outside valid range
                print(f"Phone numbers must be between {SHORTEST_NUMBER} and {LONGEST_NUMBER} digits long.")

        except ValueError:  # If not 100% integers
            print("Please enter a valid phone number will integers only.")


def user_information(order_dictionary):
    """Collect all user information and return updated order dictionary."""
    order_dictionary["Name"] = string_validation("Name: ", False)
    order_dictionary["Email"] = email_validation("Email: ")
    order_dictionary["Number"] = phone_validation("Phone Number: +64")
    return order_dictionary


def print_food_menu(menu):
    """Print all food items (Dalh with Rice etc) and return index assosiated with the Back to Main Menu option on the menu."""
    number = 1
    for item in menu:  # Extracts keys

        options = ""
        for option in menu[item]:  # Extracts keys of nested dictionary  (eg, "V", "VE", etc.)
            options = options + ", " + option

        print(f"{number}. {item} ({options[2:]})")

    print(f"Or:\n   {number}. Save & Continue")

    return number


def print_food_options(menu, key, order_dictionary):
    """Print all food options (V, VE etc) and return index assosiated with the Back to Main Menu option on the menu."""
    number = 1
    for option in menu[key]:
        try:
            print(f"    {number}. {option} ({order_dictionary[key][option]})")
        except KeyError:
            print(f"    {number}. {option} (0)")
        number += 1

    print(f"Or:\n   {number}. To Main Menu")

    return number


def index_to_key(dictionary, user_answer):
    """Return the value/key assosicated with the index the user selected."""
    try:
        list_of_items = list(dictionary.keys())  # Converts the number to the key associated with it (in dictionaries)
    except AttributeError:
        list_of_items = dictionary  # Converts the number to the key associated with it (in lists)

    return list_of_items[user_answer - 1]


def collects_order(menu_items, order_dictionary, user_answer):
    """Collect and validate users order and returns updated order dictionary."""
    item = index_to_key(menu_items, user_answer)  # Convert index to key (for later use)
    while True:
        clear_screen()
        back_number = print_food_options(menu_items, item, order_dictionary)  # Print food options, returns number associated with the "Back to Main Menu" option
        user_answer = int_validation("> ")

        if user_answer > 0 and user_answer < back_number:  # View the options
            option = index_to_key(menu_items[item], user_answer)  # Converts answer to option veiwed to use as key latter

            while True:
                option_amount = int_validation("Amount: ")  # Collects amount of the food option
                if user_answer < 0:
                    print("You can't have negative orders. Entre 0 if you would like to reset that order.")
                else:
                    break

            if order_dictionary[item].get(option, None) is None:  # If nothing under that option yet
                order_dictionary[item][option] = option_amount  # Adds it to the dictionary

            else:  # If order already under that option
                while True:
                    print(f"This will overwrite the previous order of {option}, {item}. Would you like to continue? \n 1. Yes, override and save \n 2. No, go back")
                    user_answer = int_validation("> ")

                    if user_answer == 1:
                        order_dictionary[item][option] = option_amount  # Adds it to the dictionary
                        break

                    elif user_answer == 2:
                        break

                    else:
                        print("That wasn't a valid option, please enter '1' or '2'.")

        elif user_answer == back_number:
            return order_dictionary  # Returns updated dictionary

        else:
            print("That wasn't an option")


def remove_dictionaries(menu_items, order_dictionary):
    """Return dictionary where empty nested dictionaries have been removed."""
    copy_dictionary = order_dictionary.copy()  # Makes a local copy of the dictionary so that data is not deleted in other parts of the code
    for item in menu_items:
        if copy_dictionary.get(item) == {}:  # Removes unnessisary item: {} pairs before returning
            del copy_dictionary[item]
    return copy_dictionary


def has_ordered(order_dictionary, menu_items):
    """Return wether user has ordered as a bollean value (True/False)."""
    order_dictionary = remove_dictionaries(menu_items, order_dictionary)
    if menu_items.keys() & order_dictionary.keys() == set():  # Check for lack of common keys between the two dictionaries (no order), returns keys as set()
        return False
    else:
        return True


def ordering_menu(order_dictionary):
    """Control continuous flow and infromation of the ordering proccess, return updated order_dictionary."""
    menu_items = {
        "Dalh with rice": ["M", "V", "VE", "GF", "DF"],
        "Risoto": ["M", "V", "GF"],
        "Tagine": ["M", "V", "VE", "GF", "DF"],
        "Lasagna": ["M", "V"],
    }

    for item in menu_items:
        order_dictionary[item] = {}  # Added nested item: {} pairs in preperation for order otherwise option: amount pairs have nothing to be placed into

    print("Diatary Options are as follows: \n M : Meat \n V : Vegetarian \n VE : Vegan \n GF : Gluten Free \n M : Dairy Free \n")

    while True:

        print("Food items avalibles:")
        continue_number = print_food_menu(menu_items)  # Prints all food items, returns the number associated with the "Save & Continue" option
        user_answer = int_validation("> ")
        clear_screen()

        if user_answer > 0 and user_answer < continue_number:  # Views a food item
            order_dictionary = collects_order(menu_items, order_dictionary, user_answer)  # Orders and saves
            clear_screen()

        elif user_answer == continue_number:  # To finish ordering
            if has_ordered(order_dictionary, menu_items):
                order_dictionary = remove_dictionaries(menu_items, order_dictionary)
                return order_dictionary

            else:
                clear_screen()
                print("Please order before procceeding.")

        else:  # Catchs invalid inputs
            print(f"Please enter a number between 1 and {continue_number}.")


def delivery_infromation(user_dictionary):
    """Return wether user prefers pick up or delivery (including where if the latter)."""
    print("Would you like to: \n 1. Pick Up \n 2. Delivered")
    user_answer = int_validation("> ")

    if user_answer == 1:
        user_dictionary["Delivery"] = "No"

    elif user_answer == 2:
        user_dictionary["Delivery"] = "Yes"
        user_dictionary["Adress"] = string_validation("Delivery Address: ", False)

    else:
        print("Please enter either '1' or '2'.")

    return user_dictionary


def print_recipt(user_dictionary):
    """Print personal information, food order and delivery information in full recipt."""
    for item in user_dictionary:
        if isinstance(user_dictionary[item], dict):  # If value is a dictionary
            print(f"{item}:")
            for option in user_dictionary[item]:  # Prints options individually
                print(f"    {option} : {user_dictionary[item][option]}")
        else:
            print(f"{item}: {user_dictionary[item]}")  # Else print normally


def order_confirmed():
    """Return user confirms order through bollean value (True/False)."""
    while True:
        print("\nConfirm order: \n 1. Confirm \n 2. Cancal")
        user_answer = int_validation("> ")
        if user_answer == 1:
            return True
        if user_answer == 2:
            return False
        else:
            print("Please enter either 'a' or 'b'.")


def main_menu():
    """Control continious flow of program."""
    all_orders = {}

    while True:
        clear_screen()

        order_number = 1

        temp_dict = {}

        print("Welcome to Mountain Meals! \nHere you can easily order tasty food. \n ")

        print("1. Personal Information \n")
        temp_dict = user_information(temp_dict)
        clear_screen()

        print("2. Pick your food \n")
        temp_dict = ordering_menu(temp_dict)
        clear_screen()

        print("3. Delivery/Pick Up Information \n")
        temp_dict = delivery_infromation(temp_dict)
        clear_screen()

        print("4. Confirm Order \n")
        print_recipt(temp_dict)
        is_confirmed = order_confirmed()
        if is_confirmed:
            order_number += 1  # Gets next order number
            all_orders[order_number] = temp_dict

            print("Order confirmed! Thanks for coming to Mountain Meals, we hope you enjoy your food.")

        elif not is_confirmed:  # If not confirmed
            print("Your order has been cancalled! We hope you come to Mountain Meals in the future.")

        input("\n Enter to continue \n > ")


main_menu()
