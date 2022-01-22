class Solution:
    def isPalindrome(self, s: str) -> bool:  
        h=''
        for c in s.lower():
            if c.isalnum():
                h+=c
                
        return h==h[::-1]
                
            
            
            
            
        
    
          
    
    
            
        
        