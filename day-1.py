"""
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
"""
arr = [10, 15, 3, 7]
sum = 17

def pairSum(arr, sum):
    hashTable = {} # Create a hash table
    hashTable[arr[0]] = 0 # Add first element to hash table
    for i in range(1, len(arr)): # Loop through array
        currentElement = arr[i]
        requiredElement = sum - currentElement # We require sum - current Element to exist in array
        if requiredElement in hashTable:
            return True # return True if required element was found
    return False # return False if required element was not found

print(pairSum(arr, sum)) # True