class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        # nums = []
        # i, j  = 0, 0
        # while i < len(nums1) and j < len(nums2):
        #     if nums1[i] < nums2[j]:
        #         nums.append(nums1[i])
        #         i += 1
        #     else:
        #         nums.append(nums2[j])
        #         j += 1
        # while i < len(nums1):
        #     nums.append(nums1[i])
        #     i += 1
        # while j < len(nums2):
        #     nums.append(nums2[j])
        if len(nums) % 2 == 0:
            return (nums[len(nums) // 2] + nums[(len(nums) // 2) - 1]) / 2
        else:
            return nums[len(nums) // 2]