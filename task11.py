a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
c=int(input("Enter third number : "))
d=int(input("Enter fourth number : "))

if a>b and a>c and a>d:
    print("Greatest number is : ",a)

elif b>c and b>d and b>a:
        print("Greatest number is : ",b)

elif c>d and c>b and c>a:
            print("Greatest number is : ",c)

else:
        print("Greatest number is : ",d)