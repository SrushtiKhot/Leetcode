class Solution:
    def countSubstrings(self, s: str) -> int:
        res=0
        for i in range(len(s)):
            l,r=i,i         #To count palindrome in odd length
            while(l>=0 and r<len(s) and s[l]==s[r]):
                    res+=1
                    l-=1
                    r+=1
            
            l,r=i,i+1      #To count palindrome in even numbers
            while(l>=0 and r<len(s) and s[l]==s[r]):
                    res+=1
                    l-=1
                    r+=1
                
        return res
        
        #O(n^2) Time complexity
        #O(1) Space complexity