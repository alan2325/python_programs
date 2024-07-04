import functools
L=[1,2,3,4,5]
data=functools.reduce(lambda total,value:total*value,L)
data1=functools.reduce(lambda total,value:total+value,L)
print(data)
print(data1)

        #normla

def fun1(total,value):
    return total+value
import functools
data1=functools.reduce(fun1,L)
print(data1)

