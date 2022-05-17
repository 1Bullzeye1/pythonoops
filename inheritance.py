class A:
    def __init__(self):         ### inheritance constructor to be called in sub class
        print("init class A ...! ")
    def feature1(self):
        print('feature 1 on ..!')
    def feature2(self):
        print('feature 2 on ..!')

class B():

    # def __init__(self):
    #     super().__init__()      ### constructor of inherited super class A
    #     print("Init Class B....!")
    def __init__(self):
        print("Init class B...!")
    def feature3(self):
        print('feature 3 on ..!')

    def feature4(self):
        print('feature 4 on ..!')

# class C(A):     ### single level inheritance
#     def feature1(self):
#         print('feature 1 on ..!')
#
# class C(B):     ### multilevel inheritance when B inherits from A
#         def feature5(self):
#             print('feature 5 in on..!')

# class C(A,B):   ### Multiple inheritance
#         def feature5(self):
#             print('feature 5 in on...!')

class C(A,B):
    def __init__(self):  ### multiple inherited constructor goes from left to right
        super().__init__()
        print("init Class C...!")

    def feat(self):
        super().feature2()

b = B()    ### created object of class
b

f = C()
f.feat()   ### called method from super class 


