import random
class Solution:

    def __init__(self, w: List[int]):
        #Create prefix sums
        pre_sum=0
        self.prefix=[]
        for weight in w:
            pre_sum+=weight
            self.prefix.append(pre_sum)
        self.s=pre_sum
        
    def pickIndex(self) -> int:
        target=self.s*random.random()
         #find the first prefix sum that is larger than our target offset
        for pre in self.prefix:
            if pre >target:
                return self.prefix.index(pre)
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()