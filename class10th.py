# passing value to the function
# def add_numbers():
#     first  = 12
#     second = 13
#     total = first + second
#     print(total)

# add_numbers()

def add_numbers(a, b):
    first  = a
    second = b
    total = first + second
    print(total)

add_numbers(12, 12)

# Chapter no 43

def add_patient(name, father,age = "null"):
    Name = name 
    Father = father
    Age = age 
    print("Name = ",name,"\nFather Name = ",Father,"\nAge = ",Age)

# positional arguments
# add_patient("jawwad", "Rafique", 12)

# add_patient(name="jawwad",father="Rafique", age=23)

# def calc_tax(sales, rate = 0.05):
#     tax  = sales*rate 
#     print(tax)

# calc_tax(1000,rate=0.1)

# calc_tax(rate=0.12,sales=1000)


# def calc_tax(name,sales,rate = 0.05):
#     tax  = sales*rate 
#     print(tax)

# calc_tax("jawwad",rate=0.1,sales=1000)


customers = {
 0: {
    "first name":"John",
    "last name": "Ogden",
    "address": "301 Arbor Rd.",
 },
 1: {
    "first name":"Ann",
    "last name": "Sattermyer",
    "address": "PO Box 1145",
 }
}


# def find_something(dict, inner_dict, target):
#     print(dict[inner_dict][target])

# find_something(customers,1,"first name")

def get_result(winner, score , **moreInfo):
    print("Winner : ", winner)
    print("Score : ", score)

    for key ,value in moreInfo.items():
        print(key.title(), " : ", value.title())
    
get_result(winner="Jawwad", score="3-2", Losser = "hafsa", day="Monday")