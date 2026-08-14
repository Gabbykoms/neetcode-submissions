# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        #so diameter of any two nodes is the longest distance 
        #between them being connected by some common ancestor

        #so the diameter of a tree is the longest distance between any two
        #nodes in the tree. Because of the definition, the diameter need not
        #pass through the root of the tree

        #it does makes sense to calculate the longest distance in the left subtree and
        #same in the right subtree and add them to get the diameter.

        #we can find the diamter in every node and keep track of the maximum
        self.res = 0
        def dfs_height(node):

            if not node:        #edge case
                return 0
            
            left_h = dfs_height(node.left)
            right_h = dfs_height(node.right)

            #since we just found both heights, we might as well 
            #just get the diameter while we're at it and compare
            self.res = max(self.res, left_h + right_h)
            return 1 + max(left_h, right_h)         #returns the max height of the node
        
        dfs_height(root)            #call the helper function
        return self.res
        