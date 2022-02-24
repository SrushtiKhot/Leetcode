"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        hash1=[]
        hash2=[]
        while p:
            hash1.append(p)
            p=p.parent
            
            
        while q:
            hash2.append(q)
            q=q.parent
            
        for i in hash1:
            if i in hash2:
                return i
                
        
        