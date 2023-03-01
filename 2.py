students = [['Jerry', 88], ['Justin', 84], ['Tom', 90], ['Akriti', 92], ['Harsh', 90]]  


def second_highest(students):
    score = [s[1] for s in students]
    score = sorted(score, reverse = True)
    second_score = score[1]
    second_high_student = [s[0] for s in students if s[1] == second_score]
    for student in second_high_student:
        print(student)


second_highest(students)    
