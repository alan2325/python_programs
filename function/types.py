        #positional argument
# def add(a,b):
#     return a+b
# print(add('abc','def'))
# print(add(10,20))



def add(a,b=20):
    return a,b
print(add('abc'))
print(add('cde',25))
