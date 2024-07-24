 # user input

import sqlite3

con = sqlite3.connect("task1.db")#db connection

try:
    con.execute("create table student(age int,name text,mark real)")#create table
except:
    pass

# l= int (input("Enter limit : "))
# for i in range(l):
#     print("------------------------")
#     age =int(input("Enter age : "))
#     name= str(input("Enter name : "))
#     mark = int(input("Enter mark : "))


#     con.execute("insert into student(age,name,mark) values(?,?,?)",(age,name,mark))#add value
#     con.commit()#save




# data=con.execute("select * from student ")
# print(data)
# # for i in data: ##print all
# #     print(i)





# print("{:<15}{:<5}{:<5}".format("name","age","mark")) ##print in a table
# print('_'*25)
# for i in data:
#     print("{:<15}{:<5}{:<5}".format(i[1],i[0],i[2])) 
# print()



        ###find

name=str(input("Enter name : "))

data=con.execute("select * from student where name=? ",(name,))

print("{:<15}{:<5}{:<5}".format("name","age","mark")) ##print in a table
print('_'*25)
for i in data:
    print("{:<15}{:<5}{:<5}".format(i[1],i[0],i[2])) 
print()