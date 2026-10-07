'''
Polymorphism
poly


def add(a,b):
    return a + b
def add(a,b,c):
    return a+b+c
def add(a,b,c,d):
    return a+b+c+d
print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40))'''
'''
def add(*values):
    return sum(values)
print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40))
'''
'''
#Operating overloading
class A:
    def __init__(self, value):
        self.x = value

    def __add__(self, val):
        return self.x + val.x

    def __sub__(self, val):
        return self.x - val.x

    def __lt__(self, val):
        return self.x < val.x

a = A(10)
b = A(20)
print(a + b)
print(a - b)
print(a < b)
'''
'''
class B:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self, val):
        return (self.x+val.x,self.y+val.y)
    def __sub__(self, val):
        return (self.x-val.x,self.y-val.y)
a = B(10,20)
b = B(30,40)
print(a+b)
print(a-b)
'''
'''
#method overloading : Same method in both parent and child class
class Parent:
    def display(self):
        print("Parent class display method")
class Child(Parent):
    def display(self):
        print("Child class display method")
c = Child()
c.display()#child class method
Parent.display(c)#parent class method
'''

#Duck Typing
'''class Dog:
    def Sounds(self):
        print("Bark")
class Cat:
    def Sounds(self):
        print("Meow")

def make_sound(animal):
    animal.Sounds()

d = Dog()
c = Cat()
make_sound(d)
make_sound(c)
'''