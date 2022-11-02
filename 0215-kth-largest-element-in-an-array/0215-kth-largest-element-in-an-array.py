import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        
        for num in nums:
            heapq.heappush(q, -num)
            
        result = []
        while q:
            result.append(-heapq.heappop(q))
            # if len(result) == k - 1:
            #     break
                
        return result[k - 1]
            