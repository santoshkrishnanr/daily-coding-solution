"""
This problem was asked by Facebook.

You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.
"""

def countWater(arr):
    total = 0 
    for i in range(0, len(arr)):
        # Find the taller wall on left of this element
        big_left = -1
        for j in range(i-1, -1, -1):
            if arr[j] > arr[i]:
                big_left = j
                break
        # Find the taller wall on right of this element
        big_right = -1
        for j in range(i+1, len(arr)):
            if arr[j] > arr[i]:
                big_right = j
                break
        # If there are taller walls on left and right
        if big_left > -1 and big_right > -1:
            total += (min(arr[big_left], arr[big_right])-arr[i])*(big_right-big_left-1)
    return total

print(countWater([2, 1, 2])) # 1
print(countWater([3, 0, 1, 3, 0, 5])) # 8
