list1=[12,34,56,78,35]
list2=[35,98,67,5,5]
print("list1 : ",list1)
print("list2 : ",list2)
print("length of list1 = ", len(list1))
print("length of list2 = ", len(list2))
if len(list1)==len(list2):
    print("length of list are same")
else:
    print("length of list are not same")
print("sum of list1 = ", sum(list1))
print("sum of list2 = ", sum(list2))
if sum(list1) == sum(list2):
    print("sum of list are same")
else:
    print("sum of list are not same")
check = any(item in list1 for item in list2)
print("any value occur in both : ", check)

