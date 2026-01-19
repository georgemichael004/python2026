# Task: Add status based on the verified field in the user dictionary.
user = {'name': 'Alex', 'verified': True}
def add_verified():
    if user['verified']:
        user['status'] = 'active'
    else:
        user['status'] = 'pending'
        
add_verified()
print(user)
