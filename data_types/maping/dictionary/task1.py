l=int(input("Enter the limit : "))
d=[{'name':'a','age':20,'place':'vkm'},
   {'name':'b','age':44,'place':'ktm'},
   {'name':'c','age':50,'place':'ekm'},
   {'name':'d','age':30,'place':'alp'}]
for i in range(l):
    name=str(input("Enter the name : "))
    age=int(input("Enter the age : "))
    place=str(input("Enter your place : "))
    d.append({'name':name,'age':age,'place':place})
print("{:<10}{:<6}{:<6}".format("name","age","place"))
print('_'*22)
for i in d:
    print("{:<10}{:<6}{:<6}".format(i['name'],i['age'],i['place']))    
print()
print("Age above 40 : ")
print("{:<10}{:<6}{:<6}".format("name","age","place"))
print('_'*22)    
for i in d:
    
    if i["age"] >=40:
        
        print("{:<10}{:<6}{:<6}".format(i['name'],i['age'],i['place']))  
        

print()        
print("Age below 40 : ")
print("{:<10}{:<6}{:<6}".format("name","age","place"))
print('_'*22)  
for i in d:
    
    if i["age"] <40:
      
        
        print("{:<10}{:<6}{:<6}".format(i['name'],i['age'],i['place']))   
        