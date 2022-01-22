class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Valid window condition: windowlength-maxoccuring count <=k
        #In order to have lesser k , we need to replace the maximum frequency element
        #If window is invalid, we just shrink the window l+=1 and remove s[l]
        
        count={}          #Keep count of all chars in string
        res=0
        l=0
        maxf=0
        for r in range(len(s)):
            count[s[r]]=1+count.get(s[r],0)   #Get count of all chars in s 
            maxf=max(maxf,count[s[r]])
            
            #Invalid window(we donot have sufficient k to rep) 
            #while (r-l+1)-max(count.values())>k:
            #maxf is used so that we don't traverse whole dict to find max element
            while((r-l+1)-maxf)>k: #
                count[s[l]]-=1  #Shrink window 
                l+=1                
            res=max(res,r-l+1)    
        return res
    
    #O(26 n) which equals O(n) Time complexity
    #O(1) Space complexity
    
    #O(n) Time complexity if maxf is used
    
    
    
    
    
    
    
    
        