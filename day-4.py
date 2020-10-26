"""
This problem was asked by Stripe.
Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place.
"""


def MissingPositive(arr):

    minInArray = 1 #min([i for i in arr if i >= 0])

    while minInArray in arr:
        minInArray += 1

    return minInArray


print(MissingPositive([2,-1,-3, -4, -5])) # 1
# print(MissingPositive([0, 1,2,3,4,5,6]))#7
# print(MissingPositive([0,2,3,-4,-5,-6]))#1
#
# print(MissingPositive([3, 4, -1, 1])) #2
# print(MissingPositive([0, 1, 2])) #3