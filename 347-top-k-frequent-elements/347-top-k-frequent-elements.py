class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
                
        arr = sorted([item for item in d.items()], key = lambda x: x[1], reverse = True)
        
        answer = []
        
        for key, val in arr[:k]:
            answer.append(key)
            
        return answer