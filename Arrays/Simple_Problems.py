import array as arr

# 1. Print all elements of an array.

numbers = arr.array('i', [1, 2, 3, 4, 5])

print("Elements of the array:", end=' ')
for num in numbers:
    print(num, end=' ')


# 2. Find the sum of all elements.

def sum_of_array(arrays):
    sum = 0
    for num in arrays:
        sum += num
    return sum

print("\nSum of all elements:", sum_of_array(numbers))

# 3. Find the average of elements.

def average_of_array(arr):
    sum = sum_of_array(arr)
    return sum / len(arr)

print("Average of elements:", average_of_array(numbers))



# 4. Find the maximum element.

def max_of_array(arr):
    max_value = arr[0]
    for num in arr:
        if num > max_value:
            max_value = num
    return max_value

print("Maximum element:", max_of_array(numbers))


# 5. Find the minimum element.
def min_of_array(arr):
    min_value = arr[0]
    for num in arr:
        if num < min_value:
            min_value = num
    return min_value

print("Minimum element:", min_of_array(numbers))

# 6. Count even numbers in an array.
def count_even_numbers(arr):
    count = 0
    for num in arr:
        if num % 2 == 0:
            count += 1
    return count

print("Count of even numbers:", count_even_numbers(numbers))

# 7. Count odd numbers in an array.
def count_odd_numbers(arr):
    count = 0
    for num in arr:
        if num % 2 != 0:
            count += 1
    return count

print("Count of odd numbers:", count_odd_numbers(numbers))

# 8. Search for a given element (linear search).
def search_element(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i  # Return index if found
    return -1  # Return -1 if not found

target = 3
index = search_element(numbers, target)
if index != -1:
    print(f"Element {target} found at index {index}")
else:
    print(f"Element {target} not found in the array")

# 9. Check if an element exists in the array.

def element_exists(arr, target):
    for num in arr:
        if num == target:
            return True
    return False    

target = 4
print(f"Element {target} exists in the array:", element_exists(numbers, target))

# 10. Reverse the array.
def reverse_array(arr):
    reversed_arr = arr[::-1]
    return reversed_arr
print("Reversed array:", reverse_array(numbers))

# Instead of using slicing to reverse the array, we can also use a loop to reverse it in place:

def reverse_array_in_place(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr  

print("Reversed array (in place):", reverse_array_in_place(numbers))

# 11. Copy one array into another.
def copy_array(arr):
    copied_arr = arr[:]
    return copied_arr

copied_numbers = copy_array(numbers)
print("Copied array:", copied_numbers)

# Instead of using slicing to copy the array, we can also use a loop to copy it element by element:
def copy_array_with_loop(array):
    copied_arr = arr.array('i', [0] * len(array))  # Create an empty array of the same type
    for i in range(len(array)):
        copied_arr[i] = array[i]
    return copied_arr

copied_numbers_with_loop = copy_array_with_loop(numbers)
print("Copied array (with loop):", copied_numbers_with_loop)

# 12. Find the second largest element.
def second_largest(arr):
    if len(arr) < 2:
        return None
    max_val = second_max = 0
    for num in arr:
        if num > max_val:
            second_max = max_val
            max_val = num
        elif num > second_max and num != max_val:
            second_max = num
    return second_max

print("Second largest element:", second_largest(numbers))


# 13. Check if the array is sorted.
reverse_array_in_place(numbers)

def is_sorted(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True

print("Is the array sorted?", is_sorted(numbers))


# 14. Count how many times a number appears

def count_occurrences(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count

target = 2
print(f"Number {target} appears {count_occurrences(numbers, target)} times in the array")

# 15. Find the index of a given element.

def find_index(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

target = 5
index = find_index(numbers, target)

# Instead of enumerate, we can also use a simple loop to find the index of the target element:

def find_index_with_loop(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

index_with_loop = find_index_with_loop(numbers, target)


# 16. Remove duplicates (basic way).
def remove_duplicates(arr):
    unique_elements = []
    for num in arr:
        if num not in unique_elements:
            unique_elements.append(num)
    return unique_elements

print("Array after removing duplicates:", remove_duplicates(numbers))

# Instead of using a list to store unique elements, we can also use a set to remove duplicates more efficiently:

def remove_duplicates_with_set(arr):
    unique_elements = set()
    for num in arr:
        unique_elements.add(num)
    return list(unique_elements)

print("Array after removing duplicates (with set):", remove_duplicates_with_set(numbers))


# 17. Move all zeros to the end.
def move_zeros_to_end(array):
    non_zero_index = 0
    for i in range(len(array)):
        if array[i] != 0:
            array[non_zero_index] = array[i]
            non_zero_index += 1
    for i in range(non_zero_index, len(array)):
        array[i] = 0
    return array

numbers_with_zeros = arr.array('i', [0, 1, 0, 3, 12])
print("Array after moving zeros to the end:", move_zeros_to_end(numbers_with_zeros))


# 18. Find the difference between max and min.
def difference_max_min(array):

    min = array[0]
    max = array[0]

    for i in array:
        if i < min:
            min = i
        elif i > max:
            max = i
    return max - min

print("Difference between max and min:", difference_max_min(numbers))


# 19. Find the largest and smallest in one traversal.
def largest_and_smallest(array):
    if len(array) == 0:
        return None, None
    min = array[0]
    max = array[0]

    for i in array:
        if i < min:
            min = i
        elif i > max:
            max = i
    return max, min

largest, smallest = largest_and_smallest(numbers)
print("Largest element:", largest)
print("Smallest element:", smallest)


# 20. Replace negative numbers with 0.
def replace_negatives_with_zero(array):
    for i in range(len(array)):
        if array[i] < 0:
            array[i] = 0
    return array

numbers_with_negatives = arr.array('i', [-1, 2, -3, 4, -5])
print("Array after replacing negative numbers with 0:", replace_negatives_with_zero(numbers_with_negatives))


# 21. Find the first repeating element.
def first_repeating_element(array):
    seen = set()
    for num in array:
        if num in seen:
            return num
        seen.add(num)
    return None

numbers_with_repeats = arr.array('i', [1, 2, 3, 2, 4, 5])
print("First repeating element:", first_repeating_element(numbers_with_repeats))


# 22. Find the first non-repeating element.
def first_non_repeating_element(array):
    count = {}
    for num in array:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    for num in array:
        if count[num] == 1:
            return num
    return None

numbers_with_repeats = arr.array('i', [1, 2, 3, 2, 4, 5])
print("First non-repeating element:", first_non_repeating_element(numbers_with_repeats))


# 23. Check if two arrays are equal.
def are_arrays_equal(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True

array1 = arr.array('i', [1, 2, 3])
array2 = arr.array('i', [1, 2, 3])
print("Are the two arrays equal?", are_arrays_equal(array1, array2))