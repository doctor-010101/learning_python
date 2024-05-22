# Decorators in Python are tools that allow you to modify or extend the behavior of functions or methods without changing their original code. Decorators are essentially functions that take another function as an argument and return a new function with enhanced behavior.

# Defining a Decorator

# To define a decorator, you first create a function that takes another function as its input and returns a new function. For example:


import time


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# Here, `my_decorator` is a decorator that prints messages before and after the execution of any function it decorates.

# Using a Decorator

# To use a decorator, you can apply it to a function using the `@` symbol followed by the decorator name:


@my_decorator
def say_hello():
    print("Hello!")


say_hello()


# The output of this code will be:
# ```
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.

# A More Comprehensive Example

# Let's create a decorator that measures the execution time of a function using the `time` module:


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {
              end_time - start_time:.4f} seconds to execute.")
        return result
    return wrapper


# Now, we can use this decorator to decorate other functions:


@timer_decorator
def long_running_function():
    time.sleep(2)
    print("Function complete.")


long_running_function()


# The output of this code will be:
# Function complete.
# Function long_running_function took 2.0001 seconds to execute.

# Decorators with Parameters

# Sometimes you need decorators that accept parameters. To achieve this, you can create a function that returns a decorator:

def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


# You can now use this parameterized decorator:


@repeat(num_times=3)
def say_hello():
    print("Hello!")


say_hello()


# The output of this code will be:

# Hello!
# Hello!
# Hello!


# Class Method Decorators

# You can also use decorators with class methods. For example, let's modify a class method with a decorator:


def method_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling method {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Method {func.__name__} finished")
        return result
    return wrapper


class MyClass:
    @method_decorator
    def method(self):
        print("Method is running")


obj = MyClass()
obj.method()

# The output of this code will be:

# Calling method method
# Method is running
# Method method finished

# Conclusion

# Decorators in Python are powerful tools that allow you to modify the behavior of functions and methods in a clean, maintainable, and flexible way. By using decorators, you can enhance your code with additional functionality while keeping your codebase clean and readable.
