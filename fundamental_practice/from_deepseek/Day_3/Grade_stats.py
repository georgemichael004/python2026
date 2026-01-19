student_grades = {
    "math": [85, 92, 78, 90], 
    "science": [88, 76, 95, 82], 
    "history": [70, 85, 88, 92]
}

def process_data(student_grades):
    subject_averages = {}
    total_sum = 0
    total_count = 0
    improvement = []


    for subject, grades in student_grades.items():
        if grades == []:
            return False
        
        subject_average = sum(grades) / len(grades)
        subject_averages[subject] = subject_average
        total_sum += sum(grades)
        total_count += len(grades)
        for score in grades:
           if score < 70:
              improvement.append(subject, score)

    if total_count == 0:
        overall_average = 0
    else:           
        overall_average = total_sum / total_count

    top_subject = max(subject_averages, key=subject_averages.get)

    return (subject_averages, overall_average, top_subject, improvement)


