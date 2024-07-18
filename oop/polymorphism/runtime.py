# class sapmle:
#     def display(self):
#         print('sample class')
#     def s1(self):
#         print('sample class s1')
# class demo(sapmle):
#     def display(self):
#         print('demo display')
#         super().display()
#         print('start')
#     def d1(self):
#         print('demo class d1')
    
# obj=demo()
# obj.display()





    #input name & age

class sapmle:
    def __init__(self,name,age):
        print('sample class')
        print(name,age)
    def s1(self):
        print('sample class s1')
class demo(sapmle):
    def __init__(self,name,age):
        print(name,age)
        print('demo display')

        super().__init__(name,age)
        print('start')
    def d1(self):
        print('demo class d1')
    
obj=demo('akhil',17)