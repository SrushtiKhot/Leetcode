class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1  
        while(l<=r):
            mid=(l+r)//2  
            if nums[mid]==target: 
                return mid
            
            elif nums[l]<=nums[mid]: #Left sorted portion
                if(target>=nums[l] and target<nums[mid]): #If target in btn nums[l] and nums[mid]
                    r=mid-1 #Search left sorted portion
                else:
                    l=mid+1 #Saerch right      
                    
            else: #Right sorted portion         
                if(target<=nums[r] and target>nums[mid]):#If target in btn nums[mid] and nums[r]
                    l=mid+1     #Search right part
                else:
                    r=mid-1                #Search left
        return -1
    
    #O(logn) time complexity
    #O(1) Space complexity