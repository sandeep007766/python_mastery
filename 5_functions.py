"""
A function in Python is a block of code that performs a specific task.
Functions are defined using the def keyword and can take inputs, called arguments.
They are a way to encapsulate and reuse code.
"""

# Addition without Function
num1 = 5
num2 = 10

addition = num1 + num2
print("Addition of two numbers: ", addition) # Under the hoods Python will automatically convert it to a string and print it alongside the other string.
print("Addition of two numbers: ", str(addition))
""" In this case, str(addition) explicitly converts the value of addition to a string before it is printed.
This is essentially the same as the first example, but the difference is that you're manually 
calling the str() function to convert the variable addition to a string."""
print(f"Addition of two numbers: {addition}")

# Subtraction with function
def subtraction():
     sub = num1 - num2
     print(f"Subtraction is: {sub}")
subtraction()

# Multiplication function with return
def multiplication():
    mul = num1 * num2
    return mul     # returning a variable
multiply = multiplication() # saving the value returning by function in multiply variable
print(f"Multiplication of two numbers: {multiply}")

# Division function with Arguments
def division(num3, num4):
    div = num3 / num4 # gives exact result in float value like 3.3333 "If we gave '//' then it will do floor division which gives only 3 as output"
    return f"Division of two numbers: {div}"
div_value = division(10,3)
print(div_value)

