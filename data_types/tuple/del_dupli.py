t=1,2,3,4,5,4
a=list(t)
rem = []
for item in a:
    if item not in rem:
        rem.append(item)
t=tuple(rem)
print(t)
