"""
Grading students

"""
def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        if grades[i] < 38 :
            continue
        else:
            rem=grades[i] % 5
            if rem == 3:
                grades[i] = grades[i]+2
            elif rem == 4:
                grades[i] = grades[i]+1
            else:
                continue
    return grades
