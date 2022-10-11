import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def get_len(nums_arr):
            return math.sqrt((nums_arr[0] ** 2) + (nums_arr[1] ** 2))
        
        arr = []
        for i, nums in enumerate(points):
            arr.append((get_len(nums), i))
            
        arr.sort(key = lambda x: x[0])
        
        answer = []
        for i in range(k):
            answer.append(points[arr[i][1]])
            
        return answer