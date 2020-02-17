"""
This question was asked by ContextLogic.

Implement division of two positive integers without using the division, multiplication, or modulus operators. Return the quotient as an integer, ignoring the remainder.
"""
def divide(dividend, divisor):
    sign = -1 if dividend < 0 or divisor < 0 else 1
    dividend = abs(dividend)
    divisor = abs(divisor)
    quotient = 0
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1
    return sign*quotient

print(divide(13, 3))