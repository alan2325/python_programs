num={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
a=int(input("Enter a number : "))
for i in range(len(num)):
    if a in num:
        i=0
        # print("Values are : ",num[i])
        print(i+a)
   