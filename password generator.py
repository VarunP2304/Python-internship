import random
import itertools

name=input("Enter name  :")
print("Hey",name,"Welcome to password generator")

x=int(input("How many numbers you want in your password :"))
num =[i for i in range(10)]
a=random.sample(num,x)

y=int(input("How many letters you want in your password : "))
alp="QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
b=random.sample(alp,y)

z=int(input("How many special characters you want in your password : "))
symb="!@#$%^&*()?/:;"
c=random.sample(symb,z)

print("This is your password as per your requirement: ")
var=list(itertools.chain(a,b,c))
final=random.sample(var,len(var))
for i in range(len(final)):
    print(final[i],end="")
    








