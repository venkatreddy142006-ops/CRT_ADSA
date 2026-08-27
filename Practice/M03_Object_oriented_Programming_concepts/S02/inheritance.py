'''
Inheritance = Accuring properities from one class to another class
Types of inheritance:
1. Single
2. Multi-level
3. Hierarchical
4. Mulitple
5. Hybrid
'''
'''
class A:
    def display1(self):
        print("This is class A display method")
class B:
    def display2(self):
        print("This is class B display method")
b = B()
b.display1()
b.display2()

'''
'''
# Multi-level
class A:
    def display1(self):
        print("This is class A display method")
class B:
    def display2(self):
        print("This is class B display method")
class C:
    def display3(self):
        print("This is class C display method")
b = B()
b.display1()
b.display2()
b.display3()
'''
'''
#Multiple
class A:
    def display(self):
        print("This is class A display method")
class B:
    def display(self):
        print("This is class B display method")
class C(A,B):
    def display3(self):
        print("This is class C display method")
c = C()
c.display()
'''
#MRO - Method Resolution Order
