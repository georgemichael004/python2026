

users = {}
user_id = input("Enter the user ID: ")
name = input("Enter the name: ")
email = input("Enter the email: ")


users[user_id] = {"name": name, "email": email}

choice = input("Choose: update / delete / search:").lower()

if choice == "update":
    new_email = input("Enter the new email: ")
    if user_id in users:
        users[user_id]["email"] = new_email
elif choice == "delete":
    if user_id in users:
        del users[user_id]
elif choice == "search":
    search_name = input("Search name: ")
    matches = []
    for user_id, details in users.items():
        if details["name"] == search_name:
            matches.append((user_id, details))
    print(matches)

print(users)





# while True:
#     user_key = input("Input the Key i.e ID, name, email: ")
#     if user_key.lower() == "quite":
#         break
#     user_value = input(f"Input the Value for the respective {user_key}: ")
#     user_profile[user_key] = user_value

# if "ID" in user_profile:
#     user_profile["email"] = # new email

# if "ID" in user_profile:
#     user_profile.pop("ID")

# for key, value in user_profile.items():
#     user_profile[f"{value}"]

# def search_user_by_name(name):
#     'name': isinstance(name, str) and re.fullmatch(name, re.IGNORECASE)




