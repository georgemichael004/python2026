# Q: How do you validate type and range before acting?
def set_volume(level):
    """Sets the system volume, only if the input is valid integer between 0 and 10."""
    if not isinstance(level, int):
        print("Error: Volume level must be an integer.")
        return 
    if not (0 <= level <= 10):
        print("Error: Volume level must be between 0 and 10.")
        return
    
    print(f"Setting volume to {level}")

set_volume(5)
set_volume("high")
set_volume(15)
