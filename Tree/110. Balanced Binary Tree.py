'''
110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.res = True
        
        def dfs(rt):
            if not rt:
                return 0
            count_left = 1 + dfs(rt.left)
            count_right = 1 + dfs(rt.right)

            if abs(count_left - count_right) > 1:
                self.res = False
            return max(count_left, count_right)
            

        dfs(root)   
        return self.res

# print(Solution().isBalanced(TreeNode(3,TreeNode(9,TreeNode(20),TreeNode(15)),TreeNode(7))))
print(Solution().isBalanced(TreeNode(1,TreeNode(2,TreeNode(2),TreeNode(3)),TreeNode(3,TreeNode(4),TreeNode(4)))))