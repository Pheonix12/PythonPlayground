# ============================================
# LISTS - Creating Lists
# ============================================

# Lists are ordered, mutable collections that can contain mixed types
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)  # Output: ['History', 'Math', 'Physics', 'CompSci']

# Lists can contain different data types
mixed = [1, 'Hello', 3.14, True]
print(mixed)  # Output: [1, 'Hello', 3.14, True]

# Creating an empty list
empty_list = []
print(empty_list)  # Output: []

# Creating an empty list with list() constructor
empty_list2 = list()
print(empty_list2)  # Output: []

# Creating a list from a string
chars = list('Hello')
print(chars)  # Output: ['H', 'e', 'l', 'l', 'o']

# Creating a list with range
numbers = list(range(5))
print(numbers)  # Output: [0, 1, 2, 3, 4]


# ============================================
# LIST INDEXING AND SLICING
# ============================================

courses = ['History', 'Math', 'Physics', 'CompSci']

# Accessing items by index (0-based)
print(courses[0])  # Output: History
print(courses[2])  # Output: Physics

# Negative indexing (from the end)
print(courses[-1])  # Output: CompSci (last item)
print(courses[-2])  # Output: Physics (second to last)

# Slicing lists [start:end] - start inclusive, end exclusive
print(courses[0:2])  # Output: ['History', 'Math']
print(courses[1:3])  # Output: ['Math', 'Physics']

# Omitting start or end
print(courses[:2])  # Output: ['History', 'Math'] (from beginning to index 2)
print(courses[2:])  # Output: ['Physics', 'CompSci'] (from index 2 to end)
print(courses[:])  # Output: ['History', 'Math', 'Physics', 'CompSci'] (entire list)

# Slicing with step
print(courses[::2])  # Output: ['History', 'Physics'] (every 2nd item)
print(courses[::-1])  # Output: ['CompSci', 'Physics', 'Math', 'History'] (reverse list)


# ============================================
# LIST LENGTH AND MEMBERSHIP
# ============================================

courses = ['History', 'Math', 'Physics', 'CompSci']

# Get the number of items in a list
print(len(courses))  # Output: 4

# Check if item exists in list
print('Math' in courses)  # Output: True
print('Art' in courses)  # Output: False
print('Art' not in courses)  # Output: True


# ============================================
# LIST METHODS - Adding Items
# ============================================

courses = ['History', 'Math', 'Physics', 'CompSci']

# append() - Adds an item to the end
courses.append('Art')  # No output - modifies list in place
print(courses)  # Output: ['History', 'Math', 'Physics', 'CompSci', 'Art']

# insert() - Adds an item at a specific position
courses.insert(0, 'Chemistry')  # Insert at index 0
print(courses)  # Output: ['Chemistry', 'History', 'Math', 'Physics', 'CompSci', 'Art']

courses.insert(2, 'Biology')  # Insert at index 2
print(courses)  # Output: ['Chemistry', 'History', 'Biology', 'Math', 'Physics', 'CompSci', 'Art']

# extend() - Adds multiple items from another list
courses_2 = ['English', 'Spanish']
courses.extend(courses_2)  # No output - modifies list in place
print(courses)  # Output: ['Chemistry', 'History', 'Biology', 'Math', 'Physics', 'CompSci', 'Art', 'English', 'Spanish']


# ============================================
# LIST METHODS - Removing Items
# ============================================

courses = ['History', 'Math', 'Physics', 'CompSci', 'Math']

# remove() - Removes the first occurrence of a value
courses.remove('Math')  # No output - modifies list in place
print(courses)  # Output: ['History', 'Physics', 'CompSci', 'Math'] (only first 'Math' removed)

# pop() - Removes and returns item at index (default: last item)
popped = courses.pop()  # Removes last item
print(popped)  # Output: Math
print(courses)  # Output: ['History', 'Physics', 'CompSci']

popped = courses.pop(0)  # Removes item at index 0
print(popped)  # Output: History
print(courses)  # Output: ['Physics', 'CompSci']

# clear() - Removes all items
courses_copy = ['A', 'B', 'C']
courses_copy.clear()  # No output - modifies list in place
print(courses_copy)  # Output: []

# del statement - Removes item at index or entire list
items = [1, 2, 3, 4, 5]
del items[0]  # No output - removes item at index 0
print(items)  # Output: [2, 3, 4, 5]

del items[1:3]  # Remove slice
print(items)  # Output: [2, 5]


# ============================================
# LIST METHODS - Sorting and Reversing
# ============================================

nums = [3, 1, 4, 1, 5, 9, 2]

# sort() - Sorts list in place (ascending by default)
nums.sort()  # No output - modifies list in place
print(nums)  # Output: [1, 1, 2, 3, 4, 5, 9]

# sort() with reverse=True for descending order
nums.sort(reverse=True)  # No output - modifies list in place
print(nums)  # Output: [9, 5, 4, 3, 2, 1, 1]

# sorted() - Returns a new sorted list (doesn't modify original)
nums = [3, 1, 4, 1, 5, 9, 2]
sorted_nums = sorted(nums)
print(sorted_nums)  # Output: [1, 1, 2, 3, 4, 5, 9]
print(nums)  # Output: [3, 1, 4, 1, 5, 9, 2] (original unchanged)

# reverse() - Reverses list in place
nums.reverse()  # No output - modifies list in place
print(nums)  # Output: [2, 9, 5, 1, 4, 1, 3]

# Sorting strings
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.sort()  # No output - sorts alphabetically
print(courses)  # Output: ['CompSci', 'History', 'Math', 'Physics']


