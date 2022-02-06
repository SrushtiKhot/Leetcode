class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      #Brute force approach 
      #Time complexity O(n^2) and space complexity is O(1) as we just return True/False
#         if not nums:
#             return False
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]==nums[j]:
#                     return True 
#         return False

        #One line code using set Time complexity= O(n) Space complexity O(n)
#         return len(nums)!=len(set(nums)) 

        #Using Sort T.C- O(nlogn) S.C- O(1)
        
        nums.sort()
        for i in range(len(nums)-1):
            if(nums[i]==nums[i+1]):
                return True
            
        return False
        
        
    
                    
                    
                
                
            
            
                
    
        