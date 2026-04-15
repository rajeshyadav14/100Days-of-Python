
"""
Variables : Variables are containers for storing data values.

Creating Variables : 
Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.
"""

x = 18
y = "Hidden"
print(x,y)


# Casting : If you want to specify the data type of a variable, this can be done with casting.

a = str(24)
b = int(18)
c = float(24)

print(a,b,c)
print(type(a),type(b),type(c))

"""
Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""

#Legal Variable Name 
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

print(myVar)


"""
Global Variables : 
Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.
Global variables can be used by everyone, both inside of functions and outside.
"""


A = "Hidden"
def myfunc():
    print("Rajesh is similar to " + A)
myfunc()
