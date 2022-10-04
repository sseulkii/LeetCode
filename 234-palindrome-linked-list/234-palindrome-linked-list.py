# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        q = deque([])
        
        node = head
        
        while node:
            q.append(node.val)
            node = node.next
            
        while q:
            if len(q) == 1:
                return True
            if q.popleft() != q.pop():
                return False
            
        return True