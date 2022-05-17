import ctypes
import sys

## what is A Class:
##              A Class is nothing but Collection of Attributes and Methods to perform some specific task

# class Game:
#     def type(self):
#         print('FPS')
#
#
# a = 8
#
# ###---Creating an Object of Class to call the class easily
#
# g = Game()
# h = 0
# i = Game()
# print(id(a))

# print(ctypes.cast(id(a),ctypes.py_object).value)
# ### -- Calling the parameter using class
#
# Game.type(g)
# Game.type(h)
#
#
# ### now you can call methods of a class
#
# g.type()
# i.type()

### Now for next example declaring a class name Computer and defining init inside it



class Computer:

    harddisk = 'WD'

### this is an inbuilt method but we can use it according to our needs
    def __init__(self,cpu,ram):  ### declaring two parameters so that we can pass any value when calling our class methods
        self.cpu = cpu
        self.ram = ram
        print('auto called ..!')

    def type1(self):
        print('laptop : ', self.cpu, self.ram)  ### here calling our declared parameters
    def type2(self):
        print('PC : ', self.cpu, self.ram)
###  below here assigning our values for pre defined parameters...sequence is important

conf1 = Computer('ryzen 5','8 GB')
conf2 = Computer('intel i7','16 GB')

conf1.type1()
conf2.type2()

### learning more about constructors and __init__

class Car:
    wheels = 10
    def __init__(self):
        self.avg = 10
        self.com = 'Audi'


c1 = Car()
c2 = Car()

c1.com = 'BMW'
c2.avg = '20'

print(c1.avg,c1.com,c1.wheels,c2.avg,c2.com,c2.wheels)


class Student:
    school = 'MT. High'
    def __init__(self,m1,m2,m3):  ### instance variables to work with instance methods
            self.m1 = m1
            self.m2 = m2
            self.m3 = m3

    def avg(self):               ### this is instance method which will be called later on
        return (self.m1+self.m2+self.m3)/3


    @classmethod
    def getschool(cls):               ### Class method with decorator ....(wihout decorator it wont work)
        return cls.school

    @staticmethod
    def info():
        print('Student class with info as Static method')

s1 = Student(10,23,15)
s2 = Student(34,67,34)


print(s1.avg())
print(s2.avg())

print(Student.getschool())

Student.info()

