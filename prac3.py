x=int(input())
lst=list(map(int,input().split()))
a=set()
b=set()
for room in lst:
    if room not in a:
        a.add(room)
        b.add(room)
    else:
        b.discard(room)

b=list(b)
print(b)