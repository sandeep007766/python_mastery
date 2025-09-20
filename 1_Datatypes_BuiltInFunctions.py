# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

"""
Python is Dynamically typed Programming language.
dynamically typed language refers to a language in which the type of variable is determined at runtime, rather than at compile time.
Python is considered a dynamically typed language because you don't need to explicitly declare the type of variable when you define it.
The Python interpreter infers the type of the variable during program execution.
"""

"""
Data Types: 

Numeric Data Types:
int: Represents integers (whole numbers). Example: x = 5
float: Represents floating-point numbers (numbers with decimal points). Example: y = 3.14
complex: Represents complex numbers. Example: z = 2 + 3j

Sequence Types:
str: Represents strings (sequences of characters). Example: text = "Hello, World"
list: Represents lists (ordered, mutable sequences). Example: my_list = [1, 2, 3]
tuple: Represents tuples (ordered, immutable sequences). Example: my_tuple = (1, 2, 3)

Mapping Type:
dict: Represents dictionaries (key-value pairs). Example: my_dict = {'name': 'John', 'age': 30}

Set Types:
set: Represents sets (unordered collections of unique elements). Example: my_set = {1, 2, 3}
frozenset: Represents immutable sets. Example: my_frozenset = frozenset([1, 2, 3])

Boolean Type:
bool: Represents Boolean values (True or False). Example: is_valid = True

Binary Types:
bytes: Represents immutable sequences of bytes. Example: data = b'Hello'
bytearray: Represents mutable sequences of bytes. Example: data = bytearray(b'Hello')

None Type:
NoneType: Represents the None object, which is used to indicate the absence of a value or a null value.

Custom Data Types:
You can also define your custom data types using classes and objects.
"""

"""
Inbuilt Functions:

String: You can access individual characters in a string using indexing, e.g., my_string[0] will give you the first character.
Strings support various built-in methods, such as len(), upper(), lower(), strip(), replace(), and more, for manipulation.

String Manipulation and Formatting:
Concatenation: You can combine strings using the + operator.
Substrings: Use slicing to extract portions of a string, e.g., my_string[2:5] will extract characters from the 2nd to the 4th position.
String interpolation: Python supports various ways to format strings, including f-strings (f"...{variable}..."), %-formatting ("%s %d" % ("string", 42)), and str.format().
Escape sequences: Special characters like newline (\n), tab (\t), and others are represented using escape sequences.
String methods: Python provides many built-in methods for string manipulation, such as split(), join(), and startswith().

Numeric Data Types in Python (int, float):
Python supports two primary numeric data types: int for integers and float for floating-point numbers.
Integers are whole numbers, and floats can represent both whole and fractional numbers.
You can perform arithmetic operations on these types, including addition, subtraction, multiplication, division, and more.
Be aware of potential issues with floating-point precision, which can lead to small inaccuracies in calculations.
Python also provides built-in functions for mathematical operations, such as abs(), round(), and math module for advanced functions.

Regular Expressions for Text Processing:
Regular expressions (regex or regexp) are a powerful tool for pattern matching and text processing.
The re module in Python is used for working with regular expressions.
Common metacharacters: . (any character), * (zero or more), + (one or more), ? (zero or one), [] (character class), | (OR), ^ (start of a line), $ (end of a line), etc.
Examples of regex usage: matching emails, phone numbers, or extracting data from text.
re module functions include re.match(), re.search(), re.findall(), and re.sub() for pattern matching and replacement.
"""
#Concate two strings

str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)

#length of string
text = "Python is awesome"
length = len(text)
print("Length of the string:", length)

#String lower and upper case
Message = "Hai Bro! Whatsup"
uppercase = Message.upper()
lowercase = Message.lower()
print("Upper case:", uppercase)
print("Lower case:", lowercase)

#Replace text
old_text = "Python is awesome"
new_text = old_text.replace("awesome", "great")
print("Modified text:", new_text)

#String split
text = "Python is awesome"
words = text.split()
print("Words:", words)

#Stripped Text
text = "   Some spaces around   "  # A string with leading and trailing spaces.
stripped_text = text.strip()  # Removes the leading and trailing whitespace from the string.
print("Stripped text:", stripped_text)  # Prints the result.

#SubString
text = "Python is awesome"
substring = "is"
if substring in text:
    print("Substring:", substring,  "found in the text")

#Float Variables
num1 = 5.0
num2 = 2
# Basic Arithmetic
result1 = num1 + num2
print("Addition:", result1)
result2 = num1 - num2
print("Subtraction:", result2)
result3 = num1 * num2
print("Multiplication:", result3)
result4 = num1 / num2
print("Division:", result4)
# Rounding
result5 = round(3.14559265359, 2)  # Rounds to 2 decimal places
print("Rounded:", result5)

# Integer variables
num1 = 10
num2 = 5
# Integer Division
result1 = num1 // num2
print("Integer Division:", result1)
# Modulus (Remainder)
result2 = num1 % num2
print("Modulus (Remainder):", result2)
# Absolute Value
result3 = abs(-7)
print("Absolute Value:", result3)
