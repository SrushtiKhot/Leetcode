class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l,h=0,len(nums)-1
        while l<h:
            m=(l+h)//2
            if nums[m]<nums[m+1]: # here m is low mid so here is nerver a case m+1 = h while l<h
                l=m+1 # possible answer right side without the mid            
            if nums[m] > nums[m+1]:
                h=m # possible answer left side the mid
        return h 
        