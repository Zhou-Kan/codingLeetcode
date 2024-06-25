# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0
        self.depth = 0
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.depth += 1
        
        self.res = max(self.res, self.depth)
        
        self.maxDepth(root.left)
        self.maxDepth(root.right)
        
        self.depth -= 1
        
        return self.res
        
        
            
        