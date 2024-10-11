# import csv
# A CSV (Comma-Separated Values) file is a simple text file used to store tabular data (data in rows and columns). In a CSV file, each row represents a record, and within each row, the individual fields are separated by commas ( or sometimes other delimiters like semicolons or tabs).

# For example, a CSV file might look like this:

# name, age, city
# Hasan, 25, Tabriz
# Sara, 30, Tehran
# Ali, 22, Shiraz

# Key characteristics of CSV files:

# Simple format: CSV files are easy to create and read.

# Widely supported: Supported by most spreadsheet applications like Microsoft Excel and Google Sheets.

# Plain text: CSV files can be opened in any text editor.


# Working with CSV Files in Python

# In Python, you can use the built-in csv module to read from and write to CSV files.


# ---

# 1. Reading CSV files

# To read a CSV file, use csv.reader() which returns an iterable of rows from the file. Each row is a list of values(corresponding to each field in the row).

# Example:

# Assume we have a CSV file called data.csv with the following content:

# name, age, city
# Hasan, 25, Tabriz
# Sara, 30, Tehran
# Ali, 22, Shiraz

# To read this file:

#     # Open and read the CSV file
# with open('data.csv', 'r') as file:
#     csv_reader = csv.reader(file)

#     # Skip the header (optional)
#     next(csv_reader)

#     # Iterate through the rows
#     for row in csv_reader:
#         print(row)

# Output:

# ['Hasan', '25', 'Tabriz']
# ['Sara', '30', 'Tehran']
# ['Ali', '22', 'Shiraz']

# 2. Writing to a CSV file

# To write data to a CSV file, use csv.writer(), which allows you to write rows into the file.

# Example:

#     # Data to write to the CSV file
# data = [
#     ['name', 'age', 'city'],
#     ['Hasan', '25', 'Tabriz'],
#     ['Sara', '30', 'Tehran'],
#     ['Ali', '22', 'Shiraz']
# ]

# # Open and write to the CSV file
# with open('output.csv', 'w', newline='') as file:
#     csv_writer = csv.writer(file)

#     # Write each row to the file
#     csv_writer.writerows(data)

# This code creates a new output.csv file with the following content:

# name, age, city
# Hasan, 25, Tabriz
# Sara, 30, Tehran
# Ali, 22, Shiraz

# 3. Working with CSV files using dictionaries

# You can also work with CSV files where each row is treated as a dictionary. Use csv.DictReader() to read and csv.DictWriter() to write, where each row is a dictionary with the header values as keys.

# Reading with DictReader:

#     # Open and read the CSV file
# with open('data.csv', 'r') as file:
#     csv_reader = csv.DictReader(file)

#     for row in csv_reader:
#         print(row['name'], row['age'], row['city'])

# Output:

# Hasan 25 Tabriz
# Sara 30 Tehran
# Ali 22 Shiraz

# Writing with DictWriter:

#     # Data to write to the CSV file
# data = [
#     {'name': 'Hasan', 'age': 25, 'city': 'Tabriz'},
#     {'name': 'Sara', 'age': 30, 'city': 'Tehran'},
#     {'name': 'Ali', 'age': 22, 'city': 'Shiraz'}
# ]

# # Open and write to the CSV file
# with open('output.csv', 'w', newline='') as file:
#     # Define the fieldnames (keys)
#     fieldnames = ['name', 'age', 'city']

#     # Create a DictWriter object
#     csv_writer = csv.DictWriter(file, fieldnames=fieldnames)

#     # Write the header
#     csv_writer.writeheader()

#     # Write each dictionary (row)
#     csv_writer.writerows(data)

# This will write the following content to output.csv:

# name, age, city
# Hasan, 25, Tabriz
# Sara, 30, Tehran
# Ali, 22, Shiraz

# Summary of key functions:

# csv.reader(): Reads CSV rows as lists.

# csv.writer(): Writes rows(as lists) to a CSV file.

# csv.DictReader(): Reads CSV rows as dictionaries(with headers as keys).

# csv.DictWriter(): Writes rows(as dictionaries) to a CSV file.


# These methods provide a flexible way to handle CSV data in Python.
