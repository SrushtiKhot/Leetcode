class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr=0    
        maxsum=nums[0] #Initially maxsum is the first number        
        
        for n in nums: 
            if curr<0: #if negative make it as 0
                curr=0
                
            curr=curr+n
            maxsum=max(curr,maxsum)
            
        return maxsum