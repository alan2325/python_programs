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

# a='abcd'
# #3
# print(re.search('a..',a))

# #4
# print(re.search('b.*',a))

# #5
# print(re.search('b.?',a))

# #6
# print(re.search('c.+',a))

# #7
# print(re.search('[a-z].',a))

# #8
# print(re.search('[a-z].+',a))

# #9
# print(re.search('[a-z].*',a))

# #10
# print(re.search('[A-Z].?',a))

# #11
# print(re.search('[A-Z]..',a))


a='Aabcd123'

# #12
# print(re.search('[a-z]',a))
# print(re.search('[A-Z][a-z].*[1-9]',a))

#13 or fun
print(re.search('a-zA-Z0-9',a))

#14 
print(re.search('3$',a))