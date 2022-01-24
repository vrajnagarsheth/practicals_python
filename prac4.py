a = int(input())
b = []
for x in range(0,a):
    k = int(input())
    b.append(k)
b.sort()
i=set(b)
sc = list(i)
print((sc[-2]))