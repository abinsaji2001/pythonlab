fyear=int(input("enter the intial year :"))
lyear=int(input("enter the last year :"))
print("leap year :")
for i in range(fyear,lyear):
    if(i%4==0)and(i%100!=0)or(i%400==0):
        print(i)
