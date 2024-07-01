# num={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
# a=int(input("Enter a number : "))
# for i in range(len(num)):
#     if a in num:
#         l=len(a)
#         i=0
#         rev=''
#         while i<l:
#         # print("Values are : ",num[i])
#             rev=a[i]+rev
#             i+=1
#             print(rev)

# num = {
#     '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
#     '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
# }

# a = input("Enter a number : ")

# for digit in a:
#     if digit in num:
#         i=0
#         print(num[digit], end=' ')


num = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
    5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
}

a = int(input("Enter a number : "))

if 0 <= a <= 9:
    for i in range(a + 1):  # Loop from 0 to a (inclusive)
        print(num[i])
else:
    print("Invalid input.")

   
# num={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
# a=int(input("enter the number :"))
# s= str(a)
# result = ""
# for char in s:
#     digit = int(char)
#     if digit in num:
#         result += num[digit] + " "
# print(result.strip())


# num={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
# a=int(input("enter the number :"))
# result = []
# for digit in str(a):
#     result.append(num[int(digit)])

# print(" ".join(result))