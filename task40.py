
# a=int(input("enter starting number : "))
# b=int(input("enter ending number : "))
# while a<=b:
#     print(a)
#     a+=1

# sum of n mun

# a=int(input("enter starting number : "))
# b=int(input("enter ending number : "))
# sum=0
# while a<=b:
#     sum+=a
#     a+=1
# print(sum)

    # odd number

# a=int(input("enter starting number : "))
# b=int(input("enter ending number : "))
# while a<=b:
#     if a%2==1:
#         print(a)
#     a+=1


    # even number
# a=int(input("enter starting number : "))
# b=int(input("enter ending number : "))
# while a<=b:
#     if a%2==0:
#         print(a)
#     a+=1



# sum of even

a=int(input("enter starting number : "))
b=int(input("enter ending number : "))
sum=0
while a<=b:
    if a%2==1:
        print(a)
        sum+=a
    a+=1
print("sum :",sum)


# sum of even odd nat

a=int(input("Enter starting value : "))
b=int(input("Enter ending value : "))

sum=0 
odd=0
even=0
while a<=b:
    sum+=a

    if a%2==1:
        odd+=a
    
    else:
        even+=a
    a+=1
print("sum of even : ",even)
print("sum of odd: ",odd)
print("sum of natural : ",sum)      
   
