# Calculate the grade of the student based on the marks he obtained
# A -> 90-100
# B -> 80 - 89
# C -> 70 - 79
# D -> 60 - 69
# F -> Below 60

marks = int(input("Enter the marks:- "))

grade = ""
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Student get {grade} with {marks} marks.")
