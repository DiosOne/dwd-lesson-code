# 1.Report Card Generator

# dictionary where keys are student names (strings) and values are another dictionary.

# inner dictionary should store subject names (strings) as keys and
#   their corresponding grades (integers, 0-100) as values.
print()
current_students={
    'Freddy K':{'Maths': 72, 'English': 89, 'Science': 94 },
    'Jason V':{'Maths': 63, 'English': 25, 'Science': 78},
    'Michael M':{'Maths': 85, 'English': 76, 'Science': 67}
    }
avg_grades={}
for name, grades in current_students.items():
    print(f'\n{name}.')
    total_grade= sum(grades.values())
    avg_grade= round(total_grade/ len(grades),2)
    avg_grades[name]= avg_grade
    for subject, mark in grades.items():
        print(f'{subject}: {mark}')
    # identify and print their highest-scoring subject and their lowest-scoring subject
    
    high_score= max(grades.values())
    low_score= min(grades.values())
    for subject, mark in grades.items():
        if mark==high_score:
            best_subject=subject
        if mark==low_score:
            worst_subject=subject
            
    print(f'\nBest Grade: \n{high_score}. {subject}.\n \nWorst Grade: \n{low_score}. {subject}')
    print("." * 20)
    
# Calculate and print the average grade for one specific student
print(f'\nJason\'s average: {avg_grades['Jason V']}')
print(f'\nFreddy\'s average: {avg_grades['Freddy K']}')
print(f'\nMichael\'s average: {avg_grades['Michael M']}')

