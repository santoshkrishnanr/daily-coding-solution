"""
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.

For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr.
"""

# timesN accepts a number N and returns a function that accepts x
# The returned function uses x and N and returns a value (in this case, multiply x and N)
def timesN(N):
    def multiply(x):
        return x*N
    return multiply

times5 = timesN(5)
print(times5(2))

# cons accepts two items a, b and 
# returns a function that accepts a function f
# The returned function uses f and a, b 
# and returns the value of f(a, b)
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def left(a, b):
    return a

def right(a, b):
    return b

print(cons(3, 4)(left)) # 3
print(cons(3, 4)(right)) # 4

# Since we wanted functions
# Rewriting the above two lines
def car(x):
    def left(a, b):
        return a
    return x(left)

def cdr(x):
    def right(a, b):
        return b
    return x(right)

print(car(cons(3, 4))) # 3
print(cdr(cons(3, 4))) # 4