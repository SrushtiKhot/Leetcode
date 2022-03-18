class Solution:
    def calculate(self, s):
        last=0
        res=0
        opr='+'
        curr=0       
        if not s:
            return 0       
        for i in range(len(s)):
            ch=s[i]          
            if ch.isdigit():
                curr=(curr*10)+(ord(ch)-ord('0'))
                print(curr)
            
            if not ch.isdigit() and not ch.isspace() or i==len(s)-1:  
                if opr=='+' or opr=='-':
                    res+=last
                    if opr=='+':
                        last=curr
                        print(last)
                    elif opr=='-':
                        last=-curr
                        print(last)
                                
                elif opr=='*':
                    last=last*curr
                elif opr=='/':
                    if (last/curr)<0 and last%curr !=0:
                        last=last//(curr)+1
                    else:
                        last=last//(curr)     
                opr=ch
                curr=0
            
        res=res+last 
        return res
    
    #O(n) Time complexity 
    #O(1) Space complexity --> Stack
    
              
        
#         if not s:
#             return "0"
#         stack, num, sign = [], 0, "+"
#         for i in range(len(s)):
#             if s[i].isdigit():
#                 num = num*10+ord(s[i])-ord("0")
#             if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1:
#                 if sign == "-":
#                     stack.append(-num)
#                 elif sign == "+":
#                     stack.append(num)
#                 elif sign == "*":
#                     stack.append(stack.pop()*num)
#                 else:
#                     tmp = stack.pop()
#                     if tmp//num < 0 and tmp%num != 0:
#                         stack.append(tmp//num+1)
#                     else:
#                         stack.append(tmp//num)
#                 sign = s[i]
#                 num = 0
#         return sum(stack)
    
    #O(n) Time complexity 
    #O(n) Space complexity --> Stack
    
    
    