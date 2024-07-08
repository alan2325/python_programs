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

l=int(input("Enter limit : "))
d=[]
for d in range(l):
    name=str(input("Enter names : "))
    f= open('python_programs/module/file_handeling/names.txt', 'x')    
    f.write(name)
