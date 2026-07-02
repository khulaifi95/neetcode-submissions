# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = deque()

        q.append((root, -float('inf')))

        while q:
            node, maxv = q.popleft()
            if node.val >= maxv:
                res += 1
            if node.left:
                q.append((node.left,max(maxv,node.val)))
            if node.right:
                q.append((node.right,max(maxv,node.val)))
        return res