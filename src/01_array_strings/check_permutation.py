# 1.2 Check Permutation: 
# Given two strings, write a method to decide if one is a permutation of the other.
# https://github.com/joaomh/Cracking-the-Code-Interview-Python

# My solution
def Permutation(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    for character in str1:
        if character is ' ':
            pass
        elif character in str2:
            str2 = str2.replace(character, '', 1)
        else:
            return False
        
    if len(str2.replace(' ','')) == 0:
         return True
    else:
         return False


# Test
print("Pass" if Permutation('he llo','elhlo') else "Fail")
print("Pass" if Permutation('he was there','theresaweh') else "Fail")
