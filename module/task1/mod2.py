#    #1.
# import mod1
# mod1.fun1()
# mod1.fun2()


#    #2
# import mod1 as s
# s.fun1()
# s.fun2()


#    #3
# from mod1 import fun1,fun2
# fun1()
# fun2()


#    #4
# from mod1 import *
# fun2()
# fun1()



    #task


from mod1 import *
print(add1(10,20))
print(add1(40,50))

print(add2(b=20,a='abc'))
print(add2('cde',25))
 
add3(b=20,a='abc')
add3('cde',25)

print(add4('dheb',23))
print(add4())
print(add4(50))

print(add5(a='dheb',b=23))
print(add5())