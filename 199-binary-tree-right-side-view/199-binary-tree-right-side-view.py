# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q=collections.deque([root])
        res=[]
        while(q):
            l=[]
            qlen=len(q)
            rightnode=None
            for i in range(qlen):
                node=q.popleft()
                if node:
                    #l.append(node.val)
                    rightnode=node
                    q.append(node.left)
                    q.append(node.right)      
            if rightnode:
                res.append(rightnode.val)

                
        return res
        