class synnefo:  #class
    def python(s):   #object
        s.database='myysql'
        print("pytho")
    def php(self):   #object
        print("php",self.database)

akhil=synnefo()
akhil.python()
akhil.php()
print(akhil.database)