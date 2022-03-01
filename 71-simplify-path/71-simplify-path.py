class Solution:
    def simplifyPath(self,path):
        stack=[]
        l=path.split('/')
        for part in l:
            if part=='.' or not part:
                continue
                
            elif part=='..':
                 if stack:
                    stack.pop()
                
            else:
                stack.append(part)
                
        final_str='/'+'/'.join(stack)
        return final_str
    



