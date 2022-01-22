class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Valid window condition: windowlength-maxoccuring count <=k
        #In order to have lesser k , we need to replace the maximum frequency element
        #If window is invalid, we just shrink the window l+=1 and remove s[l]
        
        count={}          #Keep count of all chars in string
        res=0
        l=0
        for r in range(len(s)):
            count[s[r]]=1+count.get(s[r],0)           
            while (r-l+1)-max(count.values())>k: #Invalid window
                count[s[l]]-=1
                l+=1                
            res=max(res,r-l+1)    
        return res
        
        