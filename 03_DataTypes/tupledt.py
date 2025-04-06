# What is a Tuple in Python?
# A tuple is an immutable sequence type in Python, meaning its elements cannot be changed after creation.
# Tuples are used to store multiple items in a single variable and are defined using parentheses ().
# They are similar to lists but are immutable, making them useful for data that should not be modified.

# Example of creating a tuple
example_tuple = (1, 2, 3, 4, 5)
print("Example Tuple:", example_tuple)

# Accessing elements in a tuple
print("First element:", example_tuple[0])
print("Last element:", example_tuple[-1])

# Tuple operations
# 1. Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print("Concatenated Tuple:", concatenated_tuple)

# 2. Repetition
repeated_tuple = tuple1 * 2
print("Repeated Tuple:", repeated_tuple)

# 3. Membership testing
print("Is 2 in tuple1?", 2 in tuple1)
print("Is 7 in tuple1?", 7 in tuple1)

# 4. Slicing
sliced_tuple = example_tuple[1:4]
print("Sliced Tuple (index 1 to 3):", sliced_tuple)

# 5. Length of a tuple
print("Length of example_tuple:", len(example_tuple))

# 6. Iterating through a tuple
print("Iterating through example_tuple:")
for item in example_tuple:
    print(item)

# 7. Tuple unpacking
a, b, c, d, e = example_tuple
print("Unpacked values:", a, b, c, d, e)

# 8. Nested tuples
nested_tuple = (1, (2, 3), (4, 5, 6))
print("Nested Tuple:", nested_tuple)
print("Accessing nested element:", nested_tuple[1][1])

# 9. Immutable nature of tuples
try:
    example_tuple[0] = 10  # This will raise a TypeError
except TypeError as e:
    print("Error:", e)

# 10. Converting a list to a tuple
example_list = [1, 2, 3]
converted_tuple = tuple(example_list)
print("Converted Tuple:", converted_tuple)

# 11. Converting a tuple to a list
converted_list = list(example_tuple)
print("Converted List:", converted_list)

# Tuples are often used in scenarios where immutability is required, such as keys in dictionaries or fixed collections of items.