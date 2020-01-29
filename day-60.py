"""
This problem was asked by Facebook.

Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up into two subsets that add up to the same sum.
"""
def checkSubset(arr, s, i):
    if s == 0:
        return True
    if i == len(arr)-1:
        if s == arr[i]:
            return True
        else:
            return False
    # Check for including and excluding ith element
    if arr[i] <= s:
        return checkSubset(arr, s-arr[i], i+1) or checkSubset(arr, s, i+1)
    # Check excluding the ith element only
    else:
        return checkSubset(arr, s, i+1)

def partition(arr):
    S = sum(arr)
    if S&1:
        return False
    else:
        return checkSubset(arr, S/2, 0)

arr = [15, 5, 20, 10, 35, 15, 10]
print(partition(arr))
arr = [15, 5, 20, 10, 35]
print(partition(arr))
