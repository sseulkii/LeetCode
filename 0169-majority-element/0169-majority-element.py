class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        
        for n in nums:
            if n not in d:
                d[n] = nums.count(n)
            if d[n] > (len(nums) // 2):
                return n