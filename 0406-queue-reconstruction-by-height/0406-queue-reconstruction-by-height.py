import heapq

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        q = []
        
        for person in people:
            heapq.heappush(q, (-person[0], person[1]))
            
        result = []
        
        while q:
            h, k = heapq.heappop(q)
            result.insert(k, [-h, k])
            
        return result
