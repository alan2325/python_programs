a = int(input("Enter a number : "))
prime=True

if a < 2:
    prime = False
else:
    prime = True

    for i in range(2,a):
        if a%i == 0:
            prime = False
        break        

if prime:
    print(a,"is a prime number")
else:
    print(a,"is not a prime number")        