# Task: Call helper functions to complete a larger operation.
def greet(name):
    """"A simple greeting helper function."""
    return f"Hello, {name}!"

def introduce_character(name, level):
    """The main function that calls greet() and adds more detail."""
    greeting_message = greet(name)
    print(f"{greeting_message} You are level {level}.")

introduce_character("Puplexor", 5)
