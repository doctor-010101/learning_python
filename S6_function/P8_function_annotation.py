"""

Function annotation" is a feature in programming languages that allows developers to provide additional information about the inputs and outputs of a function within its definition.
These annotations often take the form of annotations or descriptions within the code, aiding the compiler or development environment in improving the process of analysis and execution of the program.

In many languages, annotations are used as text strings or special symbols such as ":" or "->" in the function definition, usually appearing at the beginning of a function after its name.

This feature has been introduced as a new feature in some languages like Python and has various applications. Some of its use cases include:

Specifying the data type of inputs and outputs: For example, in Python, you can use annotations to specify the data type that a function takes as input or returns as output. For instance:
python

"""


def add(x: int, y: int = 9) -> int:
    return x + y


"""

In this example, ": int" for inputs and "-> int" for the function's return value specify that the inputs and output of this function are integers.

Code readability: Annotations can make the code more understandable for readers and facilitate the understanding of a function's behavior.
Usage in code analysis tools and IDEs: Many Integrated Development Environments (IDEs) have the capability to analyze annotations and use this information to provide suggestions and apply additional analysis.
Usage in tests: Annotations can be used to determine the data type of inputs and outputs in tests, helping to ensure that tests are executed correctly and errors are easily identified.
In summary, using annotations in function definitions helps developers make the code more understandable and maintainable, reducing errors in the process.

"""


# In Python, you can use the "__annotations__" attribute to access the annotations of a function.
# This attribute allows you to retrieve the annotations for the parameters and return type of a function.

def add(x: int, y: int) -> int:
    return x + y

annotations = add.__annotations__
print(annotations)  # Output: {'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'int'>}

# In this code snippet, annotations is a dictionary where the keys are the parameter names ('x' and 'y') and the return type ('return'), and the values are the corresponding data types.
# If a function is defined without annotations, __annotations__ returns an empty dictionary.


# 🍀☘️🍀 what is mypy?

# Mypy is a tool used for performing static type checking and analysis of data types in Python code. It helps developers identify type-related errors before runtime, allowing them to prevent potential issues proactively.

# Using the type annotations defined in function signatures and variable declarations, Mypy analyzes the code and reports type-related errors. The tool supports standard Python data types such as integers, strings, lists, and dictionaries, as well as custom types defined by programmers.

# With Mypy, you can specify data types for variables, function inputs, and outputs, ensuring that your code conforms to type standards. This practice can enhance code readability, maintainability, and quality.

# In essence, Mypy serves as a valuable tool for ensuring code correctness in Python and can be particularly beneficial in the development of large and complex applications.