# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        if not root:
            return 0       
        m=max(self.maxDepth(root.left), self.maxDepth(root.right))
        return (1+m)
        '''
        #BFS approach
        
        if not root:
            return 0
        q=collections.deque([root])
        level=0
        
        while q:
            for i in range(len(q)):
                node=q.popleft()
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
                    
            level+=1
            
        return level
        
        
                
            
            
        