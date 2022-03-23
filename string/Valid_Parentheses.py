"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

def isValid(s: str) -> bool:
    #1. make list of open brackets
    #2. check if close brackets match open brackets
    #3. if not, return false
    #4. if yes, return true

    #1. make list of open brackets
    lp = ['(', '[', '{']
    rp = [')', ']', '}']

    count = 0
    open_brackets = []
    for i in s:
        if i in lp:
            open_brackets.append(i)
            count += 1
        elif i in rp:
            if len(open_brackets) == 0:
                return False
            elif open_brackets[-1] == lp[rp.index(i)]:
                open_brackets.pop()
                count -= 1
            else:
                return False
    if count == 0:
        return True
    else:
        return False

print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("()[]{}[]"))