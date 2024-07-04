a = str(input("Enter word : "))
reverse=""

for digit in str(a)[::-1]:
    reverse=reverse+str(digit)
print("Reverse order is : ",reverse)