# Reading a text file
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()



# Writing user input to a text file
text = input("Enter text to write into file: ")

file = open("output.txt", "w")
file.write(text)
file.close()

print("Data written successfully")



# Write a program to read a file stream 
file = open("sample.txt", "r")

for line in file:
    print(line, end="")

file.close()


# Random access file reading
file = open("sample.txt", "r")

file.seek(0)          # Move to beginning
print(file.read(10))  # Read first 10 characters

file.seek(20)         # Move to 20th byte
print(file.read(10))  # Read next 10 characters

file.close()


# Read from a specific index
file = open("sample.txt", "r")

file.seek(5)      # Move cursor to index 5
print(file.read())  # Read from index 5 till end

file.close()


# Program to CHECK READ & WRITE PERMISSIONS of a file
import os

file_path = "sample.txt"

# Check read permission
if os.access(file_path, os.R_OK):
    print("File has READ permission")
else:
    print("File does NOT have READ permission")

# Check write permission
if os.access(file_path, os.W_OK):
    print("File has WRITE permission")
else:
    print("File does NOT have WRITE permission")