# ============================================
# LIST METHODS - Other Useful Methods
# ============================================

nums = [1, 2, 3, 4, 5, 2, 2]

# count() - Returns number of occurrences
print(nums.count(2))  # Output: 3
print(nums.count(10))  # Output: 0 (not in list)

# index() - Returns index of first occurrence
print(nums.index(2))  # Output: 1 (first occurrence at index 1)
# print(nums.index(10))  # ValueError: 10 is not in list

# copy() - Creates a shallow copy of the list
nums_copy = nums.copy()
print(nums_copy)  # Output: [1, 2, 3, 4, 5, 2, 2]

# min() and max() - Find smallest and largest values
print(min(nums))  # Output: 1
print(max(nums))  # Output: 5

# sum() - Sum of all items
print(sum(nums))  # Output: 21


# ============================================
# LIST MUTABILITY - Important Concept
# ============================================

# Lists are mutable - changes affect all references
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1  # list_2 references the same list as list_1

print(list_1)  # Output: ['History', 'Math', 'Physics', 'CompSci']
print(list_2)  # Output: ['History', 'Math', 'Physics', 'CompSci']

list_1[0] = 'Art'  # Modify list_1

print(list_1)  # Output: ['Art', 'Math', 'Physics', 'CompSci']
print(list_2)  # Output: ['Art', 'Math', 'Physics', 'CompSci'] (also changed!)

# To avoid this, create a copy
list_3 = ['A', 'B', 'C']
list_4 = list_3.copy()  # or list_3[:]
list_3[0] = 'Z'

print(list_3)  # Output: ['Z', 'B', 'C']
print(list_4)  # Output: ['A', 'B', 'C'] (unchanged)


# ============================================
# LIST ITERATION
# ============================================

courses = ['History', 'Math', 'Physics', 'CompSci']

# Iterate over items
for course in courses:
    print(course)  # Output: History (then Math, then Physics, then CompSci on separate lines)

# Iterate with index using enumerate()
for index, course in enumerate(courses):
    print(index, course)  # Output: 0 History (then 1 Math, 2 Physics, 3 CompSci on separate lines)

# Start enumerate at different number
for index, course in enumerate(courses, start=1):
    print(index, course)  # Output: 1 History (then 2 Math, 3 Physics, 4 CompSci on separate lines)


# ============================================
# LIST COMPREHENSIONS
# ============================================

# Basic list comprehension - more concise than for loops
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

# With condition (filter)
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]

# Transform strings
courses = ['History', 'Math', 'Physics']
upper_courses = [course.upper() for course in courses]
print(upper_courses)  # Output: ['HISTORY', 'MATH', 'PHYSICS']

# With if-else
nums = [1, 2, 3, 4, 5]
labels = ['even' if x % 2 == 0 else 'odd' for x in nums]
print(labels)  # Output: ['odd', 'even', 'odd', 'even', 'odd']


# ============================================
# JOINING AND SPLITTING LISTS
# ============================================

# Convert list to string with join()
courses = ['History', 'Math', 'Physics']
course_str = ', '.join(courses)
print(course_str)  # Output: History, Math, Physics
print(type(course_str))  # Output: <class 'str'>

# Convert string to list with split()
course_str = 'History, Math, Physics'
course_list = course_str.split(', ')
print(course_list)  # Output: ['History', 'Math', 'Physics']


# ============================================
# NESTED LISTS (2D Lists / Matrices)
# ============================================

# Lists can contain other lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing nested list items
print(matrix[0])  # Output: [1, 2, 3] (first row)
print(matrix[1][2])  # Output: 6 (row 1, column 2)
print(matrix[2][0])  # Output: 7 (row 2, column 0)

# Iterating over 2D list
for row in matrix:
    print(row)  # Output: [1, 2, 3] (then [4, 5, 6], then [7, 8, 9] on separate lines)

# Iterating over all elements
for row in matrix:
    for item in row:
        print(item, end=' ')  # Output: 1 2 3 4 5 6 7 8 9 (on same line with spaces)
print()  # Output: (blank line)

