# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def get_depth(node):
            while node:
                if not node.left and not node.right:
                    return 1
                
                return max(get_depth(node.left), get_depth(node.right)) + 1
            
            return 0
        
        return get_depth(root)