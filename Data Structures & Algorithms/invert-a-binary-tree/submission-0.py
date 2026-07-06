# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

                  

            #always start at the root.
            #look as though it were just one root and it's children then recurse

            #edge case:
            if not root:
                return None
            #we can swap directly in python
            root.left, root.right = root.right, root.left
            self.invertTree(root.left) 
            self.invertTree(root.right)
            return root
        