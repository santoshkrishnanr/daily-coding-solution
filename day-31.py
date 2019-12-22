"""
This problem was asked by Google.

The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. 
For example, the edit distance between “kitten” and “sitting” is three:
substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
"""
def editDistance(string1, string2):
    def helper(string1, string2, m, n):
        if m == 0:
            return n
        if n == 0:
            return m
        if string1[m-1] == string2[n-1]:
            return helper(string1, string2, m-1, n-1)
        else:
            return 1 + min(helper(string1, string2, m-1, n), helper(string1, string2, m, n-1), helper(string1, string2, m-1, n-1))
    return helper(string1, string2, len(string1), len(string2))

print(editDistance("kitten", "sitting"))