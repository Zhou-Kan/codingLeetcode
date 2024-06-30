# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def traverse(root, pre, length):
            nonlocal res
            if not root:
                return
            
            if root.val == pre + 1:
                length += 1
            else:
                length = 1
                
            res = max(res, length)
            
            traverse(root.left, root.val, length)
            traverse(root.right, root.val, length)
            
        traverse(root, float('-inf'), 1)
        
        return res