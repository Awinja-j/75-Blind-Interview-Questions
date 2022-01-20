"""
680. Valid Palindrome II
Easy

3737

226

Add to List

Share
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
"""

def validPalindrome(s: str) -> bool:
    if not s: return False
    if len(s) == 1: return True
    if s == s[::-1]: return True 
        
    count = 0
    start = 0
    end = len(s) - 1
        
    while start< end:
        if s[start] != s[end]:
            d = s[:start] + s[start + 1:]
            m = s[:end] + s[end + 1:]
            return d == d[::-1] or m == m[::-1]
        start += 1
        end -= 1
    return True
    

print(validPalindrome("aba"))
print(validPalindrome("abca"))
print(validPalindrome("abc"))