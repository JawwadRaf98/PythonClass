# Nasted For loop

uni = ['Karachi University','Dawood University']
childs = ['Yusra', 'Hareem', 'Maryam' ,'Hafsa']

# Yursa is in Karachi University
# Hareem is in Karachi University
# Maryam is in Karachi University
# Hafsa is in Karachi University


# for i in uni:
#     for j in childs:
#         print(j ,"is in",i)

# for i in childs:
#     for j in uni:
#         print(i ,"is in",j)


# father  = ['Rafique Ahmed']
# childrens = ['Atique','Hina','Sidra','Farah','Jawwad']
# fullName = []
# for i in father:
#     for j in childrens:
#         name = j+" "+i
#         # print(j,i)
#         fullName.append(name)
        
# for i in childrens:
#     for j in father:
#         name = i+" "+j
#         print(i,j)
        # fullName.append(name)
# print(fullName)

# *
# **
# ***
# ****
# *****

# for i in range(1,11):
#     print("*"*i)


# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

# print("Hello "*2)

# Calculator

num1 = int(input("Please enter 1st number  : "))
operator = input("+ for addition\n- for subtraction\n* for Multiplication\n/ for division\n^ for power \n Enter: ")
num2 = int(input("Please enter 2nd number  : "))

if operator == "+":
    print(num1,"+",num2,"=",num1+num2)
elif operator == "-":
    print(num1,"-",num2,"=",num1-num2)
elif operator == "*":
    print(num1,"*",num2,"=",num1*num2)
elif operator == "/":
    print(num1,"/",num2,"=",num1/num2)
elif operator == "^":
    print(num1,"^",num2,"=",num1**num2)
else:
    print("Invalid Operator")


