# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        hash_map = defaultdict(int)
        hash_map[0] = 1
        res = 0
        
        def dfs(root, path):
            if not root:
                return 
            nonlocal res
            path.append(root.val)
            
            total = sum(path)
            
            if total - targetSum in hash_map:
                res += hash_map[total - targetSum]
            
            hash_map[total] += 1
            
            dfs(root.left, path)
            dfs(root.right, path)
            
            path.pop()
            hash_map[total] -= 1
            
        dfs(root, [])
        return res
        