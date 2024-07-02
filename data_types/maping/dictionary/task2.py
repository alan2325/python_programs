# num = {
#     0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
#     5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
# }

# a = int(input("Enter a number : "))

# if 0 <= a <= 9:
#     for i in range(a + 1):  
#         print(num[i])
# else:
#     print("Invalid input.")







   
# num={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
# a=int(input("enter the number :"))
# s= str(a)
# result = ""
# for char in s:
#     digit = int(char)
#     if digit in num:
#         result += num[digit] + " "
# print(result)




# num={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
# a=int(input("enter the number :"))
# result = []
# for digit in str(a):
#     result.append(num[int(digit)])

# print(" ".join(result))




num={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
a=int(input("enter the number :"))
result = ''
while a>0:
    digit=a%10
    word=num[digit]
    result=word+ ' ' +result
    a=a//10
print(result)    