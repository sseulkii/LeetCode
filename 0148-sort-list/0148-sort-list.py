# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
            
        arr.sort()
        
        node = head = ListNode()
        
        for n in arr:
            node.next = ListNode(n)
            node = node.next
            
        return head.next