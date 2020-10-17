"""
This problem was asked by Uber.
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
"""
def remainingProduct(arr):
    n = len(arr)
    a = [1]
    b = [1]
    for i in range(0, n-1):
        a.append(a[i]*arr[i])
        b.append(b[i]*arr[n-1-i])
    b.reverse()
    c = [a[i] * b[i] for i in range(0, n)]
    return c

print(remainingProduct([1, 2, 3, 4, 5])) # [120, 60, 40, 30, 24]
print(remainingProduct([1, 2, 3])) # [6, 3, 2]
