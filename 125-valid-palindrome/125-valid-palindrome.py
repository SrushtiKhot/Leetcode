class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''     
        h=''
        for c in s.lower(): #All characters should be converted to lower case
            if c.isalnum(): #If characters are alphanumeric add to the result
                h+=c             
        return h==h[::-1]  #Check if palindrome
    #O(n) Time complexity
    #O(n) Space complexity
    '''
        l, r = 0, len(s) - 1
        while l < r:
            if s[l].isalnum() and s[r].isalnum():
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
            else:
                if not s[l].isalnum():
                    l += 1
                if not s[r].isalnum():
                    r -= 1
        return True
    
        
        #O(n) Time complexity
        #O(1) Space complexity
    
                
            
            
            
            
        
    
          
    
    
            
        
        