# List comprehension for 2D lists
flattened = [item for row in matrix for item in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Creating a 2D list with list comprehension
zeros = [[0 for _ in range(3)] for _ in range(3)]
print(zeros)  # Output: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


# ============================================
# ZIP FUNCTION - Combining Lists
# ============================================

# zip() combines multiple lists element by element
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
cities = ['NYC', 'LA', 'Chicago']

# Combine into tuples
combined = zip(names, ages, cities)
print(list(combined))  # Output: [('Alice', 25, 'NYC'), ('Bob', 30, 'LA'), ('Charlie', 35, 'Chicago')]

# Using zip in a loop
for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")  # Output: Alice is 25 years old and lives in NYC (then Bob..., then Charlie... on separate lines)

# zip() stops at shortest list
list1 = [1, 2, 3, 4]
list2 = ['a', 'b']
print(list(zip(list1, list2)))  # Output: [(1, 'a'), (2, 'b')] (stops at shortest)

# Unzipping with zip(*list)
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
numbers, letters = zip(*pairs)
print(numbers)  # Output: (1, 2, 3)
print(letters)  # Output: ('a', 'b', 'c')


# ============================================
# SHALLOW COPY VS DEEP COPY
# ============================================

# Shallow copy - copies the list but not nested objects
import copy

# Shallow copy with simple list (works fine)
list1 = [1, 2, 3]
list2 = list1.copy()  # or list1[:] or copy.copy(list1)
list1[0] = 999
print(list1)  # Output: [999, 2, 3]
print(list2)  # Output: [1, 2, 3] (unchanged)

# Shallow copy with nested list (problem!)
list1 = [[1, 2], [3, 4]]
list2 = list1.copy()  # Shallow copy
list1[0][0] = 999  # Modify nested list
print(list1)  # Output: [[999, 2], [3, 4]]
print(list2)  # Output: [[999, 2], [3, 4]] (also changed! - nested list is shared)

# Deep copy - copies everything including nested objects
list1 = [[1, 2], [3, 4]]
list2 = copy.deepcopy(list1)  # Deep copy
list1[0][0] = 999
print(list1)  # Output: [[999, 2], [3, 4]]
print(list2)  # Output: [[1, 2], [3, 4]] (unchanged - completely independent)


# ============================================
# TUPLES - Creating Tuples
# ============================================

# Tuples are ordered, immutable collections
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
print(tuple_1)  # Output: ('History', 'Math', 'Physics', 'CompSci')
print(type(tuple_1))  # Output: <class 'tuple'>

# Tuples can be created without parentheses
tuple_2 = 'History', 'Math', 'Physics'
print(tuple_2)  # Output: ('History', 'Math', 'Physics')

# Single item tuple (comma is required!)
single = (1,)  # Note the comma
print(single)  # Output: (1,)
print(type(single))  # Output: <class 'tuple'>

not_tuple = (1)  # This is just an integer in parentheses
print(type(not_tuple))  # Output: <class 'int'>

# Empty tuple
empty_tuple = ()
print(empty_tuple)  # Output: ()

# Empty tuple with tuple() constructor
empty_tuple2 = tuple()
print(empty_tuple2)  # Output: ()

# Creating tuple from list
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3)


# ============================================
# TUPLE INDEXING AND SLICING
# ============================================

tuple_1 = ('History', 'Math', 'Physics', 'CompSci')

# Indexing works the same as lists
print(tuple_1[0])  # Output: History
print(tuple_1[-1])  # Output: CompSci

# Slicing works the same as lists
print(tuple_1[1:3])  # Output: ('Math', 'Physics')
print(tuple_1[:2])  # Output: ('History', 'Math')
print(tuple_1[::-1])  # Output: ('CompSci', 'Physics', 'Math', 'History')


# ============================================
# TUPLE IMMUTABILITY
# ============================================

# Tuples cannot be modified after creation
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
# tuple_1[0] = 'Art'  # TypeError: 'tuple' object does not support item assignment

# Multiple variables can reference the same tuple without issues
tuple_2 = tuple_1
print(tuple_1)  # Output: ('History', 'Math', 'Physics', 'CompSci')
print(tuple_2)  # Output: ('History', 'Math', 'Physics', 'CompSci')

# Since tuples are immutable, both will always be the same
# This is different from lists where modifications affect all references


# ============================================
# TUPLE METHODS (Only 2!)
# ============================================

tuple_1 = (1, 2, 3, 2, 4, 2, 5)

# count() - Returns number of occurrences
print(tuple_1.count(2))  # Output: 3
print(tuple_1.count(10))  # Output: 0

# index() - Returns index of first occurrence
print(tuple_1.index(2))  # Output: 1
# print(tuple_1.index(10))  # ValueError: tuple.index(x): x not in tuple


# ============================================
# TUPLE UNPACKING
# ============================================

# Assign tuple values to multiple variables
person = ('John', 25, 'Developer')
name, age, job = person
print(name)  # Output: John
print(age)  # Output: 25
print(job)  # Output: Developer

# Unpacking with * (collects remaining items)
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(first)  # Output: 1
print(middle)  # Output: [2, 3, 4] (note: becomes a list)
print(last)  # Output: 5

# Swapping values using tuple unpacking
a = 10
b = 20
a, b = b, a  # Swap without temporary variable
print(a)  # Output: 20
print(b)  # Output: 10


# ============================================
# WHEN TO USE TUPLES VS LISTS
# ============================================

# Use tuples when:
# 1. Data shouldn't change (immutable)
# 2. Returning multiple values from a function
# 3. Dictionary keys (lists can't be keys)
# 4. Slightly faster and use less memory than lists

coordinates = (40.7128, 74.0060)  # Latitude, longitude shouldn't change
print(coordinates)  # Output: (40.7128, 74.006)


# ============================================
# DICTIONARIES - Creating Dictionaries
# ============================================

# Dictionaries store key-value pairs (unordered in Python < 3.7, ordered in 3.7+)
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)  # Output: {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(type(student))  # Output: <class 'dict'>

# Empty dictionary
empty_dict = {}
print(empty_dict)  # Output: {}

# Empty dictionary with dict() constructor
empty_dict2 = dict()
print(empty_dict2)  # Output: {}

# Creating dictionary with dict() constructor
student2 = dict(name='Alice', age=22, grade='A')
print(student2)  # Output: {'name': 'Alice', 'age': 22, 'grade': 'A'}


# ============================================
# ACCESSING DICTIONARY VALUES
# ============================================

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

# Access value by key using square brackets
print(student['name'])  # Output: John
print(student['courses'])  # Output: ['Math', 'CompSci']
# print(student['phone'])  # KeyError: 'phone' (key doesn't exist)

# Access value using get() method (safer - returns None if key doesn't exist)
print(student.get('name'))  # Output: John
print(student.get('phone'))  # Output: None (no error)
print(student.get('phone', 'Not Found'))  # Output: Not Found (custom default)


# ============================================
# ADDING AND MODIFYING DICTIONARY ITEMS
# ============================================

student = {'name': 'John', 'age': 25}

