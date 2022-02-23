class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzero={}
        for i,n in enumerate(nums):
            if n!=0:
                self.nonzero[i]=n
                
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans=0
        for i in self.nonzero:
            if i in vec.nonzero:
                ans+=self.nonzero[i]*vec.nonzero[i]
                
                
        return ans
            
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)