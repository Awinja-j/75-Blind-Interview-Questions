'''
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
 

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
'''
from collections import Counter

def removeDuplicateLetters(s: str) -> str:
    stack = []
    counter = dict()
    for index,ch in enumerate(s):
            counter[ch] = index
    
    for k, v in enumerate(s):
        if v not in stack:
            while stack and stack[-1] > v and counter[stack[-1]] > k:
                stack.pop()
            stack.append(v)
    return ''.join(stack)






    # for i in s:
    #     if i not in letter:
    #         letter.add(i)
    #         counter[i] -= 1
    #         while stack and stack[-1] > i and counter[stack[-1]] > 0:
    #             letter.remove(stack.pop())
    #         stack.append(i)
    # return ''.join(stack)
# print(removeDuplicateLetters('bcabc'))
# print(removeDuplicateLetters('cbacdcbc'))
# print(removeDuplicateLetters('bcabc'))
# print(removeDuplicateLetters('cbacdcbc'))
print(removeDuplicateLetters('bbcaac'))