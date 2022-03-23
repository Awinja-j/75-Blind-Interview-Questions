""""
Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 

Example 1:

Input: s = "()"
Output: 1
Example 2:

Input: s = "(())"
Output: 2
Example 3:

Input: s = "()()"
Output: 2
 

Constraints:

2 <= s.length <= 50
s consists of only '(' and ')'.
s is a balanced parentheses string.

"""

def scoreOfParentheses(s: str) -> int:
        stack = [0] #The score of the current frame

        for x in s:
            if x == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)

        return stack.pop()

print(scoreOfParentheses("()"))
print(scoreOfParentheses("(())"))
print(scoreOfParentheses("()()"))
print(scoreOfParentheses("(()())"))
print(scoreOfParentheses("(()(()))"))