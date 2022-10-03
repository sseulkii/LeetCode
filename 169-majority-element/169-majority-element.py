class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        n = len(nums)
        
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
            if d[num] > n / 2:
                return num