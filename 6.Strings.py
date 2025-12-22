# STRING OPERATIONS IN PYTHON

import re

# 1. Different ways of creating a string
s1 = "Hello"
s2 = 'World'
s3 = """This is
a multi-line string"""
s4 = str("Python")

print("1. Strings:")
print(s1, s2, s3, s4)

# 2. Concatenating two strings using + operator
a = "Hello"
b = "Python"
print("\n2. Concatenation:", a + " " + b)

# 3. Finding the length of the string
text = "Bright IT Career"
print("\n3. Length of string:", len(text))

# 4. Extract a string using Substring (slicing)
text2 = "PythonProgramming"
substring = text2[0:6]
print("\n4. Substring:", substring)

# 5. Searching in strings using index()
text3 = "Python Programming"
print("\n5. Index of 'Program':", text3.index("Program"))

# 6. Matching a String Against a Regular Expression (matches)
pattern = "[A-Za-z0-9]+"
string = "Python123"

print("\n6. Regex Match:")
if re.fullmatch(pattern, string):
    print("String matches the pattern")
else:
    print("String does not match the pattern")

# 7. Comparing strings
str1 = "apple"
str2 = "banana"
print("\n7. String Comparison:")
print("Equal:", str1 == str2)
print("Less than:", str1 < str2)
print("Greater than:", str1 > str2)

# 8. startsWith(), endsWith() and compareTo()
text4 = "Python Programming"
print("\n8. startsWith & endsWith:")
print(text4.startswith("Python"))
print(text4.endswith("Programming"))

# compareTo equivalent
compare_result = (text4 > "Java") - (text4 < "Java")
print("compareTo result:", compare_result)

# 9. Trimming strings with strip()
text5 = "   Hello World   "
print("\n9. Trimmed string:", text5.strip())

# 10. Replacing characters in strings with replace()
text6 = "Hello World"
print("\n10. Replace:", text6.replace("World", "Python"))

# 11. Splitting strings with split()
text7 = "Python is very easy"
print("\n11. Split:", text7.split(" "))

# 12. Converting integer objects to Strings
num = 100
string_num = str(num)
print("\n12. Integer to String:", string_num)

# 13. Converting to uppercase and lowercase
text8 = "Python Programming"
print("\n13. Uppercase:", text8.upper())
print("Lowercase:", text8.lower())