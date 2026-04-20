# Collects user informaiton
def user_information():
    print("Hi")

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
    while True:
        print("Welcom to Mountain Meals!" \
        "Here you can easily order tasty food.")

        print("1. Personal Information")
        user_information()

        print("2. Pick your food")
        ordering_information()

        print("3. Delivery/Pick Up Information")
        delivery_infromation()

        print("4. Confirm Order")
        print_recipt()
        order_confirmation()

        print("Thanks for coming to Mountain Meals! We hope you enjoy your food.")