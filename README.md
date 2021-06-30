# PythonFunctions

## Notes:
* A function is a block of code which only runs when it is called.
* You can pass data, known as parameters, into a function.
* A function can return data as a result. 
* To call a function, use the function name followed by parenthesis 
* Information can be passed into functions as arguments.
* Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
# Number of arguments
* By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less
# Parameters or arguments
- From a function's perspective:
- A parameter is the variable listed inside the parentheses in the function definition.
- An argument is the value that is sent to the function when it is called.
# Arbitrary arguments or *args
* If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# Keyword arguments or kwargs
* You can also send arguments with the key = value syntax.
* This way the order of the arguments does not matter.
# Arbitray keyword arguments or **kwargs
* If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
* This way the function will receive a dictionary of arguments, and can access the items accordingly:
# Default parameter value
* The following example shows how to use a default parameter value.
* If we call the function without argument, it uses the default value:

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")