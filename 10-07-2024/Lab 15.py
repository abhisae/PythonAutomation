#Raw String or Provide specified path to the string

#If we want to display a path of particular file or destination then
# we put "r" infrontof specified path.


print(r"C:\Users\hp\Downloads")


# Mutable objects:

# Can be modified after creation.
# Operations on the object can change its state or content without creating a new object.
# Examples: lists, dictionaries, sets.

# Immutable objects:
# Cannot be modified after creation.
# Any operation that appears to modify the object actually creates a new object with the modified value.
# Examples: integers, floats, strings, tuples.


# Mutable object (list)
my_list = [1, 2, 3]
my_list[0] = 10
print(my_list)  # Output: [10, 2, 3]

# Immutable object (string)
my_string = "hello"
my_string[0] = "H"  # This will raise an error