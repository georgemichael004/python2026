# Define a function to create a character representation
full_dot = '●'
empty_dot = '○'



def create_character(name, STR, INT, CHA):
    # Validate the character name
    if not isinstance(name, str):
        # Name should be a string
        return "The character name should be a string"
    if name == "":
        # Name should not be empty
        return "The character should have a name"
    if len(name) > 10:
        # Name should be 10 characters or less
        return "The character name is too long"
    if " " in name:
        # Name should not contain spaces
        return "The character name should not contain spaces"

    # Validate the character stats
    if not (isinstance(STR, int) and isinstance(INT, int) and isinstance(CHA, int)):
        # All stats should be integers
        return "All stats should be integers"

    # Collect stats into a list for easier comparison
    stats = [STR, INT, CHA]
    if min(stats) < 1:
        # No stat should be less than 1
        return "All stats should be no less than 1"
    if max(stats) > 4:
        # No stat should be more than 4
        return "All stats should be no more than 4"
    if sum(stats) != 7:
        # The sum of all stats should be exactly 7
        return "The character should start with 7 points"

    # Define a helper function to create a bar representation for a stat
    def bar(value):
        # Return a string with full dots for the stat value and empty dots for the remaining space
        return full_dot * value + empty_dot * (10 - value)

    # Return a formatted string representing the character
    return (
        f"{name}\n"  # Character name
        f"STR {bar(STR)}\n"  # Strength stat bar
        f"INT {bar(INT)}\n"  # Intelligence stat bar
        f"CHA {bar(CHA)}"  # Charisma stat bar
    )