# Add new key-value pair
student['phone'] = '555-5555'  # No output - modifies dict in place
print(student)  # Output: {'name': 'John', 'age': 25, 'phone': '555-5555'}

# Modify existing value
student['age'] = 26  # No output - modifies dict in place
print(student)  # Output: {'name': 'John', 'age': 26, 'phone': '555-5555'}

# update() - Add multiple key-value pairs
student.update({'name': 'Jane', 'city': 'NYC', 'age': 27})  # No output
print(student)  # Output: {'name': 'Jane', 'age': 27, 'phone': '555-5555', 'city': 'NYC'}


# ============================================
# REMOVING DICTIONARY ITEMS
# ============================================

student = {'name': 'John', 'age': 25, 'courses': ['Math'], 'phone': '555-5555'}

# pop() - Removes key and returns its value
age = student.pop('age')
print(age)  # Output: 25
print(student)  # Output: {'name': 'John', 'courses': ['Math'], 'phone': '555-5555'}

# popitem() - Removes and returns last inserted key-value pair (as tuple)
item = student.popitem()
print(item)  # Output: ('phone', '555-5555')
print(student)  # Output: {'name': 'John', 'courses': ['Math']}

# del - Removes key
del student['courses']  # No output
print(student)  # Output: {'name': 'John'}

# clear() - Removes all items
student.clear()  # No output
print(student)  # Output: {}


# ============================================
# DICTIONARY METHODS - Keys, Values, Items
# ============================================

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

# keys() - Returns all keys
print(student.keys())  # Output: dict_keys(['name', 'age', 'courses'])

# values() - Returns all values
print(student.values())  # Output: dict_values(['John', 25, ['Math', 'CompSci']])

# items() - Returns key-value pairs as tuples
print(student.items())  # Output: dict_items([('name', 'John'), ('age', 25), ('courses', ['Math', 'CompSci'])])

# Check if key exists
print('name' in student)  # Output: True
print('phone' in student)  # Output: False

# Check if value exists (in values)
print('John' in student.values())  # Output: True


# ============================================
# DICTIONARY METHODS - Additional Methods
# ============================================

# copy() - Creates a shallow copy of the dictionary
student = {'name': 'John', 'age': 25}
student_copy = student.copy()
student['name'] = 'Jane'
print(student)  # Output: {'name': 'Jane', 'age': 25}
print(student_copy)  # Output: {'name': 'John', 'age': 25} (unchanged)

# setdefault() - Get value or set default if key doesn't exist
student = {'name': 'John', 'age': 25}
age = student.setdefault('age', 30)  # Key exists, returns existing value
print(age)  # Output: 25
print(student)  # Output: {'name': 'John', 'age': 25} (unchanged)

phone = student.setdefault('phone', '555-0000')  # Key doesn't exist, sets and returns default
print(phone)  # Output: 555-0000
print(student)  # Output: {'name': 'John', 'age': 25, 'phone': '555-0000'}

# fromkeys() - Create dictionary from sequence of keys with optional default value
keys = ['name', 'age', 'city']
new_dict = dict.fromkeys(keys)  # Default value is None
print(new_dict)  # Output: {'name': None, 'age': None, 'city': None}

new_dict2 = dict.fromkeys(keys, 'Unknown')  # Custom default value
print(new_dict2)  # Output: {'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}

# Create dict from list with default value
numbers = [1, 2, 3]
num_dict = dict.fromkeys(numbers, 0)
print(num_dict)  # Output: {1: 0, 2: 0, 3: 0}


# ============================================
# ITERATING OVER DICTIONARIES
# ============================================

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

# Iterate over keys (default)
for key in student:
    print(key)  # Output: name (then age, then courses on separate lines)

# Iterate over keys explicitly
for key in student.keys():
    print(key)  # Output: name (then age, then courses on separate lines)

# Iterate over values
for value in student.values():
    print(value)  # Output: John (then 25, then ['Math', 'CompSci'] on separate lines)

# Iterate over key-value pairs
for key, value in student.items():
    print(key, value)  # Output: name John (then age 25, then courses ['Math', 'CompSci'] on separate lines)


# ============================================
# DICTIONARY COMPREHENSIONS
# ============================================

# Create dictionary from lists
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
people = {name: age for name, age in zip(names, ages)}
print(people)  # Output: {'Alice': 25, 'Bob': 30, 'Charlie': 35}

# Dictionary comprehension with condition
squares = {x: x**2 for x in range(5) if x % 2 == 0}
print(squares)  # Output: {0: 0, 2: 4, 4: 16}

# Transform existing dictionary
original = {'a': 1, 'b': 2, 'c': 3}
doubled = {k: v*2 for k, v in original.items()}
print(doubled)  # Output: {'a': 2, 'b': 4, 'c': 6}


# ============================================
# NESTED DICTIONARIES
# ============================================

# Dictionary containing other dictionaries
students = {
    'student1': {'name': 'John', 'age': 25},
    'student2': {'name': 'Jane', 'age': 22},
    'student3': {'name': 'Bob', 'age': 27}
}

print(students)  # Output: {'student1': {'name': 'John', 'age': 25}, 'student2': {'name': 'Jane', 'age': 22}, 'student3': {'name': 'Bob', 'age': 27}}

# Access nested values
print(students['student1'])  # Output: {'name': 'John', 'age': 25}
print(students['student1']['name'])  # Output: John
print(students['student2']['age'])  # Output: 22


# ============================================
# SETS - Creating Sets
# ============================================

