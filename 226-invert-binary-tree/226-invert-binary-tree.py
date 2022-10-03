# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        root.left, root.right = root.right, root.left
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
        
#         def invert(node):
#             if not node.left and not node.right:
#                 return node
            
#             if not node.left:
#                 node.left = invert(node.right)
#                 node.right = None
#                 return node
            
#             if not node.right:
#                 node.right = invert(node.left)
#                 node.left = None
#                 return node
            
#             left = invert(node.left)
#             right = invert(node.right)
                
#             node.left, node.right = right, left
            
#             return node
        
#         return invert(root)