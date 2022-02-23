class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ans=[]
        for i in range(len(heights)):
            while ans and heights[i]>=heights[ans[-1]]:
                ans.pop()
                
            ans.append(i)
            
        return ans
                
        