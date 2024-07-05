# def fun1():
#     print("Welcome")

# def fun2():
#     print("Hello")







    #task

            # 1.positional argument
def add1(a,b):
    return a+b



            # 2.default
def add2(a,b=20):
    return a,b



            # 3.keyword
def add3(a,b):
    print('name : ',a)
    print('age',b)



            # 4.arbitrary 
def add4(*a):
    return(a)


            # 5.arbitrary keyword
def add5(**a):
    return a
