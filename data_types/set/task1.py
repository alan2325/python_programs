php=set()
bio=set()
c=int(input("Enter your choice \n1:php \n2:bio"))

l_b=str(input("Enter the number of student in bio : "))
while True:
    if c==1:
        l_p=str(input("Enter the number of student in php : "))
        for i in range(l_p):
            php_nm=str(input("Enter the name of students : "))
    if c==2:
        l_b=str(input("Enter the number of student in bio : "))
        for i in range(l_b):
            bio_nm=str(input("Enter the name of students : "))