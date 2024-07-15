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
            print('a1')
class b:
    def b1(self):
        print('b1')
class f:
    def f1(self):
         print('f1')
class c(a,b):
     def c1(self):
          print('c1')
class d(b,f):
     def d1(self):
         print("d1")
class e(c,d):
     def e1(self):
          print('e1') 



ee=e()
ee.e1()
ee.c1()
ee.a1()
ee.b1()
ee.f1()
ee.d1()
ee.a1()