a=int(input("Enter starting value : "))
b=int(input("Enter ending value : "))

sum=0 
odd=0
even=0

for i in range(a,b+1):
    sum+=i

    if i%2==1:
        odd+=i
    
    else:
        even+=i
print("sum of even : ",even)
print("sum of odd: ",odd)
print("sum of natural : ",sum)      