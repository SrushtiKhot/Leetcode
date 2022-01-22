class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count={}
        if(len(s)!=len(t)):
            return False
        
        for i in s:
            count[i]=1+count.get(i,0)
        for j in t:
            if j in count.keys():
                count[j]-=1
                    
        return(max(count.values())==0)
            