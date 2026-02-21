# Q: How do you validate operations and avoid division by zero?
def calculator():
    print("Welcome to safe Calculaor")
    while True:
        num1_str = input("Enter the first number: ") 
        if num1_str == "exit": break
        opp = input("Enter the operation ie +, -, *, /: ")
        if opp not in ["+", "-", "*", "/"]:
            print("Invalid operation")
            continue
        num2_str = input("Enter the second number: ")       

        try:
            num1 = float(num1_str)
            num2 = float(num2_str)

            if opp == "+":
                result = num1 + num2
            elif opp == "-":
                result = num1 - num2
            elif opp == "*":
                result = num1 * num2
            elif opp == "/":
                if num2 == 0:
                    print("Error denominator can not be a zero")
                    continue
                result = num1 / num2
            print(f"Result: {result}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")

        
calculator()
        



