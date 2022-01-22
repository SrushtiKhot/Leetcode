class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet=set()
        res=0 #To keep track of previous result(Lenght of sliding window) and find the max 
        l=0
        for r in range(len(s)): #r points from 0 to len(s)
            
            #This while loop runs until duplicate of s[r] gets removed from the charset
            while(s[r] in charSet): #If duplicate found,
                
                #Shrink window and remove s[l] from set
                charSet.remove(s[l])
                l+=1
        #If no duplicate found,add it to the set
            charSet.add(s[r])
            res=max(res,r-l+1)        
        return res
    
#O(n) Time complexity as we use sliding window technique
#O(n) Space complexity