import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
                
        h = []
        
        for key, val in d.items():
            heapq.heappush(h, (-val, key))
            
        answer = []
        
        while k:
            answer.append(heapq.heappop(h)[1])
            k -= 1
            
        return answer