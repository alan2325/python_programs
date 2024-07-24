import sqlite3

con = sqlite3.connect("task1.db")#db connection

# ch=int(input("Enter choice \1.add \2.update \3.delete"))
# while true:
#     if ch ==1:
        ####fund name ,user input

# name=str(input("Enter name : "))
# age=int(input("Enter age"))
# data=con.execute("select * from student where name=? and age >?",(name,age))

# print("{:<15}{:<5}{:<5}".format("name","age","mark")) ##print in a table
# print('_'*25)
# for i in data:
#     print("{:<15}{:<5}{:<5}".format(i[1],i[0],i[2])) 
# print()



            ###update name ,user input

##elif ch==2:
# try:
#     con.execute("create table student(age int,name text,mark real)")#create table
# except:
#     pass


# name=str(input("Enter old name : "))
# new=str(input("Enter new name : "))
# con.execute("update student set name=? where name =?",(new,name))
# con.commit()
# data=con.execute("select * from student")

# print("{:<15}{:<5}{:<5}".format("name","age","mark")) ##print in a table
# print('_'*25)
# for i in data:
#     print("{:<15}{:<5}{:<5}".format(i[1],i[0],i[2])) 
# print()

## elif ch ==3:

try:
    con.execute("create table student(age int,name text,mark real)")#create table
except:
    pass


name=str(input("Enter name : "))
con.execute("delete from student where name =?",(name,))
con.commit()
data=con.execute("select * from student")

print("{:<15}{:<5}{:<5}".format("name","age","mark")) ##print in a table
print('_'*25)
for i in data:
    print("{:<15}{:<5}{:<5}".format(i[1],i[0],i[2])) 
print()