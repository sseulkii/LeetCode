class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary_search(arr, start, end, target):
            if start > end:
                return -1
        
            mid = (start + end) // 2
        
            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                return binary_search(nums, start, mid - 1, target)
            
            else:
                return binary_search(nums, mid + 1, end, target)
            
        return binary_search(nums, 0, len(nums) - 1, target)