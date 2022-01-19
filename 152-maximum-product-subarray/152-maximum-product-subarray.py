class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        currmax,currmin=1,1
        
        for n in nums:
            if n==0:
                #If 0 encountered, then we don't want to break the streak, so cmax,cmin=1
                currmax,currmin=1,1
                continue
                
            temp=n*currmax #As currmax gets modified in next step we need the original value to cmin
            currmax=max(n,currmax*n,currmin*n) #n can also be max val
            currmin=min(n,temp,currmin*n)
            res=max(res,currmax)
            
        return res
    
    #O(n) time complexity
    #O(1) Space complexity
            

        