
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