class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Using sort T.C- O(nlogn) S.C- O(n)
        
#         if len(s)!=len(t):
#             return False
        
#         s=sorted(s)  #Strings are immutable so you cannot use sort(s)
#         t=sorted(t)
        
#         return(s==t)

        
        #Using hashmap T.C- O(n) S.C= O(n)
        
        if len(s)!=len(t):
            return False
        
        hash={}
        for i in s:
            hash[i]=1+hash.get(i,0)
            
        for j in t:
            if j in hash:
                hash[j]-=1
                
        return(max(hash.values())==0)
    