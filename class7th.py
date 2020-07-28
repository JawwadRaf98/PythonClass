# # # Dictionaries
# # # nameOfStudents = ['Hafsa','Yusra','Hareem']

# # # print(nameOfStudents[1])

# # customer0 = {
# #     'firstName' : 'Jawwad',
# #     'lastName' : 'M.Rafique Ahmed',
# #     'Height' : 5.6    
# # }
# # customer1 = {
# #     'firstName' : 'Hafsa',
# #     'lastName' : 'Shabab Ahmed',
# #     'Height' : 4.3    
# # }

# # print('Name :', customer1['firstName'])
# # print('Last Name :', customer1['lastName'])
# # print('Height :', customer1['Height'],"Feet")


# # Hospital

# patients = [
#     {
#         "Name": [ 'Ali','Hamza','Anus','Ammar','Taqi'],
#     },
#     {
#         "Name":'Sehroz',
#     },
#     {
#         "Name":'Fariha',
#     },
#     {
#         "Name":'Shiza',
#     },
#     {
#         "Name":'Jawwad',
#     },
# ]

# print(patients[0]['Name'][3])

a = 1
for i in range(1,11):
    if i<=6:
        print('*'*i)
    else:
        d = i - a
        print("*"*d)
        a += 1

