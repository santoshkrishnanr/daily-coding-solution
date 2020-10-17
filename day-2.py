"""
This problem was asked by Uber.
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
"""

import numpy as np

def remainingProduct(arr):

    n = len(arr)
    list1 = [0]*n
    for i in range(0, n):
        b = arr[0]
        arr.remove(arr[0])
        c = np.prod(arr)
        list1[i]= c
        arr=arr+[b]
    return list1

print(remainingProduct([3, 2, 1]))#[2, 3, 6].
print(remainingProduct([1, 2, 3, 4, 5])) # [120, 60, 40, 30, 24]

