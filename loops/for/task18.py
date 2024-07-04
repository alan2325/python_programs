a=int(input("Enter starting value : "))
b=int(input("Enter ending value : "))

sum=0 

for i in range(a,b):
    if i%2==1:
        sum+=i
        print(i)

print("sum : ",sum) 

