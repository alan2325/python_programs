# 
# L=[1,2,3,4,5]
# data=filter(lambda a:a%2==0,L)
# print (list(data))


        #normal

# def fun1(a):
#     return a%2==0
# data1=filter(fun1,L)
# print(list(data1))





        #2.print words with starting letter 'a'

L=['apple','orange']
data=filter(lambda a:a[0]=='a',L)
print (list(data))


        #normal

def fun1(a):
    return a[0]=='a'
data1=filter(fun1,L)
print(list(data1))

