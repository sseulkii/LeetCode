class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        d = [0] * n
        
        if n == 1:
            return nums[0]
        
        d[0] = nums[0]
        d[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            d[i] = max(d[i-1], d[i-2] + nums[i])
            
        return d[-1]