# Sets are unordered collections of unique items
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
print(cs_courses)  # Output: {'CompSci', 'History', 'Math', 'Physics'} (order may vary)
print(type(cs_courses))  # Output: <class 'set'>

# Sets automatically remove duplicates
numbers = {1, 2, 3, 2, 4, 1, 5}
print(numbers)  # Output: {1, 2, 3, 4, 5}

# Empty set (must use set(), not {})
empty_set = set()
print(empty_set)  # Output: set()
print(type(empty_set))  # Output: <class 'set'>

# {} creates an empty dictionary, not a set!
empty_dict = {}
print(type(empty_dict))  # Output: <class 'dict'>

# Creating set from list
my_list = [1, 2, 3, 2, 1]
my_set = set(my_list)
print(my_set)  # Output: {1, 2, 3}


# ============================================
# SET MEMBERSHIP AND LENGTH
# ============================================

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}

# Check membership
print('Math' in cs_courses)  # Output: True
print('Art' in cs_courses)  # Output: False

# Get number of items
print(len(cs_courses))  # Output: 4


# ============================================
# SET METHODS - Adding and Removing
# ============================================

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}

# add() - Add single item
cs_courses.add('Art')  # No output - modifies set in place
print(cs_courses)  # Output: {'CompSci', 'History', 'Art', 'Math', 'Physics'} (order may vary)

# Adding duplicate has no effect
cs_courses.add('Math')  # No output - 'Math' already exists
print(cs_courses)  # Output: {'CompSci', 'History', 'Art', 'Math', 'Physics'} (unchanged)

# update() - Add multiple items from another set/list
cs_courses.update(['Chemistry', 'Biology'])  # No output
print(cs_courses)  # Output: {'CompSci', 'History', 'Art', 'Math', 'Physics', 'Chemistry', 'Biology'} (order may vary)

# remove() - Remove item (raises error if not found)
cs_courses.remove('Art')  # No output
print(cs_courses)  # Output: {'CompSci', 'History', 'Math', 'Physics', 'Chemistry', 'Biology'} (order may vary)
# cs_courses.remove('Drama')  # KeyError: 'Drama'

# discard() - Remove item (no error if not found)
cs_courses.discard('Math')  # No output
print(cs_courses)  # Output: {'CompSci', 'History', 'Physics', 'Chemistry', 'Biology'} (order may vary)
cs_courses.discard('Drama')  # No error, no output
print(cs_courses)  # Output: {'CompSci', 'History', 'Physics', 'Chemistry', 'Biology'} (unchanged)

# pop() - Remove and return random item
item = cs_courses.pop()
print(item)  # Output: (some course name - varies)
print(cs_courses)  # Output: (set without the popped item)

# clear() - Remove all items
cs_courses.clear()  # No output
print(cs_courses)  # Output: set()


# ============================================
# SET OPERATIONS - Mathematical Set Theory
# ============================================

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

# intersection() - Items in both sets
print(cs_courses.intersection(art_courses))  # Output: {'History', 'Math'}
# OR using & operator
print(cs_courses & art_courses)  # Output: {'History', 'Math'}

# difference() - Items in first set but not in second
print(cs_courses.difference(art_courses))  # Output: {'CompSci', 'Physics'}
# OR using - operator
print(cs_courses - art_courses)  # Output: {'CompSci', 'Physics'}

# symmetric_difference() - Items in either set but not both
print(cs_courses.symmetric_difference(art_courses))  # Output: {'CompSci', 'Physics', 'Art', 'Design'}
# OR using ^ operator
print(cs_courses ^ art_courses)  # Output: {'CompSci', 'Physics', 'Art', 'Design'}

# union() - All items from both sets
print(cs_courses.union(art_courses))  # Output: {'History', 'Math', 'Physics', 'CompSci', 'Art', 'Design'}
# OR using | operator
print(cs_courses | art_courses)  # Output: {'History', 'Math', 'Physics', 'CompSci', 'Art', 'Design'}


# ============================================
# SET OPERATIONS - Subset and Superset
# ============================================

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
set3 = {1, 2, 3}

# issubset() - Check if all items in set1 are in set2
print(set1.issubset(set2))  # Output: True (set1 is subset of set2)
# OR using <= operator
print(set1 <= set2)  # Output: True

# issuperset() - Check if set2 contains all items from set1
print(set2.issuperset(set1))  # Output: True (set2 is superset of set1)
# OR using >= operator
print(set2 >= set1)  # Output: True

# isdisjoint() - Check if sets have no common items
print(set1.isdisjoint(set2))  # Output: False (they share 1, 2, 3)
print({1, 2}.isdisjoint({3, 4}))  # Output: True (no common items)


# ============================================
# SET METHODS - Update Operations (Modify in Place)
# ============================================

# These methods modify the set in place instead of returning a new set

# difference_update() - Remove items found in other sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}
set1.difference_update(set2)  # No output - modifies set1 in place
print(set1)  # Output: {1, 2, 3} (removed 4, 5 which were in set2)
# OR using -= operator
set1 = {1, 2, 3, 4, 5}
set1 -= set2  # Same as difference_update
print(set1)  # Output: {1, 2, 3}

# intersection_update() - Keep only items found in all sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
set1.intersection_update(set2)  # No output - modifies set1 in place
print(set1)  # Output: {3, 4, 5} (only items in both sets)
# OR using &= operator
set1 = {1, 2, 3, 4, 5}
set1 &= set2  # Same as intersection_update
print(set1)  # Output: {3, 4, 5}

