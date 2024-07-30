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
    print('\n1. Add\n2. Update\n3. Delete\n4. Search\n5. View all\n6. Exit')
    ch = int(input('Enter your choice: '))
    
    if ch == 1:
        l = int(input("Enter limit: "))
        for i in range(l):
            print('_' * 50)
            emp_id = int(input('Enter employee ID: '))
            name = input('Enter your name: ')
            age = int(input('Enter your age: '))
            email = input('Enter your email: ')
            position = input('Enter position: ')
            salary = int(input('Enter your salary: '))
            cursor.execute('''
                INSERT INTO employ (emp_id, name, age, email, position, salary)
                VALUES (%s, %s, %s, %s, %s, %s)
            ''', (emp_id, name, age, email, position, salary))
            em.commit()

    elif ch == 2:
        emp_id = int(input("Enter the ID of the employee to update: "))
        cursor.execute("SELECT * FROM employ WHERE emp_id = %s", (emp_id,))
        employee = cursor.fetchone()
        
        if employee:
            print('_' * 50)
            new_name = input(f'Enter new name (current: {employee[1]}): ')
            new_age = int(input(f'Enter new age (current: {employee[2]}): '))
            new_email = input(f'Enter new email (current: {employee[3]}): ')
            new_position = input(f'Enter new position (current: {employee[4]}): ')
            new_salary = int(input(f'Enter new salary (current: {employee[5]}): '))
            
            cursor.execute('''
                UPDATE employ
                SET name = %s, age = %s, email = %s, position = %s, salary = %s
                WHERE emp_id = %s
            ''', (new_name, new_age, new_email, new_position, new_salary, emp_id))
            em.commit()
            print("Updated successfully!")
        else:
            print("Employee ID not found.")

    elif ch == 3:
        emp_id = int(input("Enter the ID of the employee to delete: "))
        cursor.execute("DELETE FROM employ WHERE emp_id = %s", (emp_id,))
        em.commit()
        print("Deleted successfully!")

    elif ch == 4:
        emp_id = int(input("Enter the ID of the employee to search: "))
        cursor.execute("SELECT * FROM employ WHERE emp_id = %s", (emp_id,))
        employee = cursor.fetchone()
        
        if employee:
            print('_' * 50)
            print(f'ID: {employee[0]}')
            print(f'Name: {employee[1]}')
            print(f'Age: {employee[2]}')
            print(f'Email: {employee[3]}')
            print(f'Position: {employee[4]}')
            print(f'Salary: {employee[5]}')
        else:
            print("Employee ID not found.")

    elif ch == 5:
        cursor.execute("SELECT * FROM employ")
        employees = cursor.fetchall()
        
        if employees:
            print('_' * 50)
            for emp in employees:
                print(f'ID: {emp[0]}, Name: {emp[1]}, Age: {emp[2]}, Email: {emp[3]}, Position: {emp[4]}, Salary: {emp[5]}')
        else:
            print("No employees found.")

    elif ch == 6:
        break

    else:
        print("Invalid choice. Please try again.")

cursor.close()
em.close()
