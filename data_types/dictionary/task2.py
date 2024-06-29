l=int(input("Enter the limit : "))
d=[]
for i in range(l):
    name=str(input("Enter the name : "))
    age=int(input("Enter the age : "))
    place=str(input("Enter your place : "))
    d.append({'name':name,'age':age,'place':place})
print("{:<10}{:<6}{:<6}".format("name","age","place"))
print('_'*20)
for i in d:
    print("{:<10}{:<6}{:<6}".format(i['name'],i['age'],i['place']))