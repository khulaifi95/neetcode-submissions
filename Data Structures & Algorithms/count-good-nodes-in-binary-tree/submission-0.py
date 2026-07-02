# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(root, mval):
            if not root:
                return 0
            res = 1 if root.val >= mval else 0
            mval = max(mval, root.val)
            res += dfs(root.left, mval)
            res += dfs(root.right, mval)
            return res
        
        return dfs(root, root.val)
