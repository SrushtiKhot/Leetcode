# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        #Recursion 
#         if(p==None and q==None):
#             return True
#         if(p==None or q==None):
#             return False
#         if(p.val!=q.val):
#             return False
        
#         return(self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left))
    
    
        #Using stack
        stack=[(p,q)]
        while stack:
            p,q=stack.pop()
            if not p and not q:
                continue
                
            if(not p or not q) or (p.val!=q.val):
                return False
            
            stack.extend([(p.left,q.left),(p.right,q.right)])
            
        return True
                
        
        