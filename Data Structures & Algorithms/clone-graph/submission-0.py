"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == []:
            return []
        
        old_new_mapping = {}        #hashmap to keep track of visited/cloned nodes
        def dfs(node):
            if node in old_new_mapping:             # if already cloned, just return
                return old_new_mapping[node]
            
            #create a new node with the deets of this node
            copy = Node(node.val)
            old_new_mapping[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy
        
        return dfs(node) if node else None

        

        