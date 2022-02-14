# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #Recursive
        '''
        if not p and not q:
            return True
        if not p or not q:
            return False
        if(p.val!=q.val):
            return False
        return(self.isSameTree(p.left,q.left) and
        self.isSameTree(p.right,q.right)) 
    #O(n) Time complexity
    #O(logn) in balanced tree O(n) in unbalanced tree
    '''
        #Iterative
    
        def check(p, q):
            # if both are None
            if not p and not q:
                return True
            # one of p and q is None
            if not q or not p:
                return False
            if p.val != q.val:
                return False
            return True
        
        deq = deque([(p, q),])
        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False
            
            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
                    
        return True

        #Using stack  T.C- O(h) Height of tree
        stack=[(p,q)]
        while stack:
            p,q=stack.pop()
            if not p and not q:
                continue
                
            if(not p or not q) or (p.val!=q.val):
                return False
            
            stack.extend([(p.left,q.left),(p.right,q.right)])
            
        return True
                
        
        
                
    
                
                
                

            
            
            
            
            
        