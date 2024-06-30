# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        
        res = []
        
        def traverse(root):
            if not root:
                return 
            
            traverse(root.left)
            res.append(root)
            traverse(root.right)
            
        traverse(root)
        
        for i in range(len(res)):
            if res[i].val > p.val:
                return res[i]
            
        return None
         