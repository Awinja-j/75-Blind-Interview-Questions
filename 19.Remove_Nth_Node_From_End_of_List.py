"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Input: head = [1], n = 1
Output: []

Input: head = [1,2], n = 1
Output: [1]

Constraints:

The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz
"""
from typing import Optional
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverse(head):
            prev=None
            while head is not None:
                next = head.next
                head.next = prev
                prev = head
                head = next 
            
            return prev
        
        if head is None:
            return 
        
        head = reverse(head)
        
        temp = head
        
        n = n-1
        
        if n == 0:
            head = temp.next
            temp = None
            return reverse(head)
        
        for i in range(n -1 ):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        
        next = temp.next.next
 
        temp.next = None
 
        temp.next = next
        
        return reverse(head)