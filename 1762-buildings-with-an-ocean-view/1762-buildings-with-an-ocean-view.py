class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_h=-1
        res=[]
        for i in range(len(heights)-1,-1,-1):
            if(heights[i]>max_h):
                max_h=heights[i]
                res.append(i)
        res.sort()  
        return res
                
        