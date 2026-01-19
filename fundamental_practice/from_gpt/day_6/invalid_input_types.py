# Q: How do you loop until a valid integer input is provided?
def get_safe_integer():
    while True:
        user_input = input("Please enter a whole number: ")
        try:
            number = int(user_input)
            print(f"You entered the integer: {number}")
            return number
        except ValueError:
            print("Invalid input. Please enter a whole number.")

get_safe_integer()
