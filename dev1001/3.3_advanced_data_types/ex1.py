'''_summary_'''
# Tuples Exercise

# Student Info: (ID, Name, Major)
student_record = (101, "Alice Wonderland", "Computer Science")

# 1. Access and print the student's name.
print(f"Student's name: {student_record[1]}")

# 2. Create a new tuple that includes the student's current term.
#       Remember, tuples are immutable, so you'll create a NEW one.
#       Hint: You can concatenate tuples using '+'
#       (Challenge) Use unpack operator instead of concatenation.

record_update=(*student_record, "Summer 2025")
print(f"Updated student record: {record_update}")
# 3. Unpack the original student_record into three separate variables.

ID, name, course= student_record
print(f"ID: {ID}, Name: {name}, Course: {course}")

# 4. Use the slice operator to extract the student name only.

print(student_record[1:2])
