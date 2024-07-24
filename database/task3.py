import sqlite3

con = sqlite3.connect("task1.db")#db connection

name=str(input("Enter name : "))
age=int(input("Enter age"))
data=con.execute("select * from student where name=? and age >?",(name,age))

print("{:<15}{:<5}{:<5}".format("name","age","mark")) ##print in a table
print('_'*25)
for i in data:
    print("{:<15}{:<5}{:<5}".format(i[1],i[0],i[2])) 
print()