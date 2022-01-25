student_height = input("Enter lists of students height: ").split()
for n in range(0, len(student_height) - 1):
    student_height[n] = int(student_height[n])
print(student_height)

total_height = 0
for height in student_height:
    total_height += height
print(total_height)
#total_height = sum(student_height)

number_of_students = 0
for student in student_height:
    number_of_students += 1
print(number_of_students)
#number_of_students = len(student_height)
average_height = total_height / number_of_students
print(average_height)