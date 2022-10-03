# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list_node = ListNode()
        now = list_node
        
        node1 = list1
        node2 = list2
        
        while node1 and node2:
            if node1.val <= node2.val:
                now.next = node1
                now = now.next
                node1 = node1.next
            else:
                now.next = node2
                now = now.next
                node2 = node2.next
        while node1:
            now.next = node1
            now = now.next
            node1 = node1.next
        while node2:
            now.next = node2
            now = now.next
            node2 = node2.next
        
        return list_node.next