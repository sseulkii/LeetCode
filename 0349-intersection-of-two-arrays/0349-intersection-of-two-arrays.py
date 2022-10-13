from bisect import bisect_left

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(set(nums1))
        nums2 = sorted(set(nums2))
        ret = []
        for n in nums1:
            idx = bisect_left(nums2, n)
            if len(nums2) > idx and nums2[idx] == n:
                ret.append(n)
                
        return ret