fruits={2:"apple",6:"orange",1:"grapes",8:"strawberry",4:"pineapple"}
print(fruits)
a=list(fruits.items())
a.sort()
print("Ascending order :",a)
a=list(fruits.items())
a.sort(reverse=True)
print("Descending order :",a)
