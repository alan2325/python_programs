def add(data):
    name=str(input("Enter name : "))
    id=int(input("Enter id : "))
    age=int(input("Enter age :"))
    place=str(input("Enter place : "))
    data.append({'name':name,'id':id,'age':age,'place':place})