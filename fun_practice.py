def add_nmr(num1,num2):
    return num1+num2

add_nmr(45,67)

print(add_nmr(33,12))

nmr3=add_nmr(20,20)+10
print(nmr3)


def print_name(age,name='Friend'): #default value baad me dena hota hai normal value pehle agr default value dena hai to
    print("Hello",name,"Your age is ",age)

print(print_name(name="Sita",age=29))

def add_multiple(*args):
    sum=0
    for i in range(len(args)):
        print(sum)
        sum=sum+args[i]
    return sum

x=add_multiple(3,4,5,3,4,5,7)
print(x)

def recursion(n):
    if n==0:
        return 1
    return n*recursion(n-1)

print(recursion(5))
