L=[1,2,3,4,5]
data=list(map(lambda a:a**2,L))
print(data)
        #or
# data=map(lambda a:a**2,L)
# print(list(data))



        #normal
def fun1(a):
    return a**2
data1=map(fun1,L)
print(list(data1))



