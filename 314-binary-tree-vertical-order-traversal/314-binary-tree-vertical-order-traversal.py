# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        count=defaultdict(list) #nodes with horizontal distances
        res=[]
        q=collections.deque()
        q.append((root,0)) #hd of root is 0
        while q:
            node,hd=q.popleft()
            count[hd].append(node.val)
            if node.left:
                q.append((node.left,hd-1))
            if node.right:
                q.append((node.right,hd+1))          
        d=sorted(count.items()) #Sort dictionary on the basis of key
        for i in dict(d).values():
            res.append(i)
        return(res)
                
        
        