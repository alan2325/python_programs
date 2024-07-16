#         #1.single
# class movies:
#     def mal(self):
#         print('mal')
    
# class holiwood(movies):
#     def eng(self):
#         print('eng')
    
# anu=movies()
# anu.mal()

# bla=holiwood()
# bla.mal()
# bla.eng()

#         #2.multiple
# class movies:
#     def mal(self):
#         print('mal')
    
# class holiwood():
#     def eng(self):
#         print('eng')
    
# class wood(holiwood,movies):
#     def hin(self):
#         print('hin')
        

# bla=wood()
# bla.mal()
# bla.eng()
# bla.hin()


#         #3.multilevel
# class movies:
#     def mal(self):
#         print('mal')
    
# class holiwood(movies):
#     def eng(self):
#         print('eng')
    
# class wood(holiwood):
#     def hin(self):
#         print('hin')


# bla=wood()
# bla.mal()
# bla.eng()
# bla.hin()


#         #4.heirarchical
# class movies:
#     def mal(self):
#         print('mal')
    
# class holiwood(movies):
#     def eng(self):
#         print('eng')
    
# class wood(movies):
#     def hin(self):
#         print('hin')


# aa=holiwood()
# aa.mal()
# aa.eng()

# bla=wood()
# bla.mal()
# bla.hin()

        #5.hybrid
class a:
    def a1(self):
            print('mal')
class b:
    def b1(self):
        print('eng')
class f:
    def f1(self):
         print('hin')
class c(a,b):
     def c1(self):
          print('aa')
class d(b,f):
     def d1(self):
         print("bb")
class e(c,d):
     def e1(self):
          print('cc') 



ee=e()
ee.a1()
ee.b1()
ee.c1()
ee.d1()
ee.e1()
ee.f1()




