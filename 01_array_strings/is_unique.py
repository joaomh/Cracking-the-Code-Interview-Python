# 1.1 Is Unique:
# Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?


# O(n)
# Assuming ASCII - American Standard Code for Information Interchange
def isUniqueChars(string):
    if len(string) > 128:
        return False
    char_set = [False for _ in range(128)]
    for char in string:
        val = ord(char) # Return an integer representing the Unicode
        if char_set[val]:
            # Char already found in the string
            return False
        char_set[val] = True
    
    return True

# We can reduce our space usage by a factor of eight by using a bit vector. 
# We will assume, in the below code,that the string only uses the lowercase letters a through 
def InUnique(string):
    checker = 0
    for char in string:
        val = ord(char) - ord('a')
        if (checker & (1 << val)) < 0:
            return False
        checker |= 1 << val
    return True

if __name__ == '__main__':

    string = 'abcd'
    test_one = isUniqueChars(string)
    test_two = InUnique(string)
    print(test_one)
    print(test_two)
