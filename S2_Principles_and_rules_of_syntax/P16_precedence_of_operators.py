"""
Precedence of operators
    1 => ()
    2 => **
    3 => ~
    4 => - + (plus/minus)
    5 => *
    6 => /
    7 => %
    8 => - + (addition / subtraction)
    9 => <<, >>
    10 => &
    11 => ^
    12 => |
    13 => in, not in, is, is not, >, <, >=, <=, ==, !=
    14 => not
    15 => and
    16 => or

    According to this table, mathematical and logical expressions in Python are executed based on these priorities.
    For example, in the expression 3 + 5 * 2, the priority of multiplication and division is higher than addition,
    so 5 * 2 is executed first and then the number 3 is added to it.
"""
