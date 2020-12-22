# Code written by Jerin Rajan on 22nd Dec 2020
'''
Decorators allows to modify the behaviour of a function or a class 
Decorators allow us to wrap another function in order to extend the behavior of wrapped function, 
without permanently modifying it.
'''

# Decorator function - passing in a func as an input argument 
def decorator_fun(func):

# Wrapper function
# *args and *kwargs -> defining the arguments of the function, if not sure how many arguments & KeyArguments are present
    def wrapper_add_one(*args, **kwargs):
        
        print('inside wrapper')
        # calling the actual function - add_two() inside the wrapper
        out = func(*args, **kwargs)
        # adding +1 to the output of function - add_two()
        add_one = out + 1
        return add_one 

    return wrapper_add_one
     
# initiating decorator to modify the result after adding 1
@decorator_fun
# Original function - to add two to an input integer
def add_two(num):
    print('inside function')
    return num+2

# Getting value through return of the function after running via decorator
print(add_two(10))


