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
        q=collections.deque()
        q.append([root,1])
        res=0
        #level=0 
        while q:
            for i in range(len(q)):
                #node=q.popleft() 
                node,depth=q.pop()
                res=max(res,depth)
                if node.left:
                    q.append([node.left,depth+1])
                if node.right:
                    q.append([node.right,depth+1])
            #level+=1
            
        return res
        
        
                
            
            
        