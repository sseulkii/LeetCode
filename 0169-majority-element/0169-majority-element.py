class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
                
        return sorted(([(k,v) for k, v in d.items()]), key = lambda x: x[1], reverse = True)[0][0]