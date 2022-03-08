class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #O(nlogn) because of sort function
#         nums.sort()
#         return(nums[len(nums)-k])
        
        #O(n)average case time complexity of quickselect. Worst case is O(n^2)
        #n+n/2+n/4+...n/n =2n
    
    
        k=len(nums)-k
        return(self.quickselect(0,len(nums)-1,nums,k))

        #Using quick select
    def quickselect(self,l,r,nums,k):
        pivot=nums[r]
        p=l
        for i in range(l,r):
            if nums[i]<=pivot:
                nums[i],nums[p]=nums[p],nums[i]
                p+=1
                
        nums[p],nums[r]=nums[r],nums[p]
        if(p<k): #Search right
            return self.quickselect(p+1,r,nums,k)
        elif p>k:
            return self.quickselect(l,p-1,nums,k)
        else:
            return(nums[p])

        
                
    
        
    
        
        
        