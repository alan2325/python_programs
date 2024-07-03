# print("helo")
# def fun1():
#     print("Welcome")

# print("ok")
# fun1()



print("helo")
a=20                #global veriable
def fun1():
    a=15            #local veriable
    a=a+10
    print("local",a)

print("global",a)
fun1()