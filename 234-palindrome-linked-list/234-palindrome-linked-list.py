# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        
        now = head
        
        while now:
            arr.append(now.val)
            now = now.next
            
        return arr == arr[::-1]