# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        node = head = ListNode(0)
        extra = 0
        
        while l1 and l2:
            
            extra, val = divmod((l1.val + l2.val + extra), 10)
            l1 = l1.next
            l2 = l2.next
            head.next = ListNode(val)
            head = head.next
        
        while l1:
            extra, val = divmod((l1.val + extra), 10)
            l1 = l1.next
            head.next = ListNode(val)
            head = head.next
            
        while l2:
            extra, val = divmod((l2.val + extra), 10)
            l2 = l2.next
            head.next = ListNode(val)
            head = head.next
            
        while extra:
            extra, val = divmod(extra, 10)
            head.next = ListNode(val)
            head = head.next
            
        return node.next
        
#         def l_to_n(list_node):
#             s = ""
#             while list_node:
#                 s += str(list_node.val)
#                 list_node = list_node.next
#             return int(s[::-1])
        
#         def n_to_l(num):
#             n_reverse = list(map(int, str(num)[::-1]))
#             list_node = ListNode()
#             now = list_node
#             for n in n_reverse:
#                 now.next = ListNode(val = n)
#                 now = now.next
#             return list_node.next
            
#         return n_to_l(l_to_n(l1) + l_to_n(l2))