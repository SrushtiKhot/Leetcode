# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        #Level order traversal
        if not root:
            return     
        res=[]
        s=0  
        q=collections.deque()
        q.append(root)
        while q:
            node=q.popleft()
            res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)               
        if res:
            for i in res:
                if i in range(low,high+1):
                    s+=i
        return s
        
        