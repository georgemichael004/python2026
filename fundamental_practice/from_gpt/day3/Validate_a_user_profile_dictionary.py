# Task: Validate user profile fields (name, age, email) with rules.
user_profile = {
    "name": "Kasule",
    "age": 25,
    "email": "kasule@gmail.com"
}

def validate_user_profile(user_profile):
    if not isinstance(user_profile["name"], str):
        return False
    if user_profile["age"]  <= 18:
        return "Age should be greater than 18"
    if "@" not in user_profile["email"]:
        return "Email should contain @ "
    if "." not in user_profile["email"]:
        return "Email should contain '.'"
    return True

print(validate_user_profile(user_profile))
