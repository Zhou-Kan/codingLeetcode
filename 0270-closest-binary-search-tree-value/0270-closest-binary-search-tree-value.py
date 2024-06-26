# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        res = float('inf')
        
        def traverse(root):
            nonlocal res
            if not root:
                return 
            
            if abs(root.val - target) < abs(res - target):
                res = root.val
            elif abs(root.val - target) == abs(res - target):
                res = min(res, root.val)
                
            traverse(root.left)
            traverse(root.right)
            
        traverse(root)
        
        return res
        