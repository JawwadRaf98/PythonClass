#  if age<30 and age>20
# you are eligible for a job


# Test Condition and , or usage
# age = 21
# if age<30 and age>20:
#     print("you are eligible for a job")
# else:
#     print("you are  not eligible for a job")

# Or
# percentage = 0
# cgp = 2.3
# if percentage >= 50 or cgp >= 3:
#     print("you are eligible for a addmission")
# else:
#     print("you are not eligible for a addmission")
# age = 32
# res = "Pak"
# if (age < 30  or age > 20) and res == "Pak":
#     print("you are eligible for USA emigration")
# else:
#     print("you are not eligible for USA emigration")

# if age > 65 or (age < 21 and res == "Pak"):
#     print("you are eligible for USA emigration")
# else:
#     print("you are not eligible for USA emigration")

# a  = 1
# b  = 1
# c  = 3
# d  = 3
# x = 5
# y  = 6
# f = "not okk"
# h = "all ok"


# if (x == y or a == b) and c == d:
#     g = h
# else:
#     g = f

# print(g)

# using nasted if

# if x == y:
#     if c == d:
#         g = h
    

# elif a == b:
#     if c == d:
#         g = h
     
# else:
#     g = f  

# print(g)

name =  "Jawwad"
fName =  "Rafique"
lName = "Ahmed"

# It will only run for name Jawwad Rafique Ahmed
if name == "Jawwad":
    if fName == "Rafique":
        if lName == "Ahmed":
            print("I am ",name, fName, lName,".")
else:
    print("I am  not",name, fName, lName,".")

