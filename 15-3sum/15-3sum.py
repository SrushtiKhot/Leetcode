class Solution(object):
    def threeSum(self, nums):
        res=[]
        nums.sort()
        for i,n in enumerate(nums):
            if(i>0 and nums[i-1]==n): #skip if duplicates occur [-3,-3,1,2] skip -3 encountered at 1
                continue
                
            #Two sum on remaining elements
            l,r=i+1,len(nums)-1
            
            while l<r:
                if(n+nums[l]+nums[r]>0): 
                    r-=1
                elif(n+nums[l]+nums[r]<0):
                    l+=1
                    
                else:
                    res.append([n,nums[l],nums[r]])
                    l+=1
                    
                    while(nums[l]==nums[l-1] and l<r):  #if same elements encountered,keep going
                        l+=1   
                    
        return res
    
    #O(nlogn)+O(n*2)   O(n*2) Time complexity
            
                    
        
        
        