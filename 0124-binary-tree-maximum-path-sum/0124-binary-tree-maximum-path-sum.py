# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        
        def pathSum(root):
            if not root:
                return 0
            
            nonlocal res
            
            left = pathSum(root.left)
            
            right = pathSum(root.right)
            
            res = max(res, root.val + max(left, 0) + max(right, 0))
            
            return root.val + max(max(left, 0), max(right, 0))
        pathSum(root)
        return res
        
        
        
        
        
            

        
        
        
            
            
        