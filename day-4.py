"""
This problem was asked by Stripe.
Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place.
"""
def firstMissingPositive(arr):
    n = len(arr)
    end = n - 1

    # Find the first positive number in the back of the array 
    while arr[end] <= 0:
        end -= 1

    # Move the negative numbers to the back of the array
    i = 0
    while i <= end:
        if arr[i] <= 0:
            arr[i], arr[end] = arr[end], arr[i]
            end -= 1
        i += 1

    # There are end+1 positive integers in the array 

    # i=0 will indicate presence of 1
    # i=1 will indicate presence of 2
    # i=2 will indicate presence of 3...and so on 

    # Check all the positive integers
    for i in range(0, end+1):
        positive_num = abs(arr[i])
        # If a positive integer exists in the array, change the element at that index to indicate it's presence
        if positive_num <= end+1:
            arr[positive_num-1] *= -1

    # Check all the indexes to check which one is missing
    for i in range(0, end+1):
        # If index i is still positive, means i+1 was missing
        if arr[i] > 0:
            return i+1

    # Since all numbers from 1 to end+1 are present, end+2 is the first missing positive integer
    return end+2

print(firstMissingPositive([3, 4, -1, 1])) # 2
print(firstMissingPositive([0, 1, 2])) # 3