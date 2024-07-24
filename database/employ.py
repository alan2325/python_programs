import sqlite3

con = sqlite3.connect("task3.db")#db connection

try:
            con.execute("create table emp(age int,name text,mark real)")#create table
except:
            pass


while True:
    ch=int(input("1.Add \n2.Update \n3.Delete \n4.Display \n5.Search \n6.Exit\nEnter choice :"))
    if ch ==1:
        l= int (input("Enter limit : "))
        for i in range(l):
            print("------------------------")
            age =int(input("Enter age : "))
            name= str(input("Enter name : "))
            mark = int(input("Enter mark : "))


            con.execute("insert into emp(age,name,mark) values(?,?,?)",(age,name,mark))#add value
            con.commit()#save




        data=con.execute("select * from emp ")
        print(data)
        # for i in data: ##print all
        #     print(i)





        print("{:<15}{:<5}{:<5}".format("name","age","mark")) ##print in a table
        print('_'*25)
        for i in data:
            print("{:<15}{:<5}{:<5}".format(i[1],i[0],i[2])) 
        print()
        





                ##update name ,user input

    elif ch==2:
        # try:
        #     con.execute("create table emp(age int,name text,mark real)")#create table
        # except:
        #     pass


        name=str(input("Enter old name : "))
        new=str(input("Enter new name : "))
        con.execute("update emp set name=? where name =?",(new,name))
        con.commit()
        data=con.execute("select * from emp")

        print("{:<15}{:<5}{:<5}".format("name","age","mark")) ##print in a table
        print('_'*25)
        for i in data:
            print("{:<15}{:<5}{:<5}".format(i[1],i[0],i[2])) 
        print()

    elif ch ==3:



        name=str(input("Enter name : "))
        con.execute("delete from emp where name =?",(name,))
        con.commit()
        data=con.execute("select * from emp")

        print("{:<15}{:<5}{:<5}".format("name","age","mark")) ##print in a table
        print('_'*25)
        for i in data:
            print("{:<15}{:<5}{:<5}".format(i[1],i[0],i[2])) 
        print()
    
    elif ch ==4:

        data=con.execute("select * from emp")

        print("{:<15}{:<5}{:<5}".format("name","age","mark")) ##print in a table
        print('_'*25)
        for i in data:
            print("{:<15}{:<5}{:<5}".format(i[1],i[0],i[2])) 
        print()
    elif ch ==5:


        name=str(input("Enter name : "))

        data=con.execute("select * from emp where name=? ",(name,))

        print("{:<15}{:<5}{:<5}".format("name","age","mark")) ##print in a table
        print('_'*25)
        for i in data:
            print("{:<15}{:<5}{:<5}".format(i[1],i[0],i[2])) 
        print()
    elif ch ==6:
        print("You had exited")
        break    