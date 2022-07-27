##a=30
##b=20
##if a>b:
##    print("a is greater than b")
##    print('hello')
##print('hey')
##print('bye')

##a=int(input("enter a no: "))
##if a%2==0:
##    print(a,'is even no')
##else:
##    print(a,"is odd no")
##print('bye')

class demo:
    st=100
    def __init__(self ,a,b):
        self.a=a
        self.b=b
    def display(self):
        print(self.a)
        print(self.b)
    @classmethod
    def prin(cls):
        print(demo.st)
        print(self.a)
s=demo(10,20)
s.prin()

        
