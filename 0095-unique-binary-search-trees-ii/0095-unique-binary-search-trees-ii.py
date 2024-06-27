# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def build(l, r):
            if l > r:
                return [None]
            ans = []
            
            for i in range(l, r + 1):
                for left in build(l, i - 1):
                    for right in build(i + 1, r):
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        ans.append(root)
            return ans
        
        return build(1, n)
        