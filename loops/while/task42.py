
        # choice

print("1.ADD\n2.SUB\n3.MUL\n4.DIV\n5.MOD\n6.BREAK")
while True:
    a=int(input("Enter your choice : "))
    b=int(input("Enter first number : "))
    c=int(input("Enter second number : "))



    if a==1:
        print("sum : ",b+c)
    elif a==2:
        print("sub : ",b-c) 
    elif a==3:
        print("mul : ",b*c)   
    elif a==4:
        print("div : ",b/c)
    elif a==5:
        print("mod : ",b%c)
    elif a==6:
        print("You had exited")
        break
        
    else:
        print("INVALID INPUT !")