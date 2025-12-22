# 1. Create three methods in each class, 2 methods are specific to each class and thirdmethod (override method) should be in all three Classes A, B and C
# Super class
class A:
    def method_a1(self):
        print("Class A - Method 1")

    def method_a2(self):
        print("Class A - Method 2")

    # Overridden method
    def display(self):
        print("Display method from Class A")


# Sub class of A
class B(A):
    def method_b1(self):
        print("Class B - Method 1")

    def method_b2(self):
        print("Class B - Method 2")

    # Overridden method
    def display(self):
        print("Display method from Class B")


# Sub class of B
class C(B):
    def method_c1(self):
        print("Class C - Method 1")

    def method_c2(self):
        print("Class C - Method 2")

    # Overridden method
    def display(self):
        print("Display method from Class C")


# Creating object of Class C
obj = C()

# Calling methods
obj.method_a1()
obj.method_b1()
obj.method_c1()

print("\nCalling overridden method:")
obj.display()

# 2. Create a class with main method. Create an object for each class A, B and C in mainmethod and call every method of each class using its own object/instance
# Super class
class A:
    def a_method1(self):
        print("Class A - Method 1")

    def a_method2(self):
        print("Class A - Method 2")

    def display(self):
        print("Display method from Class A")


# Sub class of A
class B(A):
    def b_method1(self):
        print("Class B - Method 1")

    def b_method2(self):
        print("Class B - Method 2")

    def display(self):
        print("Display method from Class B")

# 3. Call an overridden method with super class reference to B and C class’s objects
# Super class
class A:
    def display(self):
        print("Display method from Class A")


# Sub class of A
class B(A):
    def display(self):
        print("Display method from Class B")


# Sub class of B
class C(B):
    def display(self):
        print("Display method from Class C")


# Main execution
if __name__ == "__main__":

    # Super class reference to B object
    ref1 = A()
    ref1 = B()
    ref1.display()

    # Super class reference to C object
    ref2 = A()
    ref2 = C()
    ref2.display()

# 4. Runtime Polymorphism with Data Members/Instance variables, Repeat the aboveprocess only for data members
# Super class
class A:
    def __init__(self):
        self.value = "Value from Class A"


# Sub class of A
class B(A):
    def __init__(self):
        super().__init__()
        self.value = "Value from Class B"


# Sub class of B
class C(B):
    def __init__(self):
        super().__init__()
        self.value = "Value from Class C"


# Main execution
if __name__ == "__main__":

    # Super class reference to B object
    ref1 = B()
    print(ref1.value)

    # Super class reference to C object
    ref2 = C()
    print(ref2.value)