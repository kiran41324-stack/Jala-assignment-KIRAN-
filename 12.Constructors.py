# Instantiate the class and call all constructors
class Example:
    def __init__(self, a=None, b=None):
        if a is None and b is None:
            print("Default Constructor Called")
        elif b is None:
            print("One Argument Constructor Called")
            self.a = a
        else:
            print("Two Argument Constructor Called")
            self.a = a
            self.b = b


# class Main:
    def main(self):
        obj1 = Example()          # Default constructor
        obj2 = Example(10)        # One-argument constructor
        obj3 = Example(10, 20)    # Two-argument constructor


# Call Super Class Constructors from Child Class
class Parent:
    def __init__(self, x=None):
        if x is None:
            print("Parent Default Constructor")
        else:
            print("Parent Parameterized Constructor:", x)


class Child(Parent):
    def __init__(self):
        super().__init__()        # Calls parent default constructor
        super().__init__(100)     # Calls parent parameterized constructor
        print("Child Constructor")



# Write a program which illustrates the concept of attributes of a constructor. 
class Student:
    def __init__(self, name, age):
        self.name = name   # instance attribute
        self.age = age     # instance attribute

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)