# Definition: 
# The datetime module in Python provides classes for manipulating dates and times, allowing you to work with time zones, durations, and formatted output.

# Detailed Explanation: This module includes several classes, such as datetime, date, time, and timedelta, which can be used to represent and manipulate date and time in both naive and aware formats.

# Useful Methods:

# 1. datetime.now(): Returns the current local date and time.

# 2. datetime.timedelta(days=...): Represents a duration, the difference between two dates or times.

# 3. datetime.strftime(format): Formats a datetime object as a string.

# Example:

# from datetime import datetime, timedelta

# # Current date and time
# now = datetime.now()
# print(f"Current date and time: {now}")

# # Creating a timedelta
# one_week_later = now + timedelta(weeks=1)
# print(f"One week later: {one_week_later}")

# # Formatting date and time
# formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
# print(f"Formatted date and time: {formatted_date}")

# Explanation of the example: This code snippet retrieves the current date and time, calculates a date one week later using timedelta, and formats the current date and time into a readable string. The strftime method allows you to specify the desired format for output.
