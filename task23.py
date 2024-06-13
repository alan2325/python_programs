a = int(input("Enter the starting number"))
b = int(input("Enter the ending number"))

print("Prim numbers between ",a,"and",b,"are")

for num in range(a,b+1):
    if num>1:
        is_prime = True
        for i in range(2,int(num**.5)+1):
            if (num%i) ==0:
                is_prime=False
            break
        if is_prime:
            print(num)