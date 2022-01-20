class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output=[intervals[0]]
        
        for start,end in intervals[1:]: #Start traversing from 2nd interval(index 1)
            prevend=output[-1][1] 
            if start>prevend:    #Not overlapping
                output.append([start,end])
            else:
                #Overlapping
                output[-1][1]=max(end,prevend)
                
        return output
    
    #O(n) Time complexity
    #O(n) Space complexity