from bisect import bisect_left

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for mat in matrix:
            idx = bisect_left(mat, target)
            if idx < len(mat) and mat[idx] == target:
                return True
        return False