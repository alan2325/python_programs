a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
c=int(input("Enter third number : "))
d=int(input("Enter fourth number : "))

if a>b:
    if a>c:
        if a>d:
            print("Greatest number is : ",a)

        else:
            print("Greatest number is : ",d)

    else:
        if c>d:
            print("Greatest number is : ",c) 

        else:
            print("Greatest number is : ",d) 

else:

    if b>c:
        if b>d:
         print("Greatest number is : ",b)

        else:
            print("Greatest number is : ",d) 

    else:
        if c>d:
            print("Greatest number is : ",c)

        else:
            print("Greatest number is : ",d)
