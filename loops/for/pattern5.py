    # A 
    # A B 
    # A B C
for i in range(1,4):
    a=65
    for j in range(i):
        print(chr(a+j),end=" ")
    print()


    # A 
    # B B 
    # C C C
for i in range(1,4):
    a=65
    for j in range(i):
        print(chr((a-1)+i),end=" ")
    print()

    # A 
    # B A 
    # C B A 
for i in range(1,4):
    a=65
    for j in range(i,0,-1):
        print(chr((a-1)+j),end=" ")
    print()

        # or
a=65
for i in range(1,4):
    b=a
    for j in range(i):
        print(chr(b),end=" ")
        b-=1
    print()
    a+=1    