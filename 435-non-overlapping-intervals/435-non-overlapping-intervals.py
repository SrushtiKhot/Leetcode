class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count=0
        intervals.sort()
        end=intervals[0][1]
        
        if not intervals:
            return False  
        
        for i in range(1,len(intervals)):
            if(intervals[i][0]<end):
                count+=1
                end=min(end,intervals[i][1])
                #change end and inc count
                
            else:
                end=intervals[i][1]
                
                
        return count
                
            

        