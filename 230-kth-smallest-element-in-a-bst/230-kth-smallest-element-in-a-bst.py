# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #Perform inorder traversal and return kth elemnt as inorder is in ascending order
        stack=[]
        n=0
        curr=root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr=curr.left     
            curr=stack.pop()
            n+=1     
            if n==k:
                return curr.val      
            curr=curr.right
            
            
            
#         res=[]
#         def inorder(node):
#             if not node:
#                 return
#             inorder(node.left)
#             if len(res)==k:
#                 return
#             res.append(node.val)
#             inorder(node.right)
            
#         inorder(root)
            
#         return res[-1]

        node=root
        stack=[]
        while True:
            if node:
                stack.append(node) 
                node=node.left
            else:
                node=stack.pop()
                k-=1
                if k==0:
                    return node.val
                node=node.right
        #return node.val






            
                
        