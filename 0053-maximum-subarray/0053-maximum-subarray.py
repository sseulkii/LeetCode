class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        inf = int(1e9)
        dp = [-inf] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i], dp[i-1] + nums[i], nums[i])
        return max(dp)