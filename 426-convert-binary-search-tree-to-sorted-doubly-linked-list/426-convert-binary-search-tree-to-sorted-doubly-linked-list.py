"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def helper(self,node):      
            if node:
                helper(self,node.left)              
                self.prev.right=node
                node.left=self.prev
                self.prev=node             
                helper(self,node.right)
        
        if not root:
            return None
        
        self.head=Node(0)
        self.prev=self.head
        helper(self,root)
        self.prev.right = self.head.right
        self.head.right.left=self.prev
        return self.head.right
            
        