# symmetric_difference_update() - Keep items in either set but not both
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.symmetric_difference_update(set2)  # No output - modifies set1 in place
print(set1)  # Output: {1, 2, 5, 6} (items in either but not both)
# OR using ^= operator
set1 = {1, 2, 3, 4}
set1 ^= set2  # Same as symmetric_difference_update
print(set1)  # Output: {1, 2, 5, 6}

# update() with multiple sets - Add items from multiple sets
set1 = {1, 2, 3}
set1.update({4, 5}, {6, 7}, [8, 9])  # Can accept multiple iterables
print(set1)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

# copy() - Creates a shallow copy of the set
set1 = {1, 2, 3}
set2 = set1.copy()
set1.add(4)
print(set1)  # Output: {1, 2, 3, 4}
print(set2)  # Output: {1, 2, 3} (unchanged)


# ============================================
# SETS - Removing Duplicates
# ============================================

# Common use case: remove duplicates from a list
numbers = [1, 2, 3, 2, 4, 1, 5, 3]
print(numbers)  # Output: [1, 2, 3, 2, 4, 1, 5, 3]

unique_numbers = list(set(numbers))  # Convert to set then back to list
print(unique_numbers)  # Output: [1, 2, 3, 4, 5] (order may vary)

# To preserve order, use dict.fromkeys() or set with sorted()
unique_ordered = list(dict.fromkeys(numbers))
print(unique_ordered)  # Output: [1, 2, 3, 4, 5] (preserves original order)


# ============================================
# FROZENSETS - Immutable Sets
# ============================================

# Frozensets are immutable versions of sets (like tuples are to lists)
frozen = frozenset([1, 2, 3, 4])
print(frozen)  # Output: frozenset({1, 2, 3, 4})
print(type(frozen))  # Output: <class 'frozenset'>

# Frozensets support all set operations that don't modify the set
set1 = frozenset([1, 2, 3])
set2 = frozenset([2, 3, 4])

print(set1 & set2)  # Output: frozenset({2, 3}) (intersection)
print(set1 | set2)  # Output: frozenset({1, 2, 3, 4}) (union)
print(set1 - set2)  # Output: frozenset({1}) (difference)

# Cannot modify frozensets
# frozen.add(5)  # AttributeError: 'frozenset' object has no attribute 'add'
# frozen.remove(1)  # AttributeError: 'frozenset' object has no attribute 'remove'

# Main use case: Frozensets can be used as dictionary keys or set elements
# (regular sets cannot because they're mutable)
my_dict = {frozenset([1, 2]): 'value1', frozenset([3, 4]): 'value2'}
print(my_dict)  # Output: {frozenset({1, 2}): 'value1', frozenset({3, 4}): 'value2'}
print(my_dict[frozenset([1, 2])])  # Output: value1

# Set of frozensets (nested sets)
set_of_sets = {frozenset([1, 2]), frozenset([3, 4]), frozenset([1, 2])}
print(set_of_sets)  # Output: {frozenset({1, 2}), frozenset({3, 4})} (duplicate removed)

# Membership testing
print(1 in frozen)  # Output: False (from earlier definition)
print(2 in set1)  # Output: True


# ============================================
# COMPARING DATA STRUCTURES
# ============================================

# Lists: Ordered, mutable, allows duplicates, []
# Tuples: Ordered, immutable, allows duplicates, ()
# Dictionaries: Unordered (ordered in 3.7+), mutable, no duplicate keys, {}
# Sets: Unordered, mutable, no duplicates, set()
# Frozensets: Unordered, immutable, no duplicates, frozenset()

print("List:", [1, 2, 2, 3])  # Output: List: [1, 2, 2, 3]
print("Tuple:", (1, 2, 2, 3))  # Output: Tuple: (1, 2, 2, 3)
print("Dictionary:", {'a': 1, 'b': 2})  # Output: Dictionary: {'a': 1, 'b': 2}
print("Set:", {1, 2, 2, 3})  # Output: Set: {1, 2, 3}
print("Frozenset:", frozenset([1, 2, 2, 3]))  # Output: Frozenset: frozenset({1, 2, 3})


# ============================================
# PERFORMANCE CHARACTERISTICS
# ============================================

# Time complexity for common operations (Big O notation)

# LISTS:
# - Accessing by index: O(1) - Very fast
# - Appending to end: O(1) - Very fast
# - Inserting at beginning: O(n) - Slow (has to shift all elements)
# - Removing from end: O(1) - Very fast
# - Removing from beginning: O(n) - Slow
# - Searching for value: O(n) - Slow (has to check each element)
# - Checking if item exists (in): O(n) - Slow

# TUPLES:
# - Same as lists for access and search
# - Generally faster than lists for iteration
# - Use less memory than lists
# - Good for fixed collections

# DICTIONARIES:
# - Accessing by key: O(1) - Very fast
# - Adding/removing key-value: O(1) - Very fast
# - Checking if key exists: O(1) - Very fast
# - Very memory efficient for lookups
# - Use more memory than lists for storage

# SETS:
# - Adding element: O(1) - Very fast
# - Removing element: O(1) - Very fast
# - Checking membership: O(1) - Very fast (fastest way to check if item exists!)
# - Set operations (union, intersection): O(len(set))
# - Use more memory than lists

# Example: Checking membership performance
import time

# List membership check (slow for large lists)
large_list = list(range(10000))
start = time.time()
9999 in large_list  # Has to check each element
end = time.time()
print(f"List membership check: {end - start:.6f} seconds")  # Output: List membership check: 0.000XXX seconds (varies)

# Set membership check (fast!)
large_set = set(range(10000))
start = time.time()
9999 in large_set  # Direct hash lookup
end = time.time()
print(f"Set membership check: {end - start:.6f} seconds")  # Output: Set membership check: 0.000XXX seconds (much faster!)

