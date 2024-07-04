            # 1.positional argument
# def add(a,b):
#     return a+b
# print(add('abc','def'))
# print(add(10,20))


            # 2.default
# def add(a,b=20):
#     return a,b
# print(add('abc'))
# print(add('cde',25))


            # 3.keyword
# def add(a,b):
#     print('name : ',a)
#     print('age',b)
# add(b=20,a='abc')
# add('cde',25)



            # 4.arbitrary 
# def add(*a):
#     return(a)
# print(add('dheb',23))
# print(add())
# print(add(50))


            # 5.arbitrary keyword
def add(**a):
    return a
print(add(a='dheb',b=23))
print(add())
