class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
                
        items = sorted(d.items(), key = lambda x: x[1], reverse = True)
        return items[0][0]