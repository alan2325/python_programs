import mysql.connector

# Establish database connection
em = mysql.connector.connect(
    host="localhost",
    user="alal",
    password="alal123",
    database="mydatabase"
)

cursor = em.cursor()

# Create table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employ2(
        emp_id INT PRIMARY KEY,
        place text,
        experience int
    )
''')




cursor.execute("select employ.emp_id,employ.name,employ.age,employ.email,employ.position,employ.salary,employ2.place,employ2.experience from employ inner join employ2 on employ.emp_id=employ2.emp_id")
data=cursor.fetchall()
for i in data:
        print(i)




        # emp_id INT PRIMARY KEY,
        # name VARCHAR(100),
        # age INT,
        # email VARCHAR(100),
        # position VARCHAR(100),
        # salary INT


# while True:
#         print('\n1. Add\n2. Update\n3. Delete\n4. Search\n5. View all\n6. Exit')
#         ch = int(input('Enter your choice: '))
        
        # if ch == 1:
        #     l = int(input("Enter limit: "))
        #     for i in range(l):
        #         print('_' * 50)
        #         emp_id = int(input('Enter employee ID: '))
        #         place = input("Enter place : ")
        #         exp =int (input("Enter experience : "))
        #         cursor.execute('INSERT INTO employ2 (emp_id, place, experience)VALUES (%s, %s, %s)', (emp_id, place, exp))
        #         em.commit()
        # elif ch == 6:
        #     break