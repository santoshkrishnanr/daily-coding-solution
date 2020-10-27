
"""
This problem was asked by Twitter.
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""


def get_automatic(l,dictionary):
    list_=[]*len(dictionary)

    for i in range(len(dictionary)):
            if l in dictionary[i]:
                list_.append(dictionary[i])
    return list_


print(get_automatic("de", ["dog", "deer", "deal"]))

assert get_automatic("de", ["dog", "deer", "deal"]) == ["deer", "deal"]
assert get_automatic("ca", ["cat", "car", "cer"]) == ["cat", "car"]
assert get_automatic("ae", ["cat", "car", "cer"]) == []
assert get_automatic("ae", []) == []
