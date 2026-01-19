# Task: Track login attempts and lock after too many failures.
# Simple login attempt counter with user input

def run_login():
    correct_email = "user@example.com"
    correct_password = "letmein"
    attempts = 0

    while attempts < 3:
        email = input("Email: ")
        password = input("Password: ")

        if email == correct_email and password == correct_password:
            print("Login successful")
            return

        attempts += 1
        if attempts >= 3:
            print("Account locked")
            return
        print(f"Invalid credentials. {3 - attempts} attempts remaining")


if __name__ == "__main__":
    run_login()

