print("1.ADD\n2.Display\n3.Update\n4.Delete\n5.Exit")
name=[]
while True:
    a=int(input("Enter your choice : "))
    
    

    
    if a==1:
        e=int(input("Enter limit : "))
        for i in range(e):
        
            b=str(input("Enter names : "))
            name.append(b)
    elif a==2:
            for i in name:
                print("Names are :",i) 
    elif a==3:
        c=str(input("Enter name needed to be updated : "))
        if c in name:
            b=str(input("Enter new updation : "))
            pos=name.index(c)
            name[pos]=b
            print("Updation is : ",name)
        else:
             print("Name not found")

    elif a==4:
            d=str(input("Enter name needed to be deleted : "))
            if d in name:
                name.remove(d)
                print("Deleted : ",name)
            else:
                print("Name not found")

    elif a==5:
            print("You had exited")
            break
            
    else:
        print("INVALID INPUT !")