class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt={}   #O(s1)
        for s in s1:    #O(s1)
            if s in cnt:
                cnt[s]+=1
            else:
                cnt[s]=1     
        #cnt  = collections.Counter(s1)
        l = 0 
        r = 0   
        while (r<len(s2)):     #O(s2)
            if(r-l+1 < len(s1)):
                r+=1       
            elif(r-l+1 == len(s1)):
                if(collections.Counter(s2[l:r+1]) == cnt):   #O(s1)
                    return True
                r+=1
                l+=1            
        return False
    
    #Time complexity O(s1+s2)
    #Space complexity o(s1)
        