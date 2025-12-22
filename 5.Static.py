# 1. Define a static variable and access that through a class

class Student:
    college = "ABC Institute"   # Static (class) variable

# Access through class
print(Student.college)

# 2. Define a static variable and access that through a instance

class Student:
    college = "ABC Institute"   # Static variable

s1 = Student()

# Access through instance
print(s1.college)

# 3. Define a static variable and change within the instance
class Student:
    # Static (class) variable
    college_name = "ABC College"

    def change_college(self):
        # Changing static variable using instance
        Student.college_name = "XYZ College"


# Creating objects
s1 = Student()
s2 = Student()

print("Before change:")
print(s1.college_name)
print(s2.college_name)

# Change static variable using one instance
s1.change_college()

print("\nAfter change:")
print(s1.college_name)
print(s2.college_name)
 
# 4. define a static variable and chnge within the class 
class Employee:
    # Static (class) variable
    company_name = "ABC Pvt Ltd"

    @classmethod
    def change_company(cls):
        # Changing static variable within the class
        cls.company_name = "XYZ Pvt Ltd"


# Access before change
print("Before change:", Employee.company_name)

# Change static variable using class method
Employee.change_company()

# Access after change
print("After change:", Employee.company_name)