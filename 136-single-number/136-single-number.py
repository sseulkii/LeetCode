class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
                
        return (min(d.items(), key = lambda x: x[1]))[0]