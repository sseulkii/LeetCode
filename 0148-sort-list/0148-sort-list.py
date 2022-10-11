# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        
        arr = []
        while node:
            arr.append(node.val)
            node = node.next
            
        arr.sort()
        
        node = start = ListNode()
        
        for n in arr:
            node.next = ListNode(n)
            node = node.next
            
        return start.next