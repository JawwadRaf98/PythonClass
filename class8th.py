# names = {
#     'Student' : {
#         'Roll no 1' : 'Jawwad',
#         'Roll no 2' : 'Hafsa',
#         'Roll no 3' : 'Umar',
#         'Roll no 4' : 'Ahmed',
#         'Roll no 5' : 'Fariha',
#         'Roll no 6' : 'Yusra',
#         'Roll no 7' : 'Hareem',
#         'Roll no 8' : 'Maryam',
#         'Roll no 9' : 'Shiza',
#     }
# }
# category = {
#     'Boys' : [names['Student']['Roll no 1'], names['Student']['Roll no 3'], names['Student']['Roll no 4']],
#     'Girls' : [names['Student']['Roll no 2'], names['Student']['Roll no 5'], names['Student']['Roll no 6'], names['Student']['Roll no 7'], names['Student']['Roll no 8'], names['Student']['Roll no 9']]
# }
# # print(names['Student']['Roll no 4'])
# print(len(category['Girls']))
cus1 = {
    'name': "Jawwad",
    'lastName' : 'M.Rafique Ahmed'
}
# CustomerName = cus1['name']
# CustomerLastName  = cus1['lastName']
# print(CustomerName)

# Changing or updating value Jawwad to Atique
# cus1['name'] = 'Atique'

# Adding Mobile Nmber
cus1['Mobile Number']  =  '0311-xxxxxxx'
# print("Before deleting mobile number: ",cus1)

# del cus1['Mobile Number']
# print("After deleting mobile number: ",cus1)

# print(cus1)
# print(cus1['name'])
# print(cus1['lastName'])
# print(cus1['Mobile Number'])

# print(type(cus1.values()))
# for values in cus1.values():
#     print(values)


# for key in cus1.keys():
#     print(key)

# for key in cus1.keys():
#     print(key," : ", cus1[key])


# Geting key and value through .items()

# for key ,value in cus1.items():
#     print(key," : ", value,"........") 

# 
# for a ,b in cus1.items():
#     print(a," : ","........") 

myList = [
    {
        "customer id": 1,
        "first name":"Ann",
        "last name": "Sattermyer",
        "address": "PO Box 1145",
    },
    {
        "customer id": 2,
        "first name":"Jill",
        "last name": "Somers",
        "address": "3 Main St.",
    }
]
print(myList[0]['first name'])
