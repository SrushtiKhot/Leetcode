class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt  = collections.Counter(s1)
        l = 0 
        r = 0
        
        while (r<len(s2)):
            
            if(r-l+1 < len(s1)):
                r+=1
                
            elif(r-l+1 == len(s1)):
                if(collections.Counter(s2[l:r+1]) == cnt):
                    return True
                r+=1
                l+=1
                
        return False
        