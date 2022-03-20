class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp=set()
        dp.add(0)
        
        if sum(nums)%2:
            return False 
        target=sum(nums)//2
        for i in range(len(nums)-1,-1,-1):
            nextDP=set()
            for t in dp:
                    nextDP.add(t+nums[i])
                    nextDP.add(t)       
            dp=nextDP
            
        if target in dp:
            return True
        
        else:
            return False
                    
        