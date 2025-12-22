# 1. Write a program to print “Bright IT Career” ten times using for loop

for i in range(10):
    print("Bright IT Career")

# 2. Write a java program to print 1 to 20 numbers using the while loop.

i = 1
while i <= 20:
    print(i)
    i += 1

# 3. Program to equal operator and not equal operators

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("a == b :", a == b)
print("a != b :", a != b)

# 4. Write a program to print the odd and even numbers.

for i in range(1, 11):
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")

# 5. Write a program to print largest number among three numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)

# 6. Write a program to print even number between 10 and 20 using while

num = 10
while num <= 20:
    if num % 2 == 0:
        print(num)
    num += 1

# 7. Write a program to print 1 to 10 using the do-while loop statement.

i = 1
while True:
    print(i)
    i += 1
    if i > 10:
        break

# 8. Write a program to find Armstrong number or not

num = int(input("Enter a number: "))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if sum == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

# 9. Write a program to find the prime or not.

num = int(input("Enter a number: "))
flag = True

if num <= 1:
    flag = False
else:
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break

if flag:
    print("Prime Number")
else:
    print("Not a Prime Number")

# 10. Write a program to palindrome or not.

num = input("Enter a number: ")

if num == num[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

# 11. Program to check whether a number is EVEN or ODD using switch

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 12. Print gender (Male/Female) program according to given M/F using switch

gender = input("Enter gender (M/F): ")

if gender == 'M' or gender == 'm':
    print("Male")
elif gender == 'F' or gender == 'f':
    print("Female")
else:
    print("Invalid input")