# import re
# a=str(input("Enter email : "))

# if  re.search('[a-zA-Z].*@gmail.com$',a):
       
#         print("valid email !")
# else:
#         print("Invalid email !")


        #or

import re
a=str(input("Enter email : "))
pattern="'[a-zA-Z].*@gmail.com$'"
if  re.search(pattern,a):
       
        print("valid email !")
else:
        print("Invalid email !")
