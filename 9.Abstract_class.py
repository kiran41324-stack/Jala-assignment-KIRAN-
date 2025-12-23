#Create an abstract class with abstract and non-abstract methods.from abc import ABC, abstractmethod
from abc import ABC, abstractmethod
# Abstract class
class Shape(ABC):

    # Abstract method
    @abstractmethod
    def draw(self):
        pass

    # Non-abstract method
    def info(self):
        print("This is a Shape class")


# Create a sub class for an abstract class. Create an object in the child class for the abstract class and access the non-abstract methods
class Circle(Shape):

    # Implementing abstract method
    def draw(self):
        print("Drawing a Circle")

    @staticmethod
    def main():
        # Abstract class reference, Child class object
        shape_obj = Circle()
        shape_obj.info()   # Calling non-abstract method



 # Create an instance for the child class in child class and call abstract methods      
        # Calling abstract method using child class instance
        shape_obj.draw()


# Create instance of Child class & call NON-abstract method
        # Calling non-abstract method
        shape_obj.info()


# Running main method
Circle.main()




# Complete Combined Code of all Four queries of abstrect class

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def draw(self):
        pass

    def info(self):
        print("This is a Shape class")


class Circle(Shape):

    def draw(self):
        print("Drawing a Circle")

    @staticmethod
    def main():
        # Abstract class reference, Child class object
        shape_obj = Circle()

        # Calling non-abstract method
        shape_obj.info()

        # Calling abstract method
        shape_obj.draw()

        # Calling non-abstract method again
        shape_obj.info()



Circle.main()
