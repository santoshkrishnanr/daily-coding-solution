"""
This problem was asked by Google.

Given an array of integers where every integer occurs three times except for one integer, 
which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
"""
def getUnique(arr):
    ones = 0
    twos = 0
    for elem in arr:
        twos = twos | (ones & elem)
        ones = ones ^ elem
        not_threes = ~(ones & twos)
        ones = ones & not_threes
        twos = twos & not_threes
    return ones

print(getUnique([6, 1, 3, 3, 3, 6, 6])) # 1
print(getUnique([13, 19, 13, 13])) # 19