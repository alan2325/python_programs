php=set()
bio=set()
while True:
    c=int(input('1.Add students to biology and chemistry\n2.view students\n3.View common students \n4.Exit \nEnter your choice : '))
    if c==1:
        p=int(input("Enter the number of student in php : "))
        for i in range(p):
            php_nm=str(input("Enter the name of students in php : "))
            php.add(php_nm)

        b=int(input("Enter the number of student in bio : "))
        for i in range(b):
            bio_nm=str(input("Enter the name of students in bio : "))
            bio.add(bio_nm)
    
    elif c==2:
        print('Students in php :',php)
        print('Students in biology :',bio)
    elif c==3:
        print('common students are :')
        print(php.intersection(bio))
    elif c==4:
        print("You had exited")
        break
    else:
        print("Invalid input")