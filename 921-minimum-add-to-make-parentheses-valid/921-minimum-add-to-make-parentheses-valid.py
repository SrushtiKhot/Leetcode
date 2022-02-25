class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        bal=0
        min_add=0
        for i in s:
            if i=='(':
                bal+=1
            elif i==')' and bal>0:
                bal-=1
                
            else:
                min_add+=1
                
        return min_add+bal
                
                
                
#         stack=[]
#         min_add=0
#         for i in s: #O(n)
#             if i=='(':
#                 stack.append(i)
#             elif i==')' and stack:
#                 stack.pop()
#             else:
#                 min_add+=1
                
#         if stack: #O(stack size)
#             for i in stack:
#                 min_add+=1
                
#         return min_add

         