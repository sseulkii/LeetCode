class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_enum = sorted(enumerate(nums), key = lambda x: x[1])
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums_enum[left][1] + nums_enum[right][1] == target:
                return [nums_enum[left][0], nums_enum[right][0]]
            elif nums_enum[left][1] + nums_enum[right][1] < target:
                left += 1
            else:
                right -= 1