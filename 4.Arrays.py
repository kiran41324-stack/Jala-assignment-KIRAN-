arr = [10, 20, 30, 20, 40, 10, 50]

# 1. Write a function to add integer values of an array

def array_sum(arr):
    return sum(arr)

print(array_sum(arr))

# 2. Write a function to calculate the average value of an array of integers

def array_average(arr):
    return sum(arr) / len(arr)

print(array_average(arr))

# 3. Write a program to find the index of an array element

element = 30
print(arr.index(element))

# 4. Write a function to test if array contains a specific value

def contains_value(arr, value):
    return value in arr

print(contains_value(arr, 20))

# 5. Write a function to remove a specific element from an array

def remove_element(arr, value):
    if value in arr:
        arr.remove(value)
    return arr

print(remove_element(arr.copy(), 20))

# 6. Write a function to copy an array to another array

def copy_array(arr):
    return arr.copy()

new_arr = copy_array(arr)
print(new_arr)

# 7. Write a function to insert an element at a specific position in the array

def insert_element(arr, index, value):
    arr.insert(index, value)
    return arr

print(insert_element(arr.copy(), 2, 99))

# 8. Write a function to find the minimum and maximum value of an array

def min_max(arr):
    return min(arr), max(arr)

print(min_max(arr))

# 9. Write a function to reverse an array of integer values

def reverse_array(arr):
    return arr[::-1]

print(reverse_array(arr))

# 10. Write a function to find the duplicate values of an array

def find_duplicates(arr):
    duplicates = []
    for i in arr:
        if arr.count(i) > 1 and i not in duplicates:
            duplicates.append(i)
    return duplicates

print(find_duplicates(arr))

# 11. Write a program to find the common values between two arrays

arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]

common = list(set(arr1) & set(arr2))
print(common)

# 12. Write a method to remove duplicate elements from an array

def remove_duplicates(arr):
    return list(set(arr))

print(remove_duplicates(arr))

# 13. Write a method to find the second largest number in an array

def second_largest(arr):
    unique = list(set(arr))
    unique.sort()
    return unique[-2]

print(second_largest(arr))

# 14. Write a method to find the second largest number in an array

print(second_largest(arr))

# 15. Write a method to find number of even number and odd numbers in an array

def even_odd_count(arr):
    even = odd = 0
    for i in arr:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

print(even_odd_count(arr))

# 16. Write a function to get the difference of largest and smallest value

def max_min_difference(arr):
    return max(arr) - min(arr)

print(max_min_difference(arr))

# 17. Write a method to verify if the array contains two specified elements(12,23)

def contains_elements(arr):
    return 12 in arr and 23 in arr

print(contains_elements(arr))

# 18. Write a program to remove the duplicate elements and return the new array

def unique_array(arr):
    new_arr = []
    for i in arr:
        if i not in new_arr:
            new_arr.append(i)
    return new_arr

print(unique_array(arr))