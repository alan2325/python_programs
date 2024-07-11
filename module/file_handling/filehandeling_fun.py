            #new
# f=open('python_programs/module/file_handeling/new1.txt','x')
# f.write('123'+'frurnjrujfefeffefefeufuje')

            #overrite
# f=open('python_programs/module/file_handeling/new1.txt','x')
# f.write('123'+'frurnjrujfefeffefefeufuje')

            #new
# f=open('python_programs/module/file_handeling/new2.txt','w')
# f.write('welcome')





            #enter names
# f=open('python_programs/module/file_handeling/names.txt','x')
# f.write('alal'+'bla','sreeraj')

            #or

# l=int(input("Enter limit : "))
# d=[]
# for d in range(l):
#     name=str(input("Enter names : "))
#     f= open('python_programs/module/file_handeling/names.txt', 'x')    
#     f.write(name)



    #append
# f=open("python_programs/module/file_handling/new.txt","a")
# f.write("python")

    #read
# f=open("python_programs/module/file_handling/new.txt","r")
# print(f.read())


    #or
# f=open("python_programs/module/file_handling/new.txt","r")
# print(f.read(3))
# print('_'*20)
# print(f.read(4))

    #or
# f=open("python_programs/module/file_handling/new.txt","r")
# print(f.readline(3))
# print('_'*20)
# print(f.readline(4))
# print(f.readline())


    #to count no:lines
# f=open("python_programs/module/file_handling/new.txt","r")
# print(f.readlines())

    #reverse of all
# f=open("python_programs/module/file_handling/new.txt","r")
# l=len(f.readlines())
# f.seek(0)
# for i in range(l):
#     a=f.readline().strip()
#     print(a[::-1])


    #count words
f=open("python_programs/module/file_handling/new.txt","r")
l=len(f.readlines())
f.seek(0)
word=0
for i in range(l):
    a=f.readline().strip()
    for j in a:
        if j== ' ':
            word+=1
    # print(a[::-1])
    word+=1
print("Number of words is : ",word)