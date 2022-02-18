# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    #O(nlogn) Time complexity --> n for number of nodes and nlogn for sorting
    #O(n) Sapce complexity
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if not root:
        #     return
        # count=defaultdict(list) #nodes with horizontal distances
        # res=[]
        # q=collections.deque()
        # q.append((root,0)) #hd of root is 0
        # while q:
        #     node,hd=q.popleft()
        #     count[hd].append(node.val)
        #     if node.left:
        #         q.append((node.left,hd-1))
        #     if node.right:
        #         q.append((node.right,hd+1))
        # d=sorted(count.items()) #Sort dictionary on the basis of key
        # d1=dict(d).values()
        # for i in d1:
        #     res.append(i)
        # return(res)
        
        # return [count[i] for i in sorted(count.keys())]
    
#Optimal approach
#Time complexity O(N) No sorting is required
#O(n) to store hash
    
        if not root:
            return []
        minimum,maximum=0,0
        q=collections.deque()
        q.append((root,0)) #0 is col number
        count=defaultdict(list)
        while q:
            node,hd=q.popleft()
            if node:
                count[hd].append(node.val)
                minimum=min(hd,minimum)  #To calculate the range of min and max hashindex count
                maximum=max(hd,maximum)
                q.append((node.left,hd-1))
                q.append((node.right,hd+1))

        return([count[i] for i in range(minimum,maximum+1)])
            
           
            
            
            
            
            
        
        
    
                
        
        