# When to use each:
# - Use LISTS when: order matters, duplicates needed, frequent indexing
# - Use TUPLES when: data shouldn't change, dictionary keys, return multiple values
# - Use DICTIONARIES when: fast lookups by key, key-value associations
# - Use SETS when: testing membership, removing duplicates, mathematical set operations


# ============================================
# ADVANCED LIST SLICING TECHNIQUES
# ============================================

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Negative step (reverse with slice)
print(numbers[::-1])  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(numbers[::-2])  # Output: [9, 7, 5, 3, 1, 0] (every 2nd element reversed)

# Reverse a portion
print(numbers[2:7][::-1])  # Output: [6, 5, 4, 3, 2] (reverse slice from index 2 to 7)

# Replace slice with assignment
numbers[2:5] = [99, 88, 77]  # No output - modifies list in place
print(numbers)  # Output: [0, 1, 99, 88, 77, 5, 6, 7, 8, 9]

# Insert multiple items with empty slice
numbers = [1, 2, 5, 6]
numbers[2:2] = [3, 4]  # Insert at index 2
print(numbers)  # Output: [1, 2, 3, 4, 5, 6]

# Delete slice
numbers = [0, 1, 2, 3, 4, 5]
numbers[2:4] = []  # Delete elements at index 2 and 3
print(numbers)  # Output: [0, 1, 4, 5]

# Replace with different length
numbers = [1, 2, 3, 4, 5]
numbers[1:4] = [99]  # Replace 3 elements with 1 element
print(numbers)  # Output: [1, 99, 5]

# Step slice assignment
numbers = [0, 1, 2, 3, 4, 5]
numbers[::2] = [10, 20, 30]  # Replace every 2nd element
print(numbers)  # Output: [10, 1, 20, 3, 30, 5]


# ============================================
# ALL() AND ANY() FUNCTIONS
# ============================================

# all() - Returns True if all elements are True (or list is empty)
print(all([True, True, True]))  # Output: True
print(all([True, False, True]))  # Output: False
print(all([1, 2, 3]))  # Output: True (all non-zero numbers are truthy)
print(all([1, 0, 3]))  # Output: False (0 is falsy)
print(all([]))  # Output: True (empty list)

# any() - Returns True if any element is True
print(any([False, False, True]))  # Output: True
print(any([False, False, False]))  # Output: False
print(any([0, 0, 1]))  # Output: True
print(any([]))  # Output: False (empty list)

# Practical examples
numbers = [2, 4, 6, 8]
print(all(n % 2 == 0 for n in numbers))  # Output: True (all are even)

grades = [85, 90, 72, 88]
print(any(grade < 75 for grade in grades))  # Output: True (at least one grade below 75)


# ============================================
# FILTER, MAP, REDUCE FUNCTIONS
# ============================================

# filter() - Filter items based on a condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # Output: [2, 4, 6, 8, 10]

# map() - Transform each item
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16, 25]

# Multiple lists with map
list1 = [1, 2, 3]
list2 = [10, 20, 30]
sums = map(lambda x, y: x + y, list1, list2)
print(list(sums))  # Output: [11, 22, 33]

# reduce() - Reduce list to single value (need to import)
from functools import reduce
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)  # Output: 15 (1+2+3+4+5)

product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120 (1*2*3*4*5)

# Note: List comprehensions are often more readable than filter/map
evens = [x for x in numbers if x % 2 == 0]  # More Pythonic
squared = [x**2 for x in numbers]  # More Pythonic


# ============================================
# COLLECTIONS MODULE - Specialized Data Structures
# ============================================

from collections import defaultdict, Counter, deque, namedtuple

# defaultdict - Dictionary with default values for missing keys
dd = defaultdict(int)  # Default value is 0 for int
dd['a'] += 1  # No error even though 'a' doesn't exist yet
dd['b'] += 5
print(dd)  # Output: defaultdict(<class 'int'>, {'a': 1, 'b': 5})
print(dd['c'])  # Output: 0 (returns default value instead of error)

# defaultdict with list
dd_list = defaultdict(list)
dd_list['fruits'].append('apple')
dd_list['fruits'].append('banana')
dd_list['veggies'].append('carrot')
print(dd_list)  # Output: defaultdict(<class 'list'>, {'fruits': ['apple', 'banana'], 'veggies': ['carrot']})

# Counter - Count occurrences of items
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
counter = Counter(words)
print(counter)  # Output: Counter({'apple': 3, 'banana': 2, 'cherry': 1})
print(counter['apple'])  # Output: 3
print(counter['orange'])  # Output: 0 (no error for missing items)

# most_common() - Get most frequent items
print(counter.most_common(2))  # Output: [('apple', 3), ('banana', 2)] (top 2)

# Counter from string
letter_count = Counter('hello world')
print(letter_count)  # Output: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# Counter arithmetic
c1 = Counter(['a', 'b', 'c', 'a'])
c2 = Counter(['a', 'b', 'd'])
print(c1 + c2)  # Output: Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1}) (add counts)
print(c1 - c2)  # Output: Counter({'a': 1, 'c': 1}) (subtract counts, keep positive only)

# deque - Double-ended queue (efficient for adding/removing from both ends)
dq = deque([1, 2, 3])
dq.append(4)  # Add to right
dq.appendleft(0)  # Add to left
print(dq)  # Output: deque([0, 1, 2, 3, 4])
dq.pop()  # Remove from right
dq.popleft()  # Remove from left
print(dq)  # Output: deque([1, 2, 3])

