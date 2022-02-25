class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        min_add=0
        for i in s:
            if i=='(':
                stack.append(i)
            elif i==')' and stack:
                stack.pop()
            else:
                min_add+=1
                
        if stack:
            for i in stack:
                min_add+=1
                
        return min_add
        