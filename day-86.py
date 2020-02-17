"""
Given a string of parentheses, write a function to compute the minimum number of parentheses to be removed 
to make the string valid (i.e. each open parenthesis is eventually closed).

For example, given the string "()())()", you should return 1. 
Given the string ")(", you should return 2, since we must remove all of them.
"""
from collections import deque

def balancedParentheses(string):
    stack = deque()
    unbalanced = 0
    for elem in string:
        if elem == '(':
            unbalanced += 1
            stack.append(elem)
        elif elem == ')':
            if len(stack) > 0:
                if stack.pop() == '(':
                    unbalanced -= 1
                else:
                    unbalanced += 1
            else:
                unbalanced += 1
    return unbalanced

print(balancedParentheses("()())()"))
print(balancedParentheses(")("))