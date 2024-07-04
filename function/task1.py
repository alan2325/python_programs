def add(a,b):
    return a+b 
    
def sub(a,b):
    return a-b 
     
div=lambda a,b:a/b

mul=lambda a,b:a*b
   
def num():
    a=int(input("Enter a number : "))
    b=int(input("Enter another number : "))
    return a,b

while True:
    # print("1.add \n2.sub \n3.div \n4.mul \n5.End ")
    c=int(input("1.add \n2.sub \n3.div \n4.mul \n5.End \n Enter your choice : "))

    if c==1:
        a,b=num()
        print(add(a,b))
    elif c==2:
        a,b=num()
        print("sub is : ",sub(a,b))
    elif c==3:
        a,b=num()
        print("div is : ",div(a,b))
    elif c==4:
        a,b=num()
        print("mul is : ",mul(a,b))
    elif c==5:
        break
    else:
        print("Invalid input")