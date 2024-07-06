from add import *
from dis import *
from up import *
from dele import *
data=[{"id": "1", "name": "Alice", "age": "30", "place": "New York"},
    {"id": "2", "name": "Bob", "age": "25", "place": "Chicago"},]
while True:
    print("1.Add \n2.Display \n3.Update \n4.Delate \n5.Exit")
    ch=int(input("Enter your choice : "))
    if ch == 1:
        add(data)
    elif ch == 2:
        dis(data) 
    elif ch == 3:
        up(data)
    elif ch == 4:
        dele(data)
    elif ch == 5:
        print("You had exited")
        break
    else:
        ("Invalid input")