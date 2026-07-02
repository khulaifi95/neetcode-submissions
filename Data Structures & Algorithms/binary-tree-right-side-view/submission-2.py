# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()
        q.append(root)

        while q:
            sz = len(q)
            for i in range(sz):
                cur = q.popleft()
                if cur and cur.left:
                    q.append(cur.left)
                if cur and cur.right:
                    q.append(cur.right)
            if cur:
                res.append(cur.val)
        return res
