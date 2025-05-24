# Task: Read new_grades.csv (that was just created) and print only the
#       names of students who scored above 90.
import csv

with open("new_grades.csv", mode='r', newline='') as f:
    csv_reader = csv.reader(f)
    header = next(csv_reader) # Skip/read header row
    print(f"Header: {header}")
    for row in csv_reader:
        name, subject, grade = row
        if int(grade) > 90:
            print(f"{name} scored {grade} in {subject}")