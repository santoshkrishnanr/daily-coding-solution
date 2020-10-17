"""
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
run time pairSum 0.049 -0.031
run time for sanlist 0.029
"""
arr = [10, 15, 3, 7]
sum = 22
def sanlist(arr,sum):
    lis= arr
    s= sum
    for i in range(0, len(lis)): 
        requiredElement = s - lis[0]         #element to be searched  
        lis.remove(lis[0])                   # remove the element 
        if requiredElement in lis:           #compare with others 
            return True # return True if required element was found
    return False # return False if required element was not found

print(sanlist(arr, sum))

