English = 80    
Urdu = 80
Maths = 80
Science = 80
Programming = 80

obtMarks = English + Urdu +Maths+ Science+ Programming
totalMarks = 500

percentage =  (obtMarks / totalMarks)* 100

grade = ""


if percentage >= 80:
    grade = "A+"
elif percentage >= 70: 
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50: 
    grade = "C"
else:
     grade = "FAIL"

print("English = ", English , "out of 100")
print("Urdu = ", Urdu , "out of 100")
print("Science = ", Science , "out of 100")
print("Maths = ", Maths , "out of 100")
print("Programming = ", Programming , "out of 100")
print("Obtained Marks = ", obtMarks)
print("Total Marks = ", totalMarks)
print("Percentage = ", percentage, "%")
print("Grade = ", grade)
