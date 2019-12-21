"""
This problem was asked by Facebook.

Implement regular expression matching with the following special characters:

    . (period) which matches any single character
    * (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.
"""
# Return True if string matches pattern else False
def regex(string, pattern):
    string_index = 0
    pattern_index = 0
    while string_index < len(string) and pattern_index < len(pattern):
        if pattern[pattern_index] == ".":
            pattern_index += 1
            string_index += 1
        if pattern[pattern_index] == string[string_index]:
