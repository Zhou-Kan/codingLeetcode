# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def dfs(root, min_value, max_value):
            if not root:
                return True
            
            if root.val > min_value and root.val < max_value:
                return dfs(root.right, max(min_value, root.val), max_value) and dfs(root.left, min_value, min(root.val, max_value))
            else:
                return False
            
            
        return dfs(root, float('-inf'), float('inf'))
        