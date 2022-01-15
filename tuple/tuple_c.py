#20CS039 vraj nagarsheth
#Write a Python program to add an item in a tuple.
#creating a tuple
vraj = (7, 1, 0, 55, 33, 17)
print(vraj)
#using merge of tuples with the + operator you can add an element and it will create a new tuple, because tuples are immutable
vraj =vraj + (94,)
print(vraj)
#adding items in a specific index
vraj= vraj[:5] + (25, 2, 56) + vraj[:5]
print(vraj)
#converting the tuple to list
listx = list(vraj)
#use different ways to add items in list
listx.append(30)
vraj = tuple(listx)
print(vraj)