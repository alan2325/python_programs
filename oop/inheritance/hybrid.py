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


aa=a()
aa.a1()

bb=b()
bb.b1()

ff=f()
ff.f1()

cc=c()
cc.c1()
cc.a1()
cc.b1()


dd=d()
dd.d1()
dd.f1()

ee=e()
ee.e1()
