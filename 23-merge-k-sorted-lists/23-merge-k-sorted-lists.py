import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        h = []
        
        for list in lists:
            while list:
                heapq.heappush(h, list.val)
                list = list.next
                
        head = node = ListNode()
        
        while h:
            node.next = ListNode(heapq.heappop(h))
            node = node.next
            
        return head.next