# In Python, a variable is a named storage location used to store data.
# Variables are essential for programming as they allow us to work with data, manipulate it, and make our code more flexible and reusable.

# Assigning a value to a variable
my_variable = 42

# Accessing the value of a variable
print(my_variable)  # Output: 42

# Variable Scope and Lifetime:
# Variable Scope: In Python, variables have different scopes, which determine where in the code the variable can be accessed.
# There are mainly two types of variable scopes:
""" Local Scope: Variables defined within a function have local scope and are only accessible inside that function. """

def my_function():
    x = 10  # Local variable
    print(x)

my_function()
# print(x)  # This will raise an error since 'x' is not defined outside the function.

""" Global Scope: Variables defined outside of any function have global scope and can be accessed throughout the entire code. """
# Example
y = 20  # Global variable

def another_function():
    print(y)  # This will access the global variable 'y'

another_function()
print(y)  # This will print 20

""" Variable Lifetime """
# The lifetime of a variable is determined by when it is created and when it is destroyed or goes out of scope.
# Local variables exist only while the function is being executed, while global variables exist for the entire duration of the program.

"""" Variable Naming Convention """
# Variable Naming Conventions and Best Practices:
# It's important to follow naming conventions and best practices for variables to write clean and maintainable code:
"""
Variable names should be descriptive and indicate their purpose.
Use lowercase letters and separate words with underscores (snake_case) for variable names. We can also use Camel case (ec2InstanceIdWithLocation).
Avoid using reserved words (keywords) for variable names.
Choose meaningful names for variables.
"""

# Practice Exercises and Examples:
""" Example: Using Variables to Store and Manipulate Configuration Data in a DevOps Context
In a DevOps context, you often need to manage configuration data for various services or environments. 
Variables are essential for this purpose. Let's consider a scenario where we need to store and manipulate configuration data for a web server. """

# Define configuration variables for a web server
server_name = "my_server"
port = 80
is_https_enabled = True
max_connections = 1000

# Print the configuration
print("Server Name:", server_name)
print(f"Port: {port}")
"""
F-string (formatted string literals), allows you to embed expressions or variables directly within a string. 
The expression inside curly braces {} is evaluated, and the result is included in the string.
An f-string is prefixed with the letter f or F, and expressions inside curly braces {} are replaced with their values during runtime.
"""
print(f"HTTPS Enabled: {is_https_enabled}")
print(f"Max Connections: {max_connections}")

# Update configuration values
port = 443
is_https_enabled = False

# Print the updated configuration
print(f"Updated Port: {port}")
print(f"Updated HTTPS Enabled: {is_https_enabled}")

# In this example, we use variables to store and manipulate configuration data for a web server. This allows us to easily update and manage the server's configuration in a DevOps context.
