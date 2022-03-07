class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n>=0:    
            return self.fastPow(x,n)
        else:
            return 1/self.fastPow(x,-n)
        
        
    def fastPow(self,x,n):
        if n==0:
            return 1.0
        half=self.fastPow(x,n//2)
        if (int(n%2))==0:
            return half*half
        else:
            return half*half*x
        
    
        
        
        
            
                