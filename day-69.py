"""
This problem was asked by Facebook.

Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
"""
def maxProduct(arr):
    arr.sort()
    if arr[0]*arr[1] > arr[-1]*arr[-2]:
        return arr[0]*arr[1]*arr[-1]
    else:
        return arr[-1]*arr[-2]*arr[-3]

arr = [-10, -10, 5, 2]
print(maxProduct(arr))