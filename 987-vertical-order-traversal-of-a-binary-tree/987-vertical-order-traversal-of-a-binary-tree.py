# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import defaultdict

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        position_to_node = defaultdict(list)
        groups = defaultdict(list)
        queue = deque()
        queue.append((root, 0, 0))
        position_to_node[(0, 0)].append(root.val)
        
        while queue:
            node, row, col = queue.popleft()
            
            if node.left:
                position_to_node[(row + 1, col - 1)].append(node.left.val)
                queue.append((node.left, row + 1, col - 1))
                
            if node.right:
                position_to_node[(row + 1, col + 1)].append(node.right.val)
                queue.append((node.right, row + 1, col + 1))
                
        # Because the items are sorted first by col and then by row, our answer is generated in the
        # correct order as well.
        #print(position_to_node)
        
        items = sorted(position_to_node.items(), key = lambda x: (x[0][1])) #Sort items on basis of column 
        print(items)
        
        for item in items:
            g = sorted(item[1])   #If there are more than 1 element in same row,col they should be stored in sorted order
            groups[item[0][1]].extend(g)  #Store the sorted order
            
     
        return [nodes for nodes in groups.values()]
    
    
    #Time complexity O(nlogn) as sort is used
    #Space complexity O(n) as we use list to store nodes 
        
            
    
                
       
            
       
        
            
    
                
       
            
       
        

                
                
                
            
                
        
            
            
        
        
        
        
        