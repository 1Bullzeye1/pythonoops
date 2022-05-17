####  Duck Typing

x = 5  ### dynamic typing

print(type(x))
x = 'Navin'

print(type(x))

class PyCharm:
    def execute(self):
        print("Compiling")
        print("executing")

class Myeditor:
    def execute(self):
        print("Spell check")
        print("Convention check")
        print("Compiling")
        print("executing")


class laptop:

    def code(self,ide):   ### here you can see we got ide as attribute
        ide.execute()

ideobj = Myeditor()

lap1 = laptop()
lap2 = laptop()

lap1.code(ideobj)



##### operator overloadling

a = 10
b = 5

print(a+b)  ### the '+' sign calls the inbuilt add
## method which can be accessed as below code

print(int.__add__(a,b))  ### inbuilt add function of integer

c = '5'
d = '6'

print(str.__add__(c,d)) ### inbuilt add function of String

## there are various methods that are inbuilt



class student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self, other):   ### overided inbuilt method to satisfy user defined method
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = student(m1,m2)

        return s3
    def __gt__(self, other):    ### overided inbuilt method to satisfy user defined method
        s1 = self.m1 + self.m2
        s2 = other.m1 + other.m2

        s3 = student(s1,s2)
    def __str__(self):   ### overided inbuilt method to satisfy user defined method
        return '{} {}'.format(self.m1,self.m2)

s1  = student(5,6)
s2 = student(10,5)
s3 = s1 + s2   ### this is getting converted into student.__add__(s1,s2)
print(s3.m1)

if s1 > s2:     ### we can also modify default greater than method
    print("s1 wins")
else:
    print("s2 wins")

a = 8
print(a)

print('s1 :',s1)
print(s2)

### Method overloading and overriding

## python does not support method overloading but there is trick to do it


class calc:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s = a + b + c
        elif a!=None and b!=None:
            s = a + b
        else:
            s = a
        return s

s = calc(58,69)

print(s.sum(21,45))



### method overrriding

class A:

    def show(self):
        print(" in A Show")


class B(A):   ### using inheritance we are
              ### calling method of class A in class B

    def show(self):
        print(" in B Show")


## here when we call a method from sub class then it will search for that method in sub class
## if he finds it ..it will use that method , if that method is not found it will use that of super class
a = B()

a.show()
