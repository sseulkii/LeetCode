# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        
        while head:
            arr.append(head.val)
            head = head.next
            
        # arr_odd = [arr[i] for i in range(len(arr)) if (i % 2) == 0]
        # arr_even = [arr[i] for i in range(len(arr)) if (i % 2) == 1]
        
        arr_odd, arr_even = [], []
        
        for i in range(len(arr)):
            if i % 2 == 0:
                arr_odd.append(arr[i])
            else:
                arr_even.append(arr[i])
        
        arr = arr_odd + arr_even
        
        start = node = ListNode()
        
        for n in arr:
            node.next = ListNode(n)
            node = node.next
            
        return start.next