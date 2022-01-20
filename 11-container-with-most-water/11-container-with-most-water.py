class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        amount=0
        mc=0
        
        while(l<=r):
            amount=(min(height[l],height[r]))*(r-l)
            mc=max(amount,mc)
            
            #Incrementing pointers
            if(height[l]<=height[r]):
                l+=1
                
            else:
                r-=1
                
        return(mc)
            
            
            
        