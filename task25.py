a = int(input("Enter numbers : "))
reverse=0

for i in range(a):
    digit=a%10
    reverse=(reverse*10)+digit
    a//=10
    if a==0:
        break
print("Reverse order is ",reverse)