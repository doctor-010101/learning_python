"""
We have two types:
    1 => Normal assignment by "=" 1
    2 => arithmetic assignment(first it is calculated and then the result is assigned) 12
"""

x = 10  # The right side is assigned to the left side.

x += 2  # Same as => x = x + 2, Result: 10 + 2 = 12 => x = 12

x -= 2  # Same as => x = x - 2, Result: 10 - 2 = 8 => x = 8

x *= 2  # Same as => x = x * 2, Result: 10 * 2 = 20 => x = 20

x /= 2  # Same as => x = x / 2, Result: 10 / 2 = 5.0 => x = 5.0

x %= 2  # Same as => x = x % 2, Result: 10 % 2 = 0 => x = 0

x //= 2  # Same as => x = x // 2, Result: 10 // 2 = 5 => x = 5

x **= 2  # Same as => x = x ** 2, Result: 10 ** 2 = 100 => x = 100

x &= 2  # Same as => x = x & 2, Result: 10 & 2 = 2 => x = 2

x |= 2  # Same as => x = x | 2, Result: 10 | 2 = 10 => x = 10

x ^= 2  # Same as => x = x ^ 2, Result: 10 ^ 2 = 8 => x = 8

x >>= 2  # Same as => x = x >> 2, Result: 10 >> 2 = 2 => x = 2

x <<= 2  # Same as => x = x << 2, Result: 10 << 2 = 40 => x = 40
