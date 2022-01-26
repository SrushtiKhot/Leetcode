class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        l1=list(s)
        stack=[]
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)     
            elif s[i]==')':
                if stack:
                    stack.pop()
                else:
                    l1[i]=''
                    
        for i in stack:
            l1[i]=''
        
        
        return ''.join(l1)
        