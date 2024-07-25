import sqlite3

con = sqlite3.connect("task1.db")#db connection

# 
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

#
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

#


#         ####delete
# try:
#     con.execute("create table student(age int,name text,mark real)")#create table
# except:
#     pass


# name=str(input("Enter name : "))
# con.execute("delete from student where name =?",(name,))
# con.commit()
# data=con.execute("select * from student")

# print("{:<15}{:<5}{:<5}".format("name","age","mark")) ##print in a table
# print('_'*25)
# for i in data:
#     print("{:<15}{:<5}{:<5}".format(i[1],i[0],i[2])) 
# print()


        ###like

      
try:
    con.execute("create table student(age int,name text,mark real)")#create table
except:
    pass

data =con.execute("select * from student where name like '_r%'")
print("{:<15}{:<5}{:<5}".format("name","age","mark")) ##print in a table
print('_'*25)
for i in data:
    print("{:<15}{:<5}{:<5}".format(i[1],i[0],i[2])) 
print()