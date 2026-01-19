# Q: How do you handle ZeroDivisionError and TypeError safely?
def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except TypeError:
        print("Error: Invalid data types")

safe_divide(10, 2)
safe_divide(10, 0)
safe_divide("10", 2)
safe_divide(10, "2")
