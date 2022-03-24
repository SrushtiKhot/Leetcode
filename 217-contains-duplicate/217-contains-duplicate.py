class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap={}
        for n in nums:
            hashmap[n]=1+hashmap.get(n,0)
            
        if(max(hashmap.values())>1):
            return True
        else:   
            return False
        
        #O(n) time complexity
        #O(n) Space complexity to store hashmap
        