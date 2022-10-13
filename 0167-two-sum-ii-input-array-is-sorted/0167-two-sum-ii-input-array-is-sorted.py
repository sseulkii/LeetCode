from bisect import bisect_left

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for k, v in enumerate(numbers):
            expected = target - v
            
            idx = bisect_left(numbers, expected, lo = k + 1, hi = len(numbers))
            if idx < len(numbers) and numbers[idx] == expected:
                return [k + 1, idx + 1]