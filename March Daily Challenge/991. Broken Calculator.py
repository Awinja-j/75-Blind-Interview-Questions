'''
There is a broken calculator that has the integer startValue on its display initially. In one operation, you can:

multiply the number on display by 2, or
subtract 1 from the number on display.
Given two integers startValue and target, return the minimum number of operations needed to display target on the calculator.

 

Example 1:

Input: startValue = 2, target = 3
Output: 2
Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.
Example 2:

Input: startValue = 5, target = 8
Output: 2
Explanation: Use decrement and then double {5 -> 4 -> 8}.
Example 3:

Input: startValue = 3, target = 10
Output: 3
Explanation: Use double, decrement and double {3 -> 6 -> 5 -> 10}.
 

Constraints:

1 <= x, y <= 109
'''
'''
Approach 1: Work Backwards
Intuition

Instead of multiplying by 2 or subtracting 1 from startValue, we could divide by 2 (when target is even) or add 1 to target.

The motivation for this is that it turns out we always greedily divide by 2:

If say target is even, then if we perform 2 additions and one division, we could instead perform one division and one addition for less operations [(target + 2) / 2 vs target / 2 + 1].

If say target is odd, then if we perform 3 additions and one division, we could instead perform 1 addition, 1 division, and 1 addition for less operations [(target + 3) / 2 vs (target + 1) / 2 + 1].

Algorithm

While target is larger than startValue, add 1 if it is odd, else divide by 2. After, we need to do startValue - target additions to reach startValue.
'''

def brokenCalc(self, startValue: int, target: int) -> int:
    ans = 0
    while target > startValue:
        ans += 1
        if target % 2: # if target is even
            target += 1
        else:  # if odd, then 
            target //= 2

    return ans + startValue - target

print(brokenCalc(brokenCalc, 2, 3))
print(brokenCalc(brokenCalc, 5, 8))
print(brokenCalc(brokenCalc, 3, 10))