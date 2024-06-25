# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        depth = 0
        
        def traverse(root):
            nonlocal res, depth
            if not root:
                return 0
            
            depth += 1
            res = max(res, depth)
            
            
            traverse(root.left)
            traverse(root.right)
            
            depth -= 1
            
        traverse(root)
        return res