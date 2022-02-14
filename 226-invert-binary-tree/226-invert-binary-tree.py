# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Recursion T.C- O(h) Height of tree
#         if not root:
#             return None
        
#         temp=root.left
#         root.left=root.right
#         root.right=temp
        
#         self.invertTree(root.left)
#         self.invertTree(root.right)
        
#         return root
    
        
        #Iterative T.C- O(n) Number of nodes in tree 
        q=collections.deque()
        q.append(root)
        while q:
            node=q.popleft()
            if node:
                node.left,node.right=node.right,node.left  #Inverting the tree
                q.append(node.left)
                q.append(node.right)
        return root

        