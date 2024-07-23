import sqlite3

con = sqlite3.connect("task1.db")#db connection

try:
    con.execute("create table student(age int,name text,mark real)")#create table
except:
    pass
con.execute("insert into student(age,name,mark) values(22,'sreeraj',65)")#add value
con.commit()#save