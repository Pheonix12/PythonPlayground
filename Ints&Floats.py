# ============================================
# NUMBER BASICS - Integers and Floats
# ============================================

# Integers are whole numbers (no decimal point)
num = 3
print(num)  # Output: 3
print(type(num))  # Output: <class 'int'>

# Floats are decimal numbers
num = 3.14
print(num)  # Output: 3.14
print(type(num))  # Output: <class 'float'>

# Python automatically uses the right type
a = 5  # int
b = 5.0  # float
c = 5.5  # float
print(f"{a} is {type(a)}, {b} is {type(b)}, {c} is {type(c)}")

# Numbers can be negative
negative_int = -10
negative_float = -3.14
print(negative_int, negative_float)  # Output: -10 -3.14

# Underscores can make large numbers readable (Python 3.6+)
big_number = 1_000_000  # Same as 1000000
print(big_number)  # Output: 1000000


# ============================================
# ARITHMETIC OPERATORS
# ============================================

# Addition (+)
print(3 + 2)  # Output: 5
print(3.5 + 2.5)  # Output: 6.0

# Subtraction (-)
print(10 - 3)  # Output: 7
print(5.5 - 2.5)  # Output: 3.0

# Multiplication (*)
print(3 * 4)  # Output: 12
print(2.5 * 4)  # Output: 10.0

# Division (/) - Always returns a float
print(10 / 2)  # Output: 5.0 (float, not int!)
print(10 / 3)  # Output: 3.3333333333333335

