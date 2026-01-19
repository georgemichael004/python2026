def grade_to_letter(grade):
    if grade < 0 or grade > 100:
        return "Invalid grade"
    if grade >= 90:
        letter = "A"
    elif grade >= 80:
        letter =  "B"
    elif grade >= 70:
        letter =  "C"
    elif grade >= 60:
        letter =  "D"
    else:
        return "F"
    
    if grade == 100:
        return "A+"
    
    last_digit = grade % 10

    if last_digit in (7, 8, 9):
        return letter + "+" 
    if last_digit in (0, 1, 2):
        return letter + "-"
    return letter

    

    