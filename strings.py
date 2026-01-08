# ============================================
# STRING BASICS - Creating and Printing Strings
# ============================================

# Strings can be created with double quotes
message = "Hello World"
print(message)  # Output: Hello World

# Strings can also be created with single quotes (both work the same)
message = 'Hello World'
print(message)  # Output: Hello World

# Multi-line strings use triple quotes (""" or ''')
message = """Hello
World"""
print(message)  # Output: Hello (newline) World

# Using escape character (\) to include quotes inside strings
message = 'Phoenix\'s World'  # Backslash escapes the single quote
print(message)  # Output: Phoenix's World

# Alternative: Use double quotes to avoid escaping single quotes
message = "Phoenix's World"
print(message)  # Output: Phoenix's World


# ============================================
# STRING LENGTH AND INDEXING
# ============================================

m = 'Hello World'

# len() returns the number of characters in the string
print(len(m))  # Output: 11

# Accessing individual characters by index (0-based indexing)
print(m[0])  # Output: H (first character)
print(m[6])  # Output: W

# Negative indexing starts from the end (-1 is the last character)
print(m[-1])  # Output: d (last character)
print(m[-5])  # Output: W (5th character from the end)

# print(m[11])  # IndexError: string index out of range (index 11 doesn't exist)


# ============================================
# STRING SLICING
# ============================================

# Slicing syntax: string[start:end] - start is inclusive, end is exclusive
print(m[0:5])  # Output: Hello (characters at index 0,1,2,3,4)
print(m[6:11])  # Output: World

# Omitting start defaults to 0, omitting end goes to the end
print(m[:5])  # Output: Hello (same as [0:5])
print(m[6:])  # Output: World (from index 6 to end)
print(m[:])  # Output: Hello World (entire string)

# Slicing with step: string[start:end:step]
print(m[0:11:2])  # Output: HloWrd (every 2nd character)
print(m[::2])  # Output: HloWrd (same as above)

# Reverse a string using negative step
print(m[::-1])  # Output: dlroW olleH


# ============================================
# STRING METHODS - Case Conversion
# ============================================

# Convert to lowercase
print(m.lower())  # Output: hello world

# Convert to uppercase
print(m.upper())  # Output: HELLO WORLD

# Capitalize first letter, rest lowercase
print(m.capitalize())  # Output: Hello world

# Title case (capitalize first letter of each word)
print(m.title())  # Output: Hello World

# Swap case (upper becomes lower, lower becomes upper)
print(m.swapcase())  # Output: hELLO wORLD


# ============================================
# STRING METHODS - Searching
# ============================================

# count() returns the number of occurrences of a substring
print(m.count("l"))  # Output: 3 (three 'l's in "Hello World")
print(m.count("o"))  # Output: 2

# find() returns the index of the first occurrence (returns -1 if not found)
print(m.find("World"))  # Output: 6 (starts at index 6)
print(m.find("o"))  # Output: 4 (first 'o' is at index 4)
print(m.find("xyz"))  # Output: -1 (not found)

# index() is similar to find() but raises an error if not found
print(m.index("World"))  # Output: 6
# print(m.index("xyz"))  # ValueError: substring not found


# ============================================
# STRING METHODS - Modification (returns new string)
# ============================================

# Note: Strings are immutable in Python, so these methods return NEW strings

# replace() replaces all occurrences of a substring
print(m.replace("World", "Python"))  # Output: Hello Python
print(m.replace("l", "L"))  # Output: HeLLo WorLd
print(m)  # Output: Hello World (original string unchanged)

# strip() removes whitespace from both ends
text = "   Hello World   "
print(text.strip())  # Output: Hello World
print(text.lstrip())  # Output: Hello World    (left strip)
print(text.rstrip())  # Output:    Hello World (right strip)

# You can also strip specific characters
text2 = "***Hello***"
print(text2.strip("*"))  # Output: Hello


# ============================================
# STRING METHODS - Splitting and Joining
# ============================================

# split() splits a string into a list of substrings
sentence = "Python is awesome"
words = sentence.split()  # Splits by whitespace by default
print(words)  # Output: ['Python', 'is', 'awesome']

csv = "apple,banana,cherry"
fruits = csv.split(",")  # Split by comma
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# join() joins a list of strings into one string
print(" ".join(words))  # Output: Python is awesome
print("-".join(fruits))  # Output: apple-banana-cherry


# ============================================
# STRING METHODS - Checking Content
# ============================================

# startswith() and endswith() check string beginning/ending
print(m.startswith("Hello"))  # Output: True
print(m.startswith("World"))  # Output: False
print(m.endswith("World"))  # Output: True

