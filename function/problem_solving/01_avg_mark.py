# marks = [55, 64, 75, 80, 65]

# # Calculate the average
# average_marks = sum(marks) / len(marks)

# # Determine the grade
# if average_marks >= 80:
#     grade = "A"
# elif average_marks >= 60:
#     grade = "B"
# elif average_marks >= 50:
#     grade = "C"
# else:
#     grade = "F"

# print(f"Average Marks: {average_marks}")
# print(f"Grade: {grade}")




def find_average_marks(marks):
    sum_of_marks = sum(marks)
    total_subjects = len(marks)
    average_marks = sum_of_marks/total_subjects
    return average_marks

def grade_check(average_marks):
  if average_marks >=80:
    grade = "A"
  elif average_marks >=60:
    grade = "B"
  elif average_marks >=50:
    grade = "C"
  else:
    grade = "F"
  return grade

marks = [55, 84, 75, 85, 80]

average_marks = find_average_marks(marks)
print("Your average mark is: ", average_marks)

grade = grade_check(average_marks)
print("Your grade is: ",grade)