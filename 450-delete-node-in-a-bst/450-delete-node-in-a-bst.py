# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def succ(self,root): #Leftmost child of right subtree
        root=root.right
        while(root.left):
            root=root.left      
        return root.val
    
    def pred(self,root): #Rightmost child of left subtree
        root=root.left
        while(root.right):
            root=root.right
        return root.val
    
    def deleteNode(self,root,key):
        if not root:
            return None
        
        if key< root.val:
            #left subtree
            root.left=self.deleteNode(root.left,key)
            
        elif key>root.val:
            #Right subtree
            root.right=self.deleteNode(root.right,key)
            
        else: #key==root.val delete the current node
            if not(root.right or root.left):
                #leaf node
                root=None
                
            else: #Not leaf node
                if root.right:
                    root.val=self.succ(root)                        #Substitute root's value with it's successor
                    root.right=self.deleteNode(root.right,root.val) #delete the successor node recursively
                else:
                    root.val=self.pred(root)                        #Substitute root's value with it's successor
                    root.left=self.deleteNode(root.left,root.val)   #delete the successor node recursively  
        return root
                    
                    
             #Time complexity O(H1)+O(H2) H1-> to search. Height form root to key
                                        # H2-> To delete. Height from node to nodeto be deleted
                    
                    #O(H) Height of tree
                    
            #Space complexity O(H) Fucntion stack
            
            
            
        
    