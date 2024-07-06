from add import *
from dis import *
from up import *
data=[]
while True:
    print("1.Add \n2.Display \n3.Update \n4.Delate \n5.Exit")
    ch=int(input("Enter your choice : "))
    if ch == 1:
        add(data)
    elif ch == 2:
        dis(data) 
    elif ch == 3:
        up(data)