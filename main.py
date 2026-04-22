# Collects user informaiton
def user_information(dictionary):
    dictionary["Name"] = input("Name: ")
    dictionary["Email"] = input("Email: ")
    dictionary["Number"] = input("Phone Number: ")

# Collects order
def ordering_information():
    print("Hi")

# Devlivery/pick up information
def delivery_infromation():
    print("Hi")

# Recipt
def print_recipt():
    print("Hi")

# Cancellation/confirmation
def order_confirmation():
    print("Hi")

# Main menu
def main_menu():

    menu_items = {
        "Dalh with rice" : ["M", "VE", "V", "GF", "DF"],
        "Risoto" : ["M", "V", "GF"],
        "Tagine" : ["M", "VE", "V", "GF", "DF"],
        "Lasagna" : ["M", "V"]
    }

    order = {
        ""
    }

    """order_number = {
        "Name" : "Audrey Austin",
        "Email" : "audrey.c.austin@gmail.com",
        "Number" : 642040326799,
        "Tagine" : {
            "V" : 2
        }
    }"""

    while True:

        temp_dic = {}

        print("Welcom to Mountain Meals!" \
        "Here you can easily order tasty food.")

        print("1. Personal Information")
        user_information(temp_dic)

        print("2. Pick your food")
        ordering_information()

        print("3. Delivery/Pick Up Information")
        delivery_infromation()

        print("4. Confirm Order")
        print_recipt()
        order_confirmation()

        print("Thanks for coming to Mountain Meals! We hope you enjoy your food.")