class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(set(nums1))
        nums2 = sorted(set(nums2))
        i, j = 0, 0
        
        ret = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                ret.append(nums1[i])
                i += 1
                j += 1
            
            elif nums1[i] > nums2[j]:
                j += 1
            
            else:
                i += 1
                
        return ret