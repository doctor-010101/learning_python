# Modular programming is a software development approach where a large program is divided into smaller parts called modules. Each module implements a specific functionality of the program and can be developed, tested, and maintained independently.

### Benefits of Modular Programming:
# 1. Maintainability: Dividing the program into smaller modules makes it easier to update and modify the code.
# 2. Reusability: Modules can be reused across different projects.
# 3. Readability: Code is written in smaller, well-defined modules, making it more readable and easier to understand.
# 4. Testability: Each module can be tested independently, simplifying the debugging process.
# 5. Team Collaboration: Multiple developers can work on different parts of the program simultaneously without much interference.

### Drawbacks of Modular Programming:
# 1. Complexity in Managing Modules: Managing a large number of modules can become complicated.
# 2. Performance Overhead: In some cases, dividing the code into multiple modules can introduce performance overhead.
# 3. Need for Careful Design: Effective modular programming requires careful planning and design to ensure that modules are well-defined and properly separated.

### Example in Python:

# Let's assume we want to create a program for managing a library. This program includes adding books, removing books, and listing all the books.

# First, we define each part of the program as a module.

# **Module library.py:**

# library.py

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'Book "{book}" added to the library.')

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f'Book "{book}" removed from the library.')
        else:
            print(f'Book "{book}" not found in the library.')

    def list_books(self):
        if self.books:
            print("Books in the library:")
            for book in self.books:
                print(f'- {book}')
        else:
            print("No books in the library.")


# **Module main.py:**


# main.py

# from library import Library

def main():
    my_library = Library()

    # Adding books
    my_library.add_book("1984")
    my_library.add_book("Brave New World")

    # Listing books
    my_library.list_books()

    # Removing a book
    my_library.remove_book("1984")
    my_library.list_books()

if __name__ == "__main__":
    main()


### Explanation:
# 1. In the library.py module, the Library class is defined, which handles the tasks related to managing books.
# 2. The main.py module is the main program that uses the Library class to add, remove, and list books.

### Result:
# This modular approach ensures that if we need to change or add functionality to the library, we only need to modify the library.py module without touching the main program (main.py). Additionally, these modules can easily be reused in other projects.