# Floor Division (//) - Rounds down to nearest integer
print(10 // 3)  # Output: 3 (removes decimal part)
print(10 // 4)  # Output: 2
print(-10 // 3)  # Output: -4 (rounds down, not towards zero)

# Modulus (%) - Returns the remainder
print(10 % 3)  # Output: 1 (10 divided by 3 leaves remainder 1)
print(3 % 2)  # Output: 1
print(10 % 2)  # Output: 0 (no remainder, 10 is even)

# Exponentiation (**) - Raises to a power
print(2 ** 3)  # Output: 8 (2 to the power of 3)
print(5 ** 2)  # Output: 25
print(2 ** 0.5)  # Output: 1.4142135623730951 (square root)

# Order of Operations (PEMDAS/BODMAS)
print(3 * 2 + 1)  # Output: 7 (multiplication first)
print(3 * (2 + 1))  # Output: 9 (parentheses first)
print(2 + 3 * 4 ** 2)  # Output: 50 (exponent, then multiply, then add)


# ============================================
# ASSIGNMENT OPERATORS
# ============================================

# Basic assignment
n = 1
print(n)  # Output: 1

# Add and assign (+=)
n = 1
n = n + 1  # Traditional way
print(n)  # Output: 2

n = 1
n += 1  # Shorthand way
print(n)  # Output: 2

# Other compound assignment operators
n = 10
n -= 3  # Same as: n = n - 3
print(n)  # Output: 7

n = 5
n *= 2  # Same as: n = n * 2
print(n)  # Output: 10

n = 20
n /= 4  # Same as: n = n / 4
print(n)  # Output: 5.0

n = 17
n //= 5  # Same as: n = n // 5
print(n)  # Output: 3

n = 10
n %= 3  # Same as: n = n % 3
print(n)  # Output: 1

n = 2
n **= 3  # Same as: n = n ** 3
print(n)  # Output: 8


# ============================================
# COMPARISON OPERATORS
# ============================================

# Equal to (==)
print(5 == 5)  # Output: True
print(5 == 6)  # Output: False

# Not equal to (!=)
print(5 != 6)  # Output: True
print(5 != 5)  # Output: False

# Greater than (>)
print(10 > 5)  # Output: True
print(5 > 10)  # Output: False

# Less than (<)
print(5 < 10)  # Output: True
print(10 < 5)  # Output: False

# Greater than or equal to (>=)
print(10 >= 10)  # Output: True
print(10 >= 5)  # Output: True

# Less than or equal to (<=)
print(5 <= 10)  # Output: True
print(5 <= 5)  # Output: True

# Comparing floats and integers
print(5 == 5.0)  # Output: True (values are equal)
print(5 is 5.0)  # Output: False (different types)


# ============================================
# TYPE CONVERSION
# ============================================

# Converting to integer with int()
float_num = 3.9
print(int(float_num))  # Output: 3 (truncates decimal, doesn't round)
print(int(3.1))  # Output: 3
print(int(-3.9))  # Output: -3

# Converting strings to integers
num_string = "100"
print(int(num_string))  # Output: 100
print(type(int(num_string)))  # Output: <class 'int'>

# Converting to float with float()
int_num = 5
print(float(int_num))  # Output: 5.0

string_num = "3.14"
print(float(string_num))  # Output: 3.14

# Converting numbers to strings with str()
number = 42
print(str(number))  # Output: "42"
print(type(str(number)))  # Output: <class 'str'>

# Be careful with invalid conversions
# print(int("hello"))  # ValueError: invalid literal for int()
# print(int("3.14"))  # ValueError: invalid literal for int() with base 10


# ============================================
# BUILT-IN MATH FUNCTIONS
# ============================================

# abs() - Returns absolute value (removes negative sign)
print(abs(-5))  # Output: 5
print(abs(5))  # Output: 5
print(abs(-3.14))  # Output: 3.14

# round() - Rounds to nearest integer or specified decimal places
print(round(3.7))  # Output: 4
print(round(3.4))  # Output: 3
print(round(3.5))  # Output: 4 (rounds to nearest even number when exactly .5)
print(round(2.5))  # Output: 2 (banker's rounding)
print(round(3.14159, 2))  # Output: 3.14 (2 decimal places)
print(round(3.14159, 3))  # Output: 3.142

# pow() - Raises number to a power (same as ** operator)
print(pow(2, 3))  # Output: 8 (2 to the power of 3)
print(pow(5, 2))  # Output: 25

# pow() with 3 arguments: pow(base, exp, mod) - efficient for modular arithmetic
print(pow(2, 3, 5))  # Output: 3 (2^3 = 8, then 8 % 5 = 3)

# min() - Returns the smallest value
print(min(5, 10, 3, 8))  # Output: 3
print(min([5, 10, 3, 8]))  # Output: 3 (can also take a list)

# max() - Returns the largest value
print(max(5, 10, 3, 8))  # Output: 10
print(max([5, 10, 3, 8]))  # Output: 10

# sum() - Adds all numbers in an iterable
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))  # Output: 15
print(sum([10, 20, 30]))  # Output: 60


# ============================================
# THE MATH MODULE - Advanced Math Functions
# ============================================

import math

# Constants
print(math.pi)  # Output: 3.141592653589793
print(math.e)  # Output: 2.718281828459045

# Floor and ceiling
print(math.floor(3.7))  # Output: 3 (rounds down)
print(math.floor(3.1))  # Output: 3
print(math.ceil(3.1))  # Output: 4 (rounds up)
print(math.ceil(3.9))  # Output: 4

# Square root
print(math.sqrt(16))  # Output: 4.0
print(math.sqrt(2))  # Output: 1.4142135623730951

# Trigonometric functions (input in radians)
print(math.sin(math.pi / 2))  # Output: 1.0 (sine of 90 degrees)
print(math.cos(0))  # Output: 1.0
print(math.tan(math.pi / 4))  # Output: 0.9999999999999999 (approximately 1)

# Converting between degrees and radians
print(math.radians(180))  # Output: 3.141592653589793 (180 degrees = π radians)
print(math.degrees(math.pi))  # Output: 180.0

# Logarithms
print(math.log(math.e))  # Output: 1.0 (natural log, base e)
print(math.log10(100))  # Output: 2.0 (log base 10)
print(math.log(8, 2))  # Output: 3.0 (log base 2 of 8)

# Factorial
print(math.factorial(5))  # Output: 120 (5! = 5*4*3*2*1)
print(math.factorial(0))  # Output: 1

# Power and exponential
print(math.pow(2, 3))  # Output: 8.0 (returns float, unlike ** operator)
print(math.exp(1))  # Output: 2.718281828459045 (e^1)

# Greatest common divisor
print(math.gcd(48, 18))  # Output: 6

# Check if number is finite or infinite
print(math.isfinite(100))  # Output: True
print(math.isinf(float('inf')))  # Output: True
print(math.isnan(float('nan')))  # Output: True (Not a Number)


# ============================================
# NUMBER FORMATTING
# ============================================

num = 3.14159265359

# f-strings with formatting (Python 3.6+)
print(f"{num}")  # Output: 3.14159265359
print(f"{num:.2f}")  # Output: 3.14 (2 decimal places)
print(f"{num:.4f}")  # Output: 3.1416 (4 decimal places)

# Formatting with commas for thousands
big_num = 1000000
print(f"{big_num:,}")  # Output: 1,000,000

# Combining decimal places and thousands separator
price = 1234567.89
print(f"{price:,.2f}")  # Output: 1,234,567.89

# Percentage formatting
ratio = 0.75
print(f"{ratio:.0%}")  # Output: 75%
print(f"{ratio:.2%}")  # Output: 75.00%

# Padding and alignment
number = 42
print(f"{number:5}")  # Output: "   42" (right-aligned in 5 spaces)
print(f"{number:05}")  # Output: "00042" (zero-padded)
print(f"{number:<5}")  # Output: "42   " (left-aligned)
print(f"{number:^5}")  # Output: " 42  " (centered)

# Scientific notation
big = 123456789
print(f"{big:.2e}")  # Output: 1.23e+08

# format() method
print("{:.2f}".format(3.14159))  # Output: 3.14
print("{:,}".format(1000000))  # Output: 1,000,000


# ============================================
# CHECKING NUMBER PROPERTIES
# ============================================

# Check if a number is an integer (for floats)
x = 5.0
y = 5.5
print(x.is_integer())  # Output: True (5.0 is a whole number)
print(y.is_integer())  # Output: False

# Check if variable is a specific type
num1 = 5
num2 = 5.5
print(isinstance(num1, int))  # Output: True
print(isinstance(num2, int))  # Output: False
print(isinstance(num2, float))  # Output: True
print(isinstance(num1, (int, float)))  # Output: True (checks multiple types)

# Even or odd check using modulus
number = 10
if number % 2 == 0:
    print(f"{number} is even")  # Output: 10 is even
else:
    print(f"{number} is odd")  # This won't run because 10 is even


# ============================================
# SPECIAL NUMERIC VALUES
# ============================================

# Infinity
positive_inf = float('inf')
negative_inf = float('-inf')
print(positive_inf)  # Output: inf
print(positive_inf > 1000000)  # Output: True (infinity is larger than any number)

# Not a Number (NaN)
nan = float('nan')
print(nan)  # Output: nan
print(nan == nan)  # Output: False (NaN is never equal to anything, even itself!)
print(math.isnan(nan))  # Output: True (proper way to check for NaN)


# ============================================
# INCREMENT AND DECREMENT
# ============================================

# Python doesn't have ++ or -- operators like other languages
# Instead, use += and -=

counter = 0
counter += 1  # Increment by 1
print(counter)  # Output: 1

counter -= 1  # Decrement by 1
print(counter)  # Output: 0

# Increment/decrement by other amounts
score = 100
score += 10  # Add 10
print(score)  # Output: 110

score -= 5  # Subtract 5
print(score)  # Output: 105


# ============================================
# NUMBER METHODS WITH dir()
# ============================================

# Using dir() to discover methods
sample_int = 42
sample_float = 3.14

print("Methods for integers:")  # Output: Methods for integers:
int_methods = [method for method in dir(sample_int) if not method.startswith('_')]
print(int_methods)  # Output: ['as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

print("\nMethods for floats:")  # Output: (blank line) Methods for floats:
float_methods = [method for method in dir(sample_float) if not method.startswith('_')]
print(float_methods)  # Output: ['as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']

# Some useful methods:
print("\nInteger methods:")  # Output: (blank line) Integer methods:
print((5).bit_length())  # Output: 3 (number of bits needed to represent 5)
print(int.from_bytes(b'\x00\x10', byteorder='big'))  # Output: 16

print("\nFloat methods:")  # Output: (blank line) Float methods:
print((3.14159).as_integer_ratio())  # Output: (3537115888337719, 1125899906842624)
print((5.0).is_integer())  # Output: True


# ============================================
# PRACTICAL EXAMPLES
# ============================================

# Calculate area of a circle
radius = 5
area = math.pi * radius ** 2
print(f"Area of circle with radius {radius}: {area:.2f}")  # Output: Area of circle with radius 5: 78.54

# Calculate compound interest
principal = 1000  # Initial amount
rate = 0.05  # 5% interest rate
time = 3  # years
amount = principal * (1 + rate) ** time
print(f"Amount after {time} years: ${amount:.2f}")  # Output: Amount after 3 years: $1157.63

# Convert Celsius to Fahrenheit
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")  # Output: 25°C = 77.0°F

# Calculate average
grades = [85, 90, 78, 92, 88]
average = sum(grades) / len(grades)
print(f"Average grade: {average:.1f}")  # Output: Average grade: 86.6

# Find hypotenuse of right triangle (Pythagorean theorem)
a = 3
b = 4
c = math.sqrt(a**2 + b**2)
print(f"Hypotenuse: {c}")  # Output: Hypotenuse: 5.0


# ============================================
# RANDOM NUMBERS (BONUS)
# ============================================

import random

# Random integer in a range
print(random.randint(1, 10))  # Output: (random number like 7, 3, 10, etc. - changes each time)

# Random float between 0 and 1
print(random.random())  # Output: (random float like 0.7234567890123456 - changes each time)

# Random float in a range
print(random.uniform(1.5, 6.5))  # Output: (random float between 1.5 and 6.5, like 4.23456 - changes each time)

# Random choice from a list
numbers = [10, 20, 30, 40, 50]
print(random.choice(numbers))  # Output: (randomly picks one like 20, 50, 10, etc. - changes each time)

# Shuffle a list
deck = [1, 2, 3, 4, 5]
random.shuffle(deck)  # No output - modifies list in place
print(deck)  # Output: (randomly shuffled like [3, 1, 5, 2, 4] - changes each time)
