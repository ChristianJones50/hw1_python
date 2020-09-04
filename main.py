# Author: Christian Jones

## Determine GP for course 1
gradeletter1 = input("Enter your course 1 letter grade: ")
credit1 = float(input("Enter your course 1 credit: "))
if gradeletter1 in ["A"]:
  print("Grade point for course 1 is: 4.0")
  gradepoint1 = 4.0
elif gradeletter1 in ["A-"]:
  print("Grade point for course 1 is: 3.67")
  gradepoint1 = 3.67
elif gradeletter1 in ["B+"]:
  print("Grade point for course 1 is: 3.33")
  gradepoint1 = 3.33
elif gradeletter1 in ["B"]:
  print("Grade point for course 1 is: 3.0")
  gradepoint1 = 3.0
elif gradeletter1 in ["B-"]:
  print("Grade point for course 1 is: 2.67")
  gradepoint1 = 2.67
elif gradeletter1 in ["C+"]:
  print("Grade point for course 1 is: 2.33")
  gradepoint1 = 2.33
elif gradeletter1 in ["C"]:
  print("Grade point for course 1 is: 2.0")
  gradepoint1 = 2.0
elif gradeletter1 in ["D"]:
  print("Grade point for course 1 is: 1.0")
  gradepoint1 = 1.0
else:
  print("Grade point for course 1 is: 0.0")
  gradepoint1 = 0.0

## Determine GP for course 2
gradeletter2 = input("Enter your course 2 letter grade: ")
credit2 = float(input("Enter your course 2 credit: "))
if gradeletter2 in ["A"]:
  print("Grade point for course 2 is: 4.0")
  gradepoint2 = 4.0
elif gradeletter2 in ["A-"]:
  print("Grade point for course 2 is: 3.67")
  gradepoint2 = 3.67
elif gradeletter2 in ["B+"]:
  print("Grade point for course 2 is: 3.33")
  gradepoint2 = 3.33
elif gradeletter2 in ["B"]:
  print("Grade point for course 2 is: 3.0")
  gradepoint2 = 3.0
elif gradeletter2 in ["B-"]:
  print("Grade point for course 2 is: 2.67")
  gradepoint2 = 2.67
elif gradeletter2 in ["C+"]:
  print("Grade point for course 2 is: 2.33")
  gradepoint2 = 2.33
elif gradeletter2 in ["C"]:
  print("Grade point for course 2 is: 2.0")
  gradepoint2 = 2.0
elif gradeletter2 in ["D"]:
  print("Grade point for course 2 is: 1.0")
  gradepoint2 = 1.0
else:
  print("Grade point for course 2 is: 0.0")
  gradepoint2 = 0.0

## Determine GP for course 3
gradeletter3 = input("Enter your course 3 letter grade: ")
credit3 = float(input("Enter your course 3 credit: "))
if gradeletter3 in ["A"]:
  print("Grade point for course 3 is: 4.0")
  gradepoint3 = 4.0
elif gradeletter3 in ["A-"]:
  print("Grade point for course 3 is: 3.67")
  gradepoint3 = 3.67
elif gradeletter3 in ["B+"]:
  print("Grade point for course 3 is: 3.33")
  gradepoint3 = 3.33
elif gradeletter3 in ["B"]:
  print("Grade point for course 3 is: 3.0")
  gradepoint3 = 3.0
elif gradeletter3 in ["B-"]:
  print("Grade point for course 3 is: 2.67")
  gradepoint3 = 2.67
elif gradeletter3 in ["C+"]:
  print("Grade point for course 3 is: 2.33")
  gradepoint3 = 2.33
elif gradeletter3 in ["C"]:
  print("Grade point for course 3 is: 2.0")
  gradepoint3 = 2.0
elif gradeletter3 in ["D"]:
  print("Grade point for course 3 is: 1.0")
  gradepoint3 = 1.0
else:
  print("Grade point for course 3 is: 0.0")
  gradepoint3 = 0.0

## Determines GPA 
GPA = (int(gradepoint1) * credit1 + int(gradepoint2) * credit2 + int(gradepoint3) * credit3)/(credit1 + credit2 + credit3)
print(f"Your GPA is: {GPA}")