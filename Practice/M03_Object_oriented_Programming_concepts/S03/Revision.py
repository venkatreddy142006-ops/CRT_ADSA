'''# Take a family tree and apply all 5 types of inheritance
# Single Inherirtance
class Parent:
    def show(self):
        print("This is Parent class")

class Child(Parent):
    def display(self):
        print("This is Child class")

obj = Child()
obj.show()     
obj.display()  

# Multilevel Inheritance
class Grandparent:
    def feature1(self):
        print("Feature from Grandparent")

class Parent(Grandparent):
    def feature2(self):
        print("Feature from Parent")

class Child(Parent):
    def feature3(self):
        print("Feature from Child")

obj = Child()
obj.feature1()
obj.feature2()
obj.feature3()

# Multiple Inheritance
class Father:
    def skill1(self):
        print("Father's skill")

class Mother:
    def skill2(self):
        print("Mother's skill")

class Child(Father, Mother):
    def skill3(self):
        print("Child's skill")

obj = Child()
obj.skill1()
obj.skill2()
obj.skill3()

# Hierarchical Inheritance
class Parent:
    def common(self):
        print("Common feature")

class Child1(Parent):
    def feature1(self):
        print("Child1 feature")

class Child2(Parent):
    def feature2(self):
        print("Child2 feature")

obj1 = Child1()
obj2 = Child2()
obj1.common()
obj2.common()

# Hybrid Inheritance
class A:
    def showA(self):
        print("Class A")

class B(A):
    def showB(self):
        print("Class B")

class C(A):
    def showC(self):
        print("Class C")

class D(B, C):   # multiple + hierarchical
    def showD(self):
        print("Class D")

obj = D()
obj.showA()
obj.showB()
obj.showC()
obj.showD()
'''
# Encapsulation
'''
class A:
    def S(self):   
        print('A')

class B:
    def S(self):   
        print('B')

def K(shape):
    shape.S()      

a = A()
b = B()
K(a)
K(b)   
'''

