class Solution:
    def isValid(self, s: str) -> bool:
        dict={'(':')','{':'}','[':']'}
        stack=[]
        k=list(dict.keys())
        v=list(dict.values())   
        for i in s:
            if i in k:
                stack.append(i)
            elif i in v:
                if stack==[] or (dict[stack.pop()]!=i):
                    return False
                
        return(stack==[])
    
    #O(n) Time complexity
    #O(n) Space complexity as we use stack
                
        
        