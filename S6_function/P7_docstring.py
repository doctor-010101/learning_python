"""

🍀 Docstrings (or "documentation strings") in Python are strings of documentation and explanatory text within code,
commonly used to explain the functionality or usage of a function or class.

🍀 These explanations often serve to assist other programmers or even the programmer themselves in recalling the functionality of code sections at later times.

🍀 If Docstring is used outside the function, it is like a comment for the interpreter, otherwise it is a doc string.

🍀 Docstring is a brief description of the function's function and its writing is optional.

🍀 Nothing should be written before the documentation string.

🍀It is better to use """"""" to write the docstring, not '''''''


"""

# Example 👇


def add_numbers(a, b):
    """
    This function takes two numbers as input and returns their sum.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The sum of the two input numbers.
    """
    return a + b


""" 

Now, let's take a look at some key points to consider when writing docstrings:

🍀🍀 Functionality Explanation -> Docstrings should clearly and precisely explain the functionality of a function or class. This should include inputs, outputs, and any other important points that another programmer should know.
🍀🍀 Parameters and Data Types -> Provide the data type and a brief explanation for each parameter to assist other programmers in understanding how to use the code.
🍀🍀 Return Value -> If a function or method returns a value, provide a detailed explanation of the return data type and its meaning.
🍀🍀 Examples -> If possible, provide one or more examples of using the function in the docstring to help other programmers better understand its usage.

"""

# Now that you've written the docstring, how can you access it? In Python, you can access the docstring of a function or class using the built-in __doc__ attribute or the help() function.
# Accessing the docstring of a function using __doc__
print(add_numbers.__doc__)

# Accessing the docstring of a function using the help() function
help(add_numbers)


# ✔️ The difference between comments and docstrings :

"""

✅ Usage Location:

☘️☘️ Comments: They are placed within code as single or multi-line statements and are used to provide explanations or brief descriptions of a portion of the code.
☘️☘️ Docstrings: They are typically used to document and describe functions and classes in Python, appearing as multi-line string literals within the code.

✅ Content:

☘️☘️ Comments: Typically used to provide brief explanations or descriptions of the functionality or issues within the code.
☘️☘️ Docstrings: Used to provide comprehensive documentation and documentation about how to use a function or class, including inputs, outputs, and their functionalities.

✅ Formatting:

☘️☘️ Comments: They start with # at the beginning of the line and are usually located in the same line of code they explain.
☘️☘️ Docstrings: They are enclosed in triple quotes and usually appear at the top of a function or class.

✅ Use for Documentation:

☘️☘️ Comments: While they can be used for documentation, they are not primarily intended for this purpose and are not recommended for documenting and documenting code.
☘️☘️ Docstrings: They are recommended for documenting and documenting the main code and functions and classes, and various documentation tools use them to generate automatic documentation.

In general, docstrings are more recommended for documenting and documenting code, while comments are more for explanations and brief descriptions of the code.

"""