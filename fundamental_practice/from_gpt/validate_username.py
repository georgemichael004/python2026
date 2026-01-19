# Task: Validate a username for length and allowed characters.
def validate_username(username):
    if not isinstance(username, str):
        return "Username should be a string"
    if username not in range(3, 21):
        return "Username should be between 3 and 20 characters long"
    if " " in username:
        return "No spaces allowed in the username"
    


