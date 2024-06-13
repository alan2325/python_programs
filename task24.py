a = int(input("Enter numbers : "))
reverse=0

for digit in str(a)[::-1]:
    reverse=reverse*10+int(digit)
print("Reverse order is ",reverse)