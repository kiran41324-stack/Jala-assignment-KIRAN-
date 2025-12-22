# 1. Write a function for arithmetic operators(+,-,*,/)
def arithmetic_operations(a, b):
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    
    if b != 0:
        print("Division:", a / b)
    else:
        print("Division: Not possible (division by zero)")

# Function call
arithmetic_operations(10, 5)


# 2. Write a method for increment and decrement operators(++, --)

def increment_decrement(num):
    num += 1   # Increment
    print("After Increment:", num)

    num -= 1   # Decrement
    print("After Decrement:", num)

# Function call
increment_decrement(10)



# 3. Write a program to find the two numbers equal or not.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a == b:
    print("Both numbers are equal")
else:
    print("Both numbers are not equal")


# 4. Program for relational operators (<,<==, >, >==)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("x < y :", x < y)
print("x <= y :", x <= y)
print("x > y :", x > y)
print("x >= y :", x >= y)



# 5. Print the smaller and larger number

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Larger number:", a)
    print("Smaller number:", b)
elif b > a:
    print("Larger number:", b)
    print("Smaller number:", a)
else:
    print("Both numbers are equal")