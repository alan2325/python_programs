a='welcome'
import re

        #substitute
# print(re.sub('w','s',a))
# 
# 
#       #splite
# # print(re.split('e',a,1))




        #serch
#1
# print(re.search('w',a))

#2
# if re.search('[a-b]',a):
#     print('yes')
# else:
#     print('no')

a='abcd'
#3
print(re.search('a..',a))

#4
print(re.search('b.*',a))

#5
print(re.search('b.?',a))

#6
print(re.search('c.+',a))
