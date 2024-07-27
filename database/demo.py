import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="alal",
  password="alal123"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")