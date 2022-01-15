#20CS039 vraj nagarsheth
#  b. Write a Python script to merge two Python dictionaries.
# sample dictionaries
d1 = {'x': 22, 'y': 23}
d2 = {'a': 34, 'b': 56}
#making a copy of d1
d = d1.copy()
#adding d2 to d
d.update(d2)
#printing d
print(d)