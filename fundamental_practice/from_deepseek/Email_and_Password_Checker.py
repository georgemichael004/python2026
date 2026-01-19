def validate_user_registration_input(email, password, username):
    errors = []
    if "@" not in email:
        errors.append("email missing a '@'")

    if "." not in email:
        errors.append("email missing a '.'")
    
    if len(password) < 8:
        errors.append("password must be at least 8 characters long")
        
    
    if not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
        errors.append("password must contain at least one digit and one letter")
    
    
    
    if len(username) not in range(3, 21):
        errors.append("Username must be 3-20 characters long")
    for ch in username:
        if not (ch.isalnum() or ch == "_"):
            errors.append("Username can only contain letters, numbers, and underscores")
            break
    is_valid = len(errors) == 0
    return (is_valid, errors)

     
    