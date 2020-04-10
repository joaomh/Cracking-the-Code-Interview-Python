"""
1.4 Palindrome Permutation:
 Given a string, write a function to check if it is a permutation of a palin­
drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.)
https://github.com/joaomh/Cracking-the-Code-Interview-Python
"""
"""
 For a string to me a Palindrome, if the len(string) is odd the middle term must be a 'mirror'
# If len(string) is even, we must count the same letters duplicate
# Example:
  r a c e c a r
  1 2 3 4 3 2 1
# My solution
# We need to but the string in the dictionary
"""
# My solution
# O(n)
def palindrome(str1):

    # Normalize the string, assuming that the strings contains only alph A-Z
    str1 = str1.lower()
    str1 = str1.replace(" ", "")

    # Create a hash table
    dic = dict()
    count = 0

    for char in str1:
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1
    
    for key, value in dic.items():
        # If the value in this loop is odd and we don't find a odd value yet
        if value % 2 != 0 and count == 0:
            count += 1
        elif value % 2 != 0 and count != 0:
            return False

    return True
# Test
print(palindrome('Tact Coa'))
print(palindrome('racecar'))
