
a=''
# a=str(input("Enter phone number : "))

# if len(a)==10 and a.isdigit():
#         if re.search('[6-9].{9}',a):
#                 print(re.search('[6-9].{9}',a))
#                 print("valid number !")
#         else:
#                 print('Invalid input !')
# else:
#         print("Invalid input !")


        #or 
import re
a=str(input("Enter phone number : "))

if len(a)==10 and a.isdigit()and re.search('[6-9].{9}',a):
        print(re.search('[6-9].{9}',a))
        print("valid number !")
else:
        print("Invalid input !")