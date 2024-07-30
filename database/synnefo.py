import mysql.connector

em = mysql.connector.connect(
    host="localhost",
    user="alal",
    password="alal123",  
    database="mydatabase"  
)

cursor = em.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employ (
        emp_id INT PRIMARY KEY,
        name VARCHAR(100),
        age INT,
        email VARCHAR(100),
        position VARCHAR(100),
        salary INT
    )
''')

while True:
    print('\n1.Add\n2.Update\n3.Delete\n4.Search\n5.View all\n6.Exit')
    ch = int(input('enter your choice: '))
    if ch == 1:
        l= int (input("Enter limit : "))
        for i in range(l):
            print('_'*50)
            id = int(input('enter employee id : '))
            name = input('enter your name : ')
            age = int(input('enter your age : '))
            email = input('enter your email : ')
            pos = input('enter position : ')
            sal = int(input('enter ur salary :'))
            cursor.execute('INSERT INTO employ (emp_id, name, age, email, position, salary) VALUES (%s, %s, %s, %s, %s, %s)',
                        (id, name, age, email, pos, sal))
            em.commit()
    elif ch == 2:


        oid=str(input("Enter old id : "))
        data=cursor.execute("select * from employ WHERE emp_id=%s",(oid,))
        found=False
        for i in data:
            found=True
            # new=str(input("Enter new name : "))
            # em.execute("update employee set name=? where name =?",(new,name))
            # em.commit()
            # data=em.execute("select * from employee")
            




            print('_'*50)
            id = int(input('enter id of employee : '))
            name = input('enter your new name : ')
            age = int(input('enter your new age : '))
            email = input('enter your new email : ')
            pos = input('enter new position : ')
            sal = int(input('enter ur salary :'))
            cursor.execute('UPDATE employ SET name=%s, age=%s, email=%s, position=%s, salary=%s  WHERE emp_id=%s',
                        (name, age, email, pos, id, sal))
            em.commit()
            print("Updated succesfully !")
        
    elif ch == 3:
        id = int(input('enter id of employ to delete: '))
        cursor.execute('DELETE FROM employ WHERE emp_id=%s', (id,))
        em.commit()
    elif ch == 4:
        id = int(input('enter id to search: '))
        cursor.execute('SELECT * FROM employ WHERE emp_id=%s', (id,))
        data = cursor.fetchall()
        print('{:<10}{:<10}{:<10}{:<20}{:<10}'.format('id', 'name', 'age', 'email', 'position'))
        print('-' * 60)
        if data:
            for i in data:
                print("{:<10}{:<10}{:<10}{:<20}{:<10}".format(i[0], i[1], i[2], i[3], i[4]))
        else:
            print('id not available')
    elif ch == 5:
        cursor.execute('SELECT * FROM employ')
        data = cursor.fetchall()
        print('{:<10}{:<10}{:<10}{:<20}{:<10}'.format('id', 'name', 'age', 'email', 'position'))
        print('-' * 60)
        for i in data:
            print("{:<10}{:<10}{:<10}{:<20}{:<10}".format(i[0], i[1], i[2], i[3], i[4]))
    elif ch == 6:
        print("you have exited !")
        break
    else:
        print('invalid choice.....')