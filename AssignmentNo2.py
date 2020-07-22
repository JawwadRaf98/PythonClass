# # Hafsa
# number=int(input("enter the number:"))
# a=number//100
# b=number%100
# print("hundred's notes is",a)
# c=b//50
# d=b%50
# print("fiftys's notes is",c)
# e=d//20
# f=d%20
# print("twenty's notes is",e)
# g=f//10
# h=f%10
# print("ten's notes is",g)
# i=h//5
# j=h%5
# print("five rupees coin is",i)
# k=j//2
# l=j%2
# print("2 rupees coin is",k)
# m=l//1
# n=l%1
# print("1 rupee coin is",m)




number=int(input("enter the number:"))
a=number//100
b=number%100
c=b//50
d=b%50
e=d//20
f=d%20
g=f//10
h=f%10
i=h//5
j=h%5
k=j//2
l=j%2
m=l//1
n=l%1
if a != 0:
    print("hundred's notes is",a)
if c != 0:
    print("fiftys's notes is",c)
if e != 0:
    print("twenty's notes is",e)
if g != 0:
    print("ten's notes is",g)
if i != 0:
    print("five rupees coin is",i)
if k != 0:
    print("2 rupees coin is",k)
if m != 0:
    print("1 rupee coin is",m)