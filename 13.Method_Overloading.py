class Printer:
    def display(self, a, b=None):
        if b is not None:
            print(f"Called with two parameters: {a} and {b}")
        else:
            print(f"Called with one parameter: {a}")

# Create an instance of the class
p = Printer()

# Call the method with one parameter
p.display(10)

# Call the method with two parameters
p.display(10, 20)


class Person:
    def display_info(self, name, age=None):
        """
        Method that demonstrates overloading behavior using default parameters.
        Accepts one required parameter and one optional parameter.
        """
        if age is not None and isinstance(age, int):
            print(f"Method 1 (Two parameters: str, int): Name: {name}, Age: {age}")
        else:
            print(f"Method 2 (One parameter: str): Name: {name}")

# Create an instance of the class
person = Person()

# Call the method with one parameter (the 'one parameter' version is used)
person.display_info("Alice")

# Call the method with two parameters (the 'two parameters' version is used)
person.display_info("Bob", 30)


class Printer:
    def display(self, message, format_type=None):
        """
        A single method that handles different 'overloads' 
        using a default argument.
        """
        if format_type is None:
            # Case 1: Called with one argument (e.g., display("hello"))
            print(f"Simple Display: {message}")
        else:
            # Case 2: Called with two arguments (e.g., display("hello", "bold"))
            print(f"Formatted Display ({format_type}): {message}")

# Usage:
p = Printer()
p.display("Hello World") 
p.display("Hello World", "bold")

