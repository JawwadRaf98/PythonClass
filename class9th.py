name  = "jawwad"
# print(len(name))


# def lenght(name):
#     Name = name
#     count  = 0
#     for i in Name:
#         count += 1
#     print("the lenght of ", Name , " = ", count)


# name  =  "Jawwad Rafique Ahmed"
# lenght(name)
# name  =  "Rafique Ahmed"
# lenght(name)

# count  = 0
# for i in name:
#     count += 1
# print("the lenght of ", name , " = ", count)

# fatherName = "Muhammad Rafique Ahmed"

# # print(lenght(name))
# # print(lenght(fatherName))
# # count  = 0
# # for i in fatherName:
# #     count += 1
# # print("the lenght of ", fatherName , " = ", count)


# # Functions
# # def addition():
# #     firstNum = 12
# #     secondNum = 15
# #     total = firstNum + secondNum
# #     print(total)


# def addition(a,b):
#     firstNum = a
#     secondNum = b
#     total = firstNum + secondNum
#     print(total)

# addition(125,10)

# def subtraction(a,b):
#     total = a - b
#     print(total)
# subtraction(12,3)


# print("My Calculator")
# firstNum = float(input("Please enter first number: "))
# secondNum = float(input("Please enter second number: "))

# def addition(a, b):
#     total = a + b
#     print(a ," + ",b," = ",total)

# def subtraction(a, b):
#     total = a - b
#     print(a ," - ",b," = ",total)

# def multiplication(a, b):
#     total = a * b
#     print(a ," x ",b," = ",total)

# def Division(a, b):
#     total = a / b
#     print(a ," / ",b," = ",total)


# print("Please enter\n 1 for addition\n 2 for subtraction\n 3 for multiplication\n 4 for division.")
# option = int(input("...."))

# if option == 1:
#     addition(firstNum, secondNum)
# elif option == 2:
#     subtraction(firstNum, secondNum)
# elif option == 3:
#     multiplication(firstNum, secondNum)
# elif option == 4:
#     Division(firstNum, secondNum)
# else:
#     print("Invalid operator")

def Calculator():
    print("My Calculator")
    firstNum = float(input("Please enter first number: "))
    secondNum = float(input("Please enter second number: "))

    def addition(a, b):
        total = a + b
        print(a ," + ",b," = ",total)

    def subtraction(a, b):
        total = a - b
        print(a ," - ",b," = ",total)

    def multiplication(a, b):
        total = a * b
        print(a ," x ",b," = ",total)

    def Division(a, b):
        total = a / b
        print(a ," / ",b," = ",total)
    def options():
        print("Please enter\n 1 for addition\n 2 for subtraction\n 3 for multiplication\n 4 for division.")
        option = int(input("...."))

        if option == 1:
            addition(firstNum, secondNum)
        elif option == 2:
            subtraction(firstNum, secondNum)
        elif option == 3:
            multiplication(firstNum, secondNum)
        elif option == 4:
            Division(firstNum, secondNum)
        else:
            print("Invalid operator")
    options()

Calculator()

    

