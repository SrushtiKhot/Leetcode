class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count=0
        intervals.sort() #Easy to keep track of start and end
        end=intervals[0][1] #initial end      
        if not intervals:
            return False          
        for i in range(1,len(intervals)): #traverse from 1st to last interval 
            if(intervals[i][0]<end): #If next start is less than end the the intervals overlap  
                count+=1
                end=min(end,intervals[i][1]) #Keep min end value as we need to decrease overlapping
            else:
                end=intervals[i][1] #if not overlapping then shift end to present interval's end         
        return count
                
            
#O(n) Time complexity
#O(1) Space complexity
        