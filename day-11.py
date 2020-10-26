
"""
This problem was asked by Facebook.
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed.
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