# Check if string contains only digits, letters, etc.
num_str = "12345"
alpha_str = "Hello"
alnum_str = "Hello123"

print(num_str.isdigit())  # Output: True (all digits)
print(alpha_str.isalpha())  # Output: True (all alphabetic)
print(alnum_str.isalnum())  # Output: True (alphanumeric)
print(m.isalpha())  # Output: False (contains space)

# Other useful checks
print("HELLO".isupper())  # Output: True
print("hello".islower())  # Output: True
print("   ".isspace())  # Output: True (all whitespace)


# ============================================
# STRING CONCATENATION
# ============================================

# Using the + operator
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # Output: John Doe

# String repetition using *
print("Ha" * 3)  # Output: HaHaHa
print("-" * 20)  # Output: --------------------


# ============================================
# STRING FORMATTING
# ============================================

name = "Alice"
age = 25

# Method 1: f-strings (modern, recommended - Python 3.6+)
print(f"My name is {name} and I am {age} years old")
print(f"Next year I'll be {age + 1}")

# Method 2: format() method
print("My name is {} and I am {} years old".format(name, age))
print("My name is {0} and I am {1} years old. {0} is my first name.".format(name, age))

# Method 3: % formatting (old style)
print("My name is %s and I am %d years old" % (name, age))


# ============================================
# THE 'in' OPERATOR
# ============================================

# Check if a substring exists in a string
print("World" in m)  # Output: True
print("Python" in m)  # Output: False
print("Hello" not in m)  # Output: False


# ============================================
# STRING IMMUTABILITY
# ============================================

# Strings cannot be changed in place
original = "Hello"
# original[0] = "J"  # TypeError: 'str' object does not support item assignment

# Instead, create a new string
modified = "J" + original[1:]
print(modified)  # Output: Jello


# ============================================
# THE dir() METHOD - Discovering String Methods
# ============================================

# dir() returns a list of all attributes and methods of an object
# Very useful for exploring what you can do with strings
sample_string = "Python"

# Get all methods and attributes available on a string
all_methods = dir(sample_string)
print("All string methods and attributes:")
print(all_methods)

# Filter out private/magic methods (those starting with underscore)
public_methods = [method for method in dir(sample_string) if not method.startswith('_')]
print("\nPublic string methods only:")
print(public_methods)
# Output will include: capitalize, casefold, center, count, encode, endswith,
# expandtabs, find, format, format_map, index, isalnum, isalpha, isascii,
# isdecimal, isdigit, isidentifier, islower, isnumeric, isprintable, isspace,
# istitle, isupper, join, ljust, lower, lstrip, maketrans, partition, removeprefix,
# removesuffix, replace, rfind, rindex, rjust, rpartition, rsplit, rstrip,
# split, splitlines, startswith, strip, swapcase, title, translate, upper, zfill

# You can also use dir() on the str class itself
print("\nMethods from str class:")
print([method for method in dir(str) if not method.startswith('_')])

# Using help() to get detailed information about a specific method
print("\n" + "="*50)
print("Help for the upper() method:")
print("="*50)
help(str.upper)

print("\n" + "="*50)
print("Help for the replace() method:")
print("="*50)
help(str.replace)


# ============================================
# BONUS: Some Lesser-Known String Methods
# ============================================

# center() - centers the string within a given width
print("Python".center(20, "-"))  # Output: -------Python-------

# ljust() and rjust() - left and right justify
print("Python".ljust(10, "*"))  # Output: Python****
print("Python".rjust(10, "*"))  # Output: ****Python

# zfill() - pads string with zeros on the left
print("42".zfill(5))  # Output: 00042
print("-42".zfill(5))  # Output: -0042

# expandtabs() - replaces tabs with spaces
tabbed = "Hello\tWorld"
print(tabbed.expandtabs(4))  # Output: Hello   World (tab = 4 spaces)

# removeprefix() and removesuffix() - Python 3.9+
filename = "document.pdf"
print(filename.removesuffix(".pdf"))  # Output: document
url = "https://example.com"
print(url.removeprefix("https://"))  # Output: example.com

# splitlines() - splits string by line breaks
multiline = "Line 1\nLine 2\nLine 3"
print(multiline.splitlines())  # Output: ['Line 1', 'Line 2', 'Line 3']

# partition() - splits string into 3 parts at first occurrence of separator
email = "user@example.com"
print(email.partition("@"))  # Output: ('user', '@', 'example.com')

# rpartition() - same as partition but from the right
path = "/home/user/documents/file.txt"
print(path.rpartition("/"))  # Output: ('/home/user/documents', '/', 'file.txt')