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

# Open the file in 'x' mode to create it (this will raise an error if the file already exists)
with open('python_programs/module/file_handeling/names.txt', 'x') as f:
    # Concatenate the strings into a single string
    data = 'alal' '\n' + 'bla' + '\n' + 'sreeraj'
    # Write the concatenated string to the file
    f.write(data)
