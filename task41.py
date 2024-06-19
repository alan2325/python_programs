# a=int(input('enter a value'))
# i=1
# while i<=10:
#     print(i,'*',a,'=',a*i)
#     i+=1



a=int(input('enter a number'))
rev=0
while a>0:
    d=a%10
    rev=(rev*10)+d
    a//=10
print(rev)