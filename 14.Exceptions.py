#1. Write a program to generate a Arithmetic Exception witthout exception handling

def cause_arithmetic_error():
    """
    Attempts a division by zero operation, which Python raises 
    a ZeroDivisionError for automatically.
    """
    numerator = 10
    denominator = 0
    result = numerator / denominator
    # The line above will raise a ZeroDivisionError, 
    # so the following print statement will not be executed.
    print(f"The result is: {result}")

if __name__ == "__main__":
    print("Attempting to cause an Arithmetic Exception...")
    cause_arithmetic_error()
    print("This line will not be printed because the program will terminate.")

#2. Handle the Arithmetic Exception using try-catch block

try:
    # Code that might raise an arithmetic exception (e.g., division by zero)
    numerator = 10
    denominator = 0
    result = numerator / denominator
    print(f"Result: {result}")
except ZeroDivisionError as e:
    # Code to handle the specific error
    print(f"Error: Cannot divide by zero. Details: {e}")

#3. Write a method which throws exception, call that method in main class without try block

def throw_exception_method():
    """
    This method raises a ValueError when called.
    """
    print("Method is about to raise an exception.")
    # You can raise any built-in or custom exception
    raise ValueError("This is an intentional exception thrown from the method.")

# This is the main part of the script (often considered the 'main class' context in Python)

print("Program started.")

# Calling the method without a try...except block
throw_exception_method() 

print("This line will not be executed.")

#4. Write a program with multiple catch blocks

def get_user_input_and_divide():
    try:
        # Ask the user for two numbers
        first = float(input("What is your first number? "))
        second = float(input("What is your second number? "))
        
        # Perform the division
        result = first / second
        print(f"The result of {first} divided by {second} is {result}")

    except ValueError:
        # This block runs if float() fails (e.g., user enters a letter)
        print("Error: You must enter a valid number (digits only).")

    except ZeroDivisionError:
        # This block runs if division by zero occurs
        print("Error: You can't divide by zero.")

    except Exception as e:
        # This generic block catches any other exceptions not covered above
        print(f"An unexpected error occurred: {e}")

# Run the function
get_user_input_and_divide()


#5. Write a program to throw exception with your own message

try:
    # Code that might encounter an issue
    raise ValueError("This is my custom error message.")
except ValueError as e:
    # Code to handle the exception
    print(f"An exception occurred: {e}")


    #6. Write a program to create your own exception

    class InvalidAgeError(Exception):
        """Exception raised for invalid age values."""

    def __init__(self, age, message="Age must be between 0 and 120"):
        self.age = age
        self.message = message
        # Call the base class constructor with the custom message
        super().__init__(self.message)

    def __str__(self):
        """Customize the string representation of the exception."""
        return f"{self.message}. Provided age: {self.age}"

def validate_age(age):
    """Function to validate age and raise a custom exception if invalid."""
    if not isinstance(age, int):
        raise TypeError("Age must be an integer.")
    if age < 0 or age > 120:
        raise InvalidAgeError(age)
    print(f"Age {age} is valid.")

# Main program to demonstrate raising and handling the exception
try:
    # Example of a valid age
    validate_age(50)
    
    # Example that raises InvalidAgeError
    validate_age(150)
    
except InvalidAgeError as e:
    # Catch and handle the specific custom exception
    print(f"Caught an error: {e}")
    
except TypeError as e:
    # Catch any other specific exceptions
    print(f"Caught a type error: {e}")

else:
    # This block runs if no exceptions were raised in the try block
    print("No custom age errors occurred in the first two checks.")

finally:
    # This block always runs, regardless of exceptions
    print("Age validation process finished.")


#7. Write a program with finally block

def divide_numbers(a, b):
    try:
        print(f"Attempting division: {a} / {b}")
        result = a / b
        print("Division successful.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    finally:
        # This code block always runs
        print("Executing the finally block (cleanup/guaranteed tasks).")
    
    # Code after the try...except...finally block also runs if the exception is handled
    print("Program continues after the try block structure.\n")

# --- Example 1: No exception occurs ---
divide_numbers(10, 2)

# --- Example 2: An exception occurs ---
divide_numbers(10, 0)


#8. Write a program to generate arithmetic exception 

# Program to generate a ZeroDivisionError (a type of ArithmeticError)

numerator = 10
denominator = 0

print(f"Attempting to divide {numerator} by {denominator}...")

# This line will raise a ZeroDivisionError
result = numerator / denominator

print("This line will not be executed if an exception occurs.")


#9. Write a program to generrate file not found exception

try:
    # Attempt to open a file that does not exist
    with open('non_existent_file.txt', 'r') as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"Caught the exception: {e}")
    print(f"Exception type: {type(e)}")

#10. Write a program to generate class not found exception

# This code will raise a NameError

try:
    # Attempt to create an instance of a non-existent class
    my_instance = NonExistentClass()
except NameError as e:
    # Catch the exception and print the error message
    print(f"An error occurred: {e}")
    print(f"The type of exception is: {type(e).__name__}")

# Example Output:
# An error occurred: name 'NonExistentClass' is not defined
# The type of exception is: NameError

#11. Write a program to generate IOException

def raise_io_error():
    """
    Raises an IOError (which is an alias for OSError) explicitly.
    """
    print("Attempting to raise an IOError...")
    # In modern Python 3, IOError is an alias of OSError
    raise IOError("This is a simulated IOError message.")

try:
    raise_io_error()
except IOError as e:
    print(f"Caught the exception: {e}")
    print(f"Type of the exception: {type(e)}")

#12. Write a program to generate NoSuchField exception

class MyClass:
    """A simple class with one field."""
    existing_field = "This field exists"

# Create an instance of the class
obj = MyClass()

print(f"Accessing existing field: {obj.existing_field}")

try:
    # Attempt to access a field that does not exist
    print(f"Attempting to access non_existent_field: {obj.non_existent_field}")
except AttributeError as e:
    # Catch the expected AttributeError
    print(f"\nCaught the exception: {e}")
    print("This is the Python equivalent of Java's NoSuchFieldException.")

# You can also use reflection-like methods (getattr) to cause a similar issue
try:
    getattr(obj, 'another_non_existent_field')
except AttributeError as e:
    print(f"\nCaught the exception using getattr: {e}")

