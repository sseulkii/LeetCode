# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        arr = []
        
        while head:
            arr.append(head.val)
            head = head.next
            
        for i in range(0, len(arr) - 1, 2):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            
        start = node = ListNode() # 이거 node로만 해주면 답 안나옴. 무조건 변수 두개 해줘서 하나는 고정하고 하나는 .next로 계속 이어지게 해줘야 함
        for n in arr:
            node.next = ListNode(val=n)
            node = node.next
            
        return start.next