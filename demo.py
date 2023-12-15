a=int(input("enter 1"))
b=int(input("enter 2"))
c=int(input("enter 3"))
if (a>=b)and(b>=c):
    print(a," is greater")
elif(b>=a)and(b>=c):
    print(b,"is greater")
else:
    print(c,"greater")
