import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def get_len(nums_arr):
            return math.sqrt((nums_arr[0] ** 2) + (nums_arr[1] ** 2))
        
        h = []
        
        for point in points:
            heapq.heappush(h, (get_len(point), point))
            
        answer = []
        
        for _ in range(k):
            answer.append(heapq.heappop(h)[1])
            
        return answer