class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
                
        return (min(dic.items(), key = lambda x: x[1]))[0]