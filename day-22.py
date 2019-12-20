"""
This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""
def splitWords(dictionary, string):
    # Maintain a hashtable to test membership
    hashtable = set()
    for elem in dictionary:
        hashtable.add(elem)

    result = []
    # Traverse the strings and check substrings
    start = 0
    while start < len(string):
        end = 0
        while end <= len(string):
            if string[start:end] in hashtable:
                result.append(string[start:end])
                start = end
            else:
                end += 1
    if start != len(string):
        return None
    return result

print(splitWords(['quick', 'brown', 'the', 'fox'], "thequickbrownfox")) # ['the', 'quick', 'brown', 'fox']
print(splitWords(['bed', 'bath', 'bedbath', 'and', 'beyond'], "bedbathandbeyond")) # ['bed', 'bath', 'and', 'beyond']
            