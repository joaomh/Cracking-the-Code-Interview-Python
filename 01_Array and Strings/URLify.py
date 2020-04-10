"""
1.3 URLify: 
Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string.
EXAMPLE
Input: "Mr John Smith", 13
Output: "Mr%20John%20Smith"
https://github.com/joaomh/Cracking-the-Code-Interview-Python
"""
def URLify(string):

    count = 0
    for char in string:
        if char is ' ':
           count += 1
    string = string.replace(' ', '%20',count)
    return string

# Test
print(URLify('Mr John Smith'))
print(URLify('Mr John Smith is a good man'))