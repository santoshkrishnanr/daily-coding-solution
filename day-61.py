"""
This problem was asked by Google.

Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.
"""
def iexp(x, y):
    '''
    if y == 1:
        return x
    # If y is odd
    if y&1:
        return x * iexp(x, y-1)
    else:
        return iexp(x*x, y>>1)
    '''
    # Make a iterative version below:
    result = 1
    # While y is non-zero
    while y:
        # If y is odd
        if y&1:
            result = result * x
            y = y - 1
        # If y is even
        else:
            x = x * x
            # Half the value of y
            y = y >> 1
    return result

print(iexp(2, 10))
