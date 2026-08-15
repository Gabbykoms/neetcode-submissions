# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        #bfs
        if not root:
            return []
        
        res = []
        q = deque()
        q.append(root)

        while q:
            cur_sol = []
            for i in range(len(q)):
                cur = q.popleft()
                cur_sol.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(cur_sol)
        
        return res
