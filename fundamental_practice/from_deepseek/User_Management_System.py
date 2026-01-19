
def user_eligibity_check(age):
    age = int(input("Enter your age: "))
    if age < 1 or age > 150:
        print("Invalid age")
    elif age < 13:
        print("Child (under 13)")
    elif age in range(13, 18):
        print("Teenager (13-17)")
    elif age in range(18, 65):
        print("Adult (18-64)")
    elif age >= 65:
        print("Senior Citizen (65+)")
    else:
        return age


user_eligibity_check(0)



