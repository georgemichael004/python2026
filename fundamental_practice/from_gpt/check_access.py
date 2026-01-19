# Task: Grant access only when age is 18+ and ID is present.
def check_access(age, has_id):
    if age >= 18 and has_id == True:
        return "Access granted"
    else:
        return "Access denied"
    

print(check_access(6, True))
