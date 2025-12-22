# 1. Create a class with PRIVATE fields, private method and a main method. Print the fieldsin main method. Call the private method in main method.
class Demo:
    def __init__(self):
        # Private fields
        self.__name = "Saurabh"
        self.__age = 25

    # Private method
    def __show_details(self):
        print("This is a private method")

    # Main method
    def main(self):
        # Printing private fields
        print("Name:", self.__name)
        print("Age:", self.__age)

        # Calling private method
        self.__show_details()


# Execution
if __name__ == "__main__":
    d = Demo()
    d.main()

#. Create a sub class and try to access the private fields and methods from sub class.
# Parent class
class Parent:
    def __init__(self):
        # Private field
        self.__salary = 50000

    # Private method
    def __show_salary(self):
        print("Salary:", self.__salary)


# Sub class
class Child(Parent):
    def access_private(self):
        print("Trying to access private members from Child class")

        # ❌ Direct access (NOT allowed)
        # print(self.__salary)
        # self.__show_salary()

        # ✅ Access using name mangling
        print("Accessing private field:", self._Parent__salary)
        self._Parent__show_salary()


#execut

# 2. Create a class with PROTECTED fields and methods. Access these fields and methods from any other class in the same package
class Base:
    def __init__(self):
        # Protected field
        self._data = "Protected Data"

    # Protected method
    def _show(self):
        print("Protected method of Base class")

# Access PROTECTED Members from Another Class in the SAME Packagefrom base import Base

class SamePackageClass:
    def access_protected(self):
        obj = Base()
        print(obj._data)
        obj._show()


# Execution
if __name__ == "__main__":
    sp = SamePackageClass()
    sp.access_protected()

# Access PROTECTED Members from CHILD Class in DIFFERENT Package from package1.base import Base

class Child(Base):
    def access_protected(self):
        print(self._data)
        self._show()


# Execution
if __name__ == "__main__":
    c = Child()
    c.access_protected()

# Access PROTECTED Members from ANY Class in DIFFERENT Package from package1.base import Base

class OtherClass:
    def access_protected(self):
        obj = Base()
        print(obj._data)
        obj._show()


# Execution
if __name__ == "__main__":
    o = OtherClass()
    o.access_protected()

# 3. Create a Class with PUBLIC Fields and Methods
class PublicClass:
    def __init__(self):
        # Public field
        self.name = "Public User"

    # Public method
    def show_name(self):
        print("Name:", self.name)

# Access PUBLIC Members from Another Class in the SAME Package from public_class import PublicClass

class SamePackageClass:
    def access_public(self):
        obj = PublicClass()
        print(obj.name)      # Accessing public field
        obj.show_name()      # Accessing public method


# Execution
if __name__ == "__main__":
    sp = SamePackageClass()
    sp.access_public()

# Access PUBLIC Members from ANY Class in a DIFFERENT Package from package1.public_class import PublicClass

class OtherPackageClass:
    def access_public(self):
        obj = PublicClass()
        print(obj.name)      # Accessing public field
        obj.show_name()      # Accessing public method


# Execution
if __name__ == "__main__":
    op = OtherPackageClass()
    op.access_public()