# namedtuple - Tuple with named fields (like a lightweight class)
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p)  # Output: Point(x=10, y=20)
print(p.x)  # Output: 10 (access by name)
print(p[0])  # Output: 10 (can still access by index)


# ============================================
# ENUMERATE AND RANGE IN DETAIL
# ============================================

# enumerate() - Get index and value while looping
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)  # Output: 0 apple (then 1 banana, 2 cherry on separate lines)

# enumerate with custom start index
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)  # Output: 1 apple (then 2 banana, 3 cherry on separate lines)

# enumerate returns tuples
enum_obj = enumerate(fruits)
print(list(enum_obj))  # Output: [(0, 'apple'), (1, 'banana'), (2, 'cherry')]

# range() - Generate sequence of numbers
print(list(range(5)))  # Output: [0, 1, 2, 3, 4] (0 to 4)
print(list(range(2, 8)))  # Output: [2, 3, 4, 5, 6, 7] (2 to 7)
print(list(range(0, 10, 2)))  # Output: [0, 2, 4, 6, 8] (0 to 9, step 2)
print(list(range(10, 0, -1)))  # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] (10 to 1, counting down)

# range is memory efficient (doesn't create list in memory)
big_range = range(1000000)  # Doesn't actually create 1 million numbers
print(type(big_range))  # Output: <class 'range'>

# Check membership in range (very fast)
print(500 in range(1000))  # Output: True (O(1) operation)


# ============================================
# SORTING WITH KEY FUNCTIONS
# ============================================

# Sort by custom criteria using key parameter
words = ['banana', 'pie', 'Washington', 'book']

# Sort by length
sorted_by_length = sorted(words, key=len)
print(sorted_by_length)  # Output: ['pie', 'book', 'banana', 'Washington']

# Sort case-insensitive
sorted_case_insensitive = sorted(words, key=str.lower)
print(sorted_case_insensitive)  # Output: ['banana', 'book', 'pie', 'Washington']

# Sort list of tuples by second element
students = [('John', 25), ('Jane', 22), ('Bob', 27)]
sorted_by_age = sorted(students, key=lambda x: x[1])
print(sorted_by_age)  # Output: [('Jane', 22), ('John', 25), ('Bob', 27)]

# Sort dictionary by values
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
sorted_items = sorted(scores.items(), key=lambda x: x[1], reverse=True)
print(sorted_items)  # Output: [('Bob', 92), ('Alice', 85), ('Charlie', 78)]

# Using operator module for cleaner code
from operator import itemgetter
sorted_students = sorted(students, key=itemgetter(1))
print(sorted_students)  # Output: [('Jane', 22), ('John', 25), ('Bob', 27)]


# ============================================
# REVERSING SEQUENCES
# ============================================

numbers = [1, 2, 3, 4, 5]

# reversed() - Returns reverse iterator (doesn't modify original)
rev = reversed(numbers)
print(list(rev))  # Output: [5, 4, 3, 2, 1]
print(numbers)  # Output: [1, 2, 3, 4, 5] (original unchanged)

# Reverse a string
text = "Hello"
print(''.join(reversed(text)))  # Output: olleH

# Reverse dictionary items
d = {'a': 1, 'b': 2, 'c': 3}
print(dict(reversed(d.items())))  # Output: {'c': 3, 'b': 2, 'a': 1} (Python 3.8+)


# ============================================
# DISCOVERING METHODS WITH dir()
# ============================================

# Using dir() to see available methods
sample_list = [1, 2, 3]
sample_tuple = (1, 2, 3)
sample_dict = {'a': 1}
sample_set = {1, 2, 3}

print("List methods:")  # Output: List methods:
list_methods = [method for method in dir(sample_list) if not method.startswith('_')]
print(list_methods)  # Output: ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

print("\nTuple methods:")  # Output: (blank line) Tuple methods:
tuple_methods = [method for method in dir(sample_tuple) if not method.startswith('_')]
print(tuple_methods)  # Output: ['count', 'index']

print("\nDictionary methods:")  # Output: (blank line) Dictionary methods:
dict_methods = [method for method in dir(sample_dict) if not method.startswith('_')]
print(dict_methods)  # Output: ['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

print("\nSet methods:")  # Output: (blank line) Set methods:
set_methods = [method for method in dir(sample_set) if not method.startswith('_')]
print(set_methods)  # Output: ['add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']


# ============================================
# SUMMARY - QUICK REFERENCE
# ============================================

# CREATE
my_list = [1, 2, 3]  # Or list()
my_tuple = (1, 2, 3)  # Or tuple()
my_dict = {'a': 1, 'b': 2}  # Or dict()
my_set = {1, 2, 3}  # Or set()

# ACCESS
print(my_list[0])  # Output: 1 (indexing)
print(my_dict['a'])  # Output: 1 (by key)

# MODIFY (only mutable types)
my_list.append(4)  # Add to list
my_dict['c'] = 3  # Add to dict
my_set.add(4)  # Add to set

# ITERATE
for item in my_list:
    print(item)  # Output: 1 (then 2, 3, 4 on separate lines)

for key, value in my_dict.items():
    print(key, value)  # Output: a 1 (then b 2, c 3 on separate lines)

# CHECK MEMBERSHIP
print(2 in my_list)  # Output: True
print('a' in my_dict)  # Output: True (checks keys)
print(2 in my_set)  # Output: True (fastest!)

# LENGTH
print(len(my_list))  # Output: 4
print(len(my_dict))  # Output: 3
print(len(my_set))  # Output: 4
