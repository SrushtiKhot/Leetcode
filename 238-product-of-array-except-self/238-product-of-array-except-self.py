class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res=[1]*len(nums) 
        pre=1 #As initial nums[0] doesnot have any element before, keep 1 
        for i in range(len(nums)): 
            res[i]=pre  #First calculate pre and add to next index
            pre=pre*nums[i]
            
        post=1
        for i in range(len(nums)-1,-1,-1): #Start from end as there is no element infront of lastele
            res[i]*=post #multiply post to ele in res
            post=post*nums[i]
            
        return res
        
        
    #O(n) time complexity
    #O(n) Space complexity