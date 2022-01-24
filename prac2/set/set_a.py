#20CS039 vraj nagarsheth
#defining function to add items
def addtoset(set,items):
    for item in items:
        set.add(item)
    return set

set = {"10","20","30","40"}

items = ['x','y','z','a']
#calling function
set = addtoset(set,items)

#printing results
print(set)