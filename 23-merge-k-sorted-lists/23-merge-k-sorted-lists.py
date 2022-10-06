# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        arr = []
        
        for list in lists:
            while list:
                arr.append(list.val)
                list = list.next
                
        arr.sort()
        
        start = node = ListNode()
        
        for num in arr:
            node.next = ListNode(num)
            node = node.next
            
        return start.next