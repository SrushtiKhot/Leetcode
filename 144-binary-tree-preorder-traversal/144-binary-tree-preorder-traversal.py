# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Recursive solution
        # res=[]
        # if root:   #Check if root is not null
        #         res.append(root.val) 
        #         self.preorderTraversal(root.left)
        #         self.preorderTraversal(root.right)
        # return res
        # #O(h) height of tree Tiem complexity
        # #O(h) Space complexity
        #Iterative solution
        stack=[]
        res=[]
        stack.append(root)
        while stack:
            node=stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
                
        return res
     #O(h) Time complexity
     #O(h) space complexity - we have to store all nodes

        
        
        
        
        
       
        
        
        
        
        
        
        
        


        