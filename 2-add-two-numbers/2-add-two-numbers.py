# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        node = head = ListNode(0)
        extra = 0
        
        while l1 or l2 or extra:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            if extra:
                sum += extra
                
            extra, val = divmod(sum, 10)
            head.next = ListNode(val)
            head = head.next
            
        return node.next
