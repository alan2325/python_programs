 # user input

import sqlite3

con = sqlite3.connect("task1.db")

try:
    con.execute("create table student(age int,name text,mark real)")
except:
    pass


age =int(input("Enter age : "))
name= str(input("Enter name : "))
mark = int(input("Enter mark : "))


con.execute("insert into student(age,name,mark) values(?,?,?)",(age,name,mark))
con.commit()