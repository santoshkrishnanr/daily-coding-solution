"""
This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings. 
The basic idea is to represent repeated successive characters as a single count and character. 

For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
Implement run-length encoding and decoding. 
You can assume the string to be encoded have no digits and consists solely of alphabetic characters. 
You can assume the string to be decoded is valid.
"""
def encode(string):
    i = 0
    encoded = ""
    while i < len(string):
        char = string[i]
        count = 0
        while (i < len(string) and string[i] == char):
            count += 1
            i += 1
        encoded += str(count) + char
    return encoded 
        
def decode(string):
    i = 0
    decoded = ""
    while i < len(string):
        count = int(string[i])
        char = string[i+1]
        decoded += count * char
        i += 2
    return decoded

string = "AAAABBBCCDAA"
encoded = encode(string)
print(encoded) # 4A3B2C1D2A
print(decode(encoded)) # AAAABBBCCDAA