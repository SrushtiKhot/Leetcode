from collections import defaultdict
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res=sorted(points,key=lambda x:(x[0]*x[0])+x[1]*x[1])
        print(res)
        return res[:k]
        
            
    
            
          
        