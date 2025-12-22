# Definition of ClassOne
class ClassOne:
    def __init__(self):
        print("ClassOne Constructor Called")

    def method_one(self):
        print("Method of ClassOne")

# Definition of ClassTwo
class ClassTwo:
    def __init__(self):
        print("ClassTwo Constructor Called")

    def method_two(self):
        print("Method of ClassTwo")

# Example import statements (uncomment as needed for your specific project structure)
# from .classone import ClassOne
# from .classtwo import ClassTwo
# from mypackage import ClassOne, ClassTwo

def main():
    # Creating object of ClassOne
    obj1 = ClassOne()
    obj1.method_one()

    # Creating object of ClassTwo
    obj2 = ClassTwo()
    obj2.method_two()

# Running main function if the script is executed directly
if __name__ == "__main__":
    main()
