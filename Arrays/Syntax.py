import array as arr

# creating an array with integer type
my_array = arr.array('i', [1, 2, 3, 4, 5])

# accessing elements of the array
print(my_array[0])

# modifying an element in the array
my_array[1] = 10
print(my_array)

# appending an element to the array
my_array.append(6)
print(my_array)

# inserting an element at a specific position
my_array.insert(2, 20)
print(my_array)

# removing an element from the array
my_array.remove(10)
print(my_array)

# slicing the array
sliced_array = my_array[1:4]
print(sliced_array)

# iterating through the array
for element in my_array:
    print(element)

# getting the length of the array
print(len(my_array))

# converting the array to a list
array_list = my_array.tolist()