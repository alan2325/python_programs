class synnefo:
    def __init__(s):
        print('Regester')
    def python(s):
        s.database='mysql'
        print('python')
    def php(self):
        self.database='mysql'
        print('php',self.database)
class novavi():
    def dm(self):
        print('dm')
    def web(self):
        print('web developer')
class std(synnefo,novavi):
    def helo(self):
        print('helo')       

anu=synnefo()
anu.php()

bla=novavi()
bla.dm()


aaa=std()
aaa.helo()
aaa.python()